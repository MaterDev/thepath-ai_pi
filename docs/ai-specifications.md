# Training Data Specification

## Data Collection

### Game State Capture
```python
@dataclass
class GameStateSnapshot:
    """Represents a complete game state for training"""
    timestamp: int
    battle_state: dict
    valid_actions: list[dict]
    action_taken: Optional[dict]
    reward: float
    metadata: dict

class StateCollector:
    def __init__(self):
        self.states: list[GameStateSnapshot] = []
        self.reward_calculator = RewardCalculator()
    
    def capture_state(self, 
                     battle_state: dict,
                     valid_actions: list[dict],
                     action_taken: Optional[dict] = None) -> None:
        """Captures a game state with metadata for training"""
        reward = 0.0 if not action_taken else \
                self.reward_calculator.calculate_reward(battle_state, action_taken)
        
        snapshot = GameStateSnapshot(
            timestamp=int(time.time() * 1000),
            battle_state=battle_state,
            valid_actions=valid_actions,
            action_taken=action_taken,
            reward=reward,
            metadata={
                'difficulty': battle_state.get('difficulty', 1.0),
                'personality': battle_state.get('aiPersonality', 'BALANCED'),
                'round': battle_state.get('round', 0)
            }
        )
        self.states.append(snapshot)
```

### State Vectorization
```python
class StateVectorizer:
    """Converts game states into ML-ready tensors"""
    
    def __init__(self, max_chars: int = 8, max_effects: int = 10):
        self.max_chars = max_chars
        self.max_effects = max_effects
        
    def vectorize_state(self, state: dict) -> torch.Tensor:
        """Convert a game state into a fixed-size tensor"""
        # Character features
        char_features = []
        for char in state['characters'].values():
            features = [
                char['stats']['health'] / char['stats']['maxHealth'],
                char['stats']['attack'] / 100.0,
                char['stats']['defense'] / 100.0,
                char['stats']['speed'] / 100.0,
                char['position']['x'] / 10.0,
                char['position']['y'] / 10.0,
                len(char['status']) / self.max_effects,
                char['resources']['energy'] / char['resources']['maxEnergy']
            ]
            char_features.append(features)
        
        # Pad to max_chars
        while len(char_features) < self.max_chars:
            char_features.append([0.0] * 8)
        
        # Global features
        global_features = [
            state['round'] / 100.0,
            len(state['turnOrder']) / self.max_chars,
            state['currentTurn'] / self.max_chars
        ]
        
        return torch.tensor(char_features + [global_features])

    def vectorize_action(self, action: dict) -> torch.Tensor:
        """Convert an action into a fixed-size tensor"""
        # One-hot encode action type
        action_types = ['ABILITY', 'MOVE', 'WAIT', 'DEFEND']
        type_vec = [1.0 if t == action['type'] else 0.0 for t in action_types]
        
        # Encode target position
        pos = action.get('movement', {}).get('path', [{'x':0, 'y':0}])[-1]
        pos_vec = [pos['x'] / 10.0, pos['y'] / 10.0]
        
        # Encode ability if present
        ability_vec = [0.0] * NUM_ABILITIES
        if action['type'] == 'ABILITY' and action.get('ability'):
            ability_vec[ABILITY_IDS[action['ability']['id']]] = 1.0
        
        return torch.tensor(type_vec + pos_vec + ability_vec)
```

## Training Data Format

### Episode Structure
```python
@dataclass
class TrainingEpisode:
    """Complete game episode for training"""
    states: list[torch.Tensor]
    actions: list[torch.Tensor]
    rewards: list[float]
    metadata: dict
    
    @property
    def episode_length(self) -> int:
        return len(self.states)
    
    def to_training_batch(self, device: str = 'cuda') -> dict:
        """Convert episode to training-ready batch"""
        return {
            'states': torch.stack(self.states).to(device),
            'actions': torch.stack(self.actions).to(device),
            'rewards': torch.tensor(self.rewards).to(device),
            'mask': self._create_attention_mask().to(device)
        }
    
    def _create_attention_mask(self) -> torch.Tensor:
        """Creates attention mask for transformer architecture"""
        size = len(self.states)
        mask = torch.triu(torch.ones(size, size), diagonal=1)
        return mask.bool()
```

### Reward Structure
```python
class RewardCalculator:
    """Calculates immediate and delayed rewards for training"""
    
    def __init__(self, gamma: float = 0.99):
        self.gamma = gamma
        self.weights = {
            # Immediate rewards
            'damage_dealt': 0.5,
            'healing_done': 0.3,
            'position_improvement': 0.2,
            'status_effect_applied': 0.2,
            'resource_efficiency': 0.1,
            
            # Major events
            'character_defeated': -1.0,
            'victory': 5.0,
            'defeat': -3.0,
            
            # Strategic rewards
            'synergy_bonus': 0.3,
            'combo_execution': 0.4,
            'objective_progress': 0.6
        }
    
    def calculate_reward(self, state: dict, action: dict) -> float:
        """Calculate immediate reward for state-action pair"""
        reward = 0.0
        
        # Calculate immediate effects
        if action['type'] == 'ABILITY':
            reward += self._calculate_ability_reward(state, action)
        elif action['type'] == 'MOVE':
            reward += self._calculate_movement_reward(state, action)
        
        # Apply strategic bonuses
        reward += self._calculate_strategic_reward(state, action)
        
        return reward
    
    def calculate_returns(self, rewards: list[float]) -> list[float]:
        """Calculate discounted returns for episode"""
        returns = []
        running_return = 0.0
        
        for r in reversed(rewards):
            running_return = r + self.gamma * running_return
            returns.insert(0, running_return)
        
        return returns
```

## Data Processing Pipeline

### Replay Processing
```python
class ReplayProcessor:
    """Processes game replays into training episodes"""
    
    def __init__(self):
        self.state_vectorizer = StateVectorizer()
        self.reward_calculator = RewardCalculator()
    
    def process_replay(self, replay: dict) -> TrainingEpisode:
        """Convert a game replay into a training episode"""
        states = []
        actions = []
        rewards = []
        
        current_state = replay['initialState']
        for turn in replay['turns']:
            # Vectorize state and action
            state_vector = self.state_vectorizer.vectorize_state(current_state)
            action_vector = self.state_vectorizer.vectorize_action(turn['action'])
            
            # Calculate reward
            reward = self.reward_calculator.calculate_reward(
                current_state, turn['action']
            )
            
            states.append(state_vector)
            actions.append(action_vector)
            rewards.append(reward)
            
            # Update state
            current_state = turn['resultingState']
        
        # Calculate returns
        returns = self.reward_calculator.calculate_returns(rewards)
        
        return TrainingEpisode(
            states=states,
            actions=actions,
            rewards=returns,
            metadata={
                'gameId': replay['id'],
                'difficulty': replay['settings']['aiDifficulty'],
                'personality': replay['settings']['aiPersonality'],
                'outcome': replay['outcome']
            }
        )
```

### Training Data Validation
```python
class DataValidator:
    """Validates training data quality and consistency"""
    
    def validate_episode(self, episode: TrainingEpisode) -> bool:
        """Validate a training episode"""
        try:
            # Check data consistency
            if not (len(episode.states) == len(episode.actions) == len(episode.rewards)):
                return False
            
            # Validate tensor shapes
            state_shape = episode.states[0].shape
            action_shape = episode.actions[0].shape
            if not all(s.shape == state_shape for s in episode.states):
                return False
            if not all(a.shape == action_shape for a in episode.actions):
                return False
            
            # Validate reward range
            if not all(-10.0 <= r <= 10.0 for r in episode.rewards):
                return False
            
            return True
            
        except Exception as e:
            logger.error(f"Validation error: {str(e)}")
            return False
```

## Training Requirements

### Hardware Requirements
- Minimum RAM: 16GB
- GPU Memory: 8GB
- Storage: 100GB for dataset

### Performance Targets
- State vectorization: < 10ms
- Reward calculation: < 5ms
- Episode processing: < 100ms
- Training step: < 500ms per batch

### Data Volume Guidelines
- Minimum episodes per difficulty: 1000
- Minimum episodes per personality: 1000
- Validation split: 20%
- Test split: 10%