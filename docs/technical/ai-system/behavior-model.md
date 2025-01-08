# AI Behavior Model

## Overview

The AI behavior model combines strategic decision-making with personality-driven actions, running efficiently on the Raspberry Pi hardware. The system uses:
- Hierarchical decision making
- Personality-influenced choices
- Dynamic difficulty adjustment
- Hardware-optimized inference

## Core Components

### Decision Making System

```python
class AIAgent:
    def __init__(self, difficulty: float, personality: str):
        self.difficulty = difficulty
        self.personality = personality
        self.strategy = self._load_strategy()
        self.model = self._initialize_model()
        self.state_evaluator = StateEvaluator()
    
    def make_decision(self, game_state: dict) -> Action:
        """Core decision-making pipeline"""
        # Convert game state to model input
        state_vector = GameStateVector.from_battle_state(game_state)
        
        # Get valid actions and their base scores
        valid_actions = self._get_valid_actions(game_state)
        action_scores = self._evaluate_actions(valid_actions, game_state)
        
        # Apply personality and difficulty modifiers
        modified_scores = self._apply_personality(action_scores)
        final_scores = self._adjust_for_difficulty(modified_scores)
        
        return self._select_action(final_scores)
```

### State Evaluation

```python
class StateEvaluator:
    def evaluate_state(self, state: dict) -> float:
        """Evaluate current game state"""
        metrics = {
            'health_ratio': self._calculate_health_ratio(state),
            'position_score': self._evaluate_positions(state),
            'threat_level': self._assess_threats(state),
            'opportunity_score': self._identify_opportunities(state)
        }
        return self._combine_metrics(metrics)
    
    def _assess_threats(self, state: dict) -> float:
        """Calculate threat level from enemies"""
        threat_scores = []
        for enemy in state['enemies']:
            damage_potential = enemy['stats']['attack'] * \
                             max(a['power'] for a in enemy['abilities'])
            threat_scores.append(
                damage_potential * (enemy['stats']['health'] / 
                                  enemy['stats']['maxHealth'])
            )
        return sum(threat_scores)
```

## Personality System

```python
@dataclass
class PersonalityProfile:
    """Defines AI personality traits"""
    aggression: float     # 0-1: preference for offensive actions
    caution: float       # 0-1: preference for defensive actions
    creativity: float    # 0-1: randomness in decision making
    
    def modify_action_scores(self, 
                           actions: List[Action], 
                           scores: np.ndarray) -> np.ndarray:
        """Apply personality traits to action scores"""
        modified_scores = scores.copy()
        
        for i, action in enumerate(actions):
            if action.type == ActionType.ATTACK:
                modified_scores[i] *= (1 + self.aggression)
            elif action.type == ActionType.DEFEND:
                modified_scores[i] *= (1 + self.caution)
                
        # Add creativity-based noise
        noise = np.random.normal(0, self.creativity, len(scores))
        modified_scores += noise
        
        return modified_scores
```

## Implementation Guidelines

For AI-assisted development:

1. **State Processing**
   ```python
   def process_game_state(state: dict) -> np.ndarray:
       """Convert game state to model input"""
       # Extract relevant features
       features = []
       
       # Character stats
       for char in state['characters'].values():
           features.extend([
               char['stats']['health'] / char['stats']['maxHealth'],
               char['stats']['attack'] / 100.0,
               char['stats']['defense'] / 100.0,
               char['stats']['speed'] / 100.0
           ])
       
       # Global state
       features.extend([
           state['round'] / 20.0,
           len(state['characters']) / 4.0
       ])
       
       return np.array(features, dtype=np.float32)
   ```

2. **Action Selection**
   ```python
   def select_action(scores: np.ndarray, 
                    temperature: float = 1.0) -> int:
       """Select action using softmax with temperature"""
       # Apply temperature scaling
       scaled_scores = scores / temperature
       
       # Softmax probability distribution
       probs = np.exp(scaled_scores) / np.sum(np.exp(scaled_scores))
       
       # Sample action
       return np.random.choice(len(scores), p=probs)
   ```

3. **Error Handling**
   ```python
   def validate_action(action: Action, 
                      game_state: dict) -> bool:
       """Validate selected action"""
       try:
           # Check action requirements
           if not action.requirements_met(game_state):
               return False
           
           # Verify target validity
           if not action.validate_target(game_state):
               return False
           
           # Check resource costs
           if not action.can_afford(game_state):
               return False
           
           return True
       except Exception as e:
           logger.error(f"Action validation error: {e}")
           return False
   ```

## Hardware Optimization

1. **Memory Management**
   - Use float32 instead of float64
   - Batch process when possible
   - Minimize object creation
   - Use memory-mapped files

2. **Computation Optimization**
   - Vectorize operations
   - Use AI HAT+ acceleration
   - Minimize copying
   - Cache results

3. **Performance Monitoring**
   ```python
   @contextmanager
   def timing_context(name: str):
       """Context manager for timing operations"""
       start = time.perf_counter()
       yield
       duration = time.perf_counter() - start
       logger.debug(f"{name} took {duration*1000:.2f}ms")
   ```

## Related Documentation
- [Training Pipeline](training-pipeline.md)
- [Difficulty System](difficulty-system.md)
- [Hardware Configuration](../hardware/configuration.md)

## Version History
- v1.0: Initial behavior model
- v1.1: Added personality system
- v1.2: Hardware optimization
