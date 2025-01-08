# AI Model Schemas

## Overview

Defines the data structures used for AI model input, output, and training. These schemas ensure consistency between:
- Training data collection
- Model inference
- Performance evaluation

## Model Input

```python
@dataclass
class GameStateVector:
    """Vectorized game state for model input"""
    state_tensor: np.ndarray      # Shape: [1, STATE_FEATURES]
    valid_actions: np.ndarray     # Shape: [1, NUM_ACTIONS]
    character_mask: np.ndarray    # Shape: [1, MAX_CHARACTERS]

    @classmethod
    def from_battle_state(cls, state: dict) -> 'GameStateVector':
        """Convert BattleState to model input format"""
        return cls(
            state_tensor=vectorize_state(state),
            valid_actions=get_valid_actions_mask(state),
            character_mask=get_character_mask(state)
        )
```

## Training Data

```python
@dataclass
class TrainingExample:
    """Single training example for AI model"""
    state: GameStateVector
    action_taken: int
    reward: float
    next_state: Optional[GameStateVector]
    done: bool
    metadata: dict

@dataclass
class TrainingBatch:
    """Batch of examples for model training"""
    states: np.ndarray           # Shape: [BATCH_SIZE, STATE_FEATURES]
    actions: np.ndarray         # Shape: [BATCH_SIZE]
    rewards: np.ndarray         # Shape: [BATCH_SIZE]
    next_states: np.ndarray     # Shape: [BATCH_SIZE, STATE_FEATURES]
    dones: np.ndarray          # Shape: [BATCH_SIZE]
```

## Model Configuration

```python
@dataclass
class ModelConfig:
    """AI model configuration"""
    architecture: str           # Model architecture type
    hidden_sizes: List[int]    # Hidden layer dimensions
    activation: str            # Activation function
    learning_rate: float       # Training learning rate
    batch_size: int           # Training batch size
    buffer_size: int          # Replay buffer size
    
    def to_dict(self) -> dict:
        """Convert to JSON-serializable format"""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: dict) -> 'ModelConfig':
        """Create from JSON-serializable format"""
        return cls(**data)
```

## Implementation Guidelines

For AI-assisted development:

1. **Data Processing**
   ```python
   def vectorize_state(state: dict) -> np.ndarray:
       """Convert game state to model input vector"""
       features = []
       # Character features
       for char in state['characters'].values():
           features.extend([
               char['stats']['health'] / char['stats']['maxHealth'],
               char['stats']['attack'] / 100.0,
               char['stats']['defense'] / 100.0,
               char['stats']['speed'] / 100.0
           ])
       # Global features
       features.extend([
           state['round'] / 20.0,  # Normalized round number
           len(state['characters']) / 4.0  # Normalized character count
       ])
       return np.array(features, dtype=np.float32)
   ```

2. **Validation**
   ```python
   def validate_training_data(batch: TrainingBatch) -> bool:
       """Validate training batch data"""
       try:
           assert batch.states.shape[0] == batch.actions.shape[0]
           assert batch.states.shape[0] == batch.rewards.shape[0]
           assert batch.states.shape[0] == batch.next_states.shape[0]
           assert batch.states.shape[0] == batch.dones.shape[0]
           assert batch.states.shape[0] > 0
           return True
       except AssertionError:
           return False
   ```

3. **Error Handling**
   - Validate input shapes
   - Check value ranges
   - Handle missing data
   - Log validation errors

## Related Schemas
- [Game State Schema](game-state.md)
- [Replay System Schema](replay-system.md)

## Version History
- v1.0: Initial model schemas
- v1.1: Added batch processing
- v1.2: Enhanced validation
