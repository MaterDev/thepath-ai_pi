# Style Guide

## Overview

This style guide ensures consistent code quality across The Path (AI-Pi) project:
- Code formatting
- Naming conventions
- Documentation standards
- Best practices

## General Guidelines

### 1. Code Organization

```
src/
├── server/         # Go server code
│   ├── game/       # Game logic
│   ├── ai/         # AI integration
│   └── net/        # Networking
├── client/         # TypeScript client
│   ├── core/       # Core logic
│   ├── ui/         # User interface
│   └── net/        # Networking
└── ai/             # Python AI system
    ├── models/     # AI models
    ├── training/   # Training system
    └── utils/      # Utilities
```

### 2. File Naming

```
# Go files
game_server.go
player_manager.go
ai_interface.go

# TypeScript files
GameClient.ts
StateManager.ts
UIController.ts

# Python files
ai_agent.py
model_trainer.py
data_processor.py
```

## Language-Specific Guidelines

### 1. Go Style

```go
// Package names
package gameserver

// Type names
type GameState struct {
    ID        string
    Players   map[string]*Player
    Round     int
    Status    GameStatus
}

// Interface names
type StateManager interface {
    Update() error
    GetState() State
    ValidateAction(Action) bool
}

// Function names
func ProcessAction(action Action) error {
    // Implementation
}

// Variable names
var (
    defaultTimeout = time.Second * 30
    maxPlayers    = 4
)

// Constants
const (
    StatusActive  GameStatus = "ACTIVE"
    StatusPaused  GameStatus = "PAUSED"
    StatusEnded   GameStatus = "ENDED"
)
```

### 2. TypeScript Style

```typescript
// Interfaces
interface GameState {
    readonly id: string;
    players: Map<string, Player>;
    round: number;
    status: GameStatus;
}

// Classes
class GameManager {
    private readonly state: GameState;
    private readonly updates: Queue<StateUpdate>;
    
    constructor(config: GameConfig) {
        this.state = new GameState(config);
        this.updates = new Queue();
    }
    
    public update(delta: number): void {
        this.processUpdates();
        this.state.update(delta);
    }
}

// Enums
enum GameStatus {
    Active = 'ACTIVE',
    Paused = 'PAUSED',
    Ended = 'ENDED'
}

// Constants
const DEFAULT_CONFIG: GameConfig = {
    updateRate: 60,
    maxPlayers: 4,
    timeout: 30000
};
```

### 3. Python Style

```python
# Class names
class AIAgent:
    """AI agent for game decision making."""
    
    def __init__(self, config: Dict[str, Any]) -> None:
        self.config = config
        self.model: Optional[Model] = None
    
    def process_state(self, 
                     state: GameState) -> List[Action]:
        """Process game state and return actions."""
        return self._get_actions(state)

# Function names
def calculate_reward(state: GameState,
                    action: Action) -> float:
    """Calculate reward for action in state."""
    return _compute_reward_value(state, action)

# Constants
MAX_BATCH_SIZE = 32
LEARNING_RATE = 0.001
DEFAULT_DIFFICULTY = 0.5

# Type aliases
StateVector = np.ndarray
ActionSpace = List[Action]
RewardSignal = float
```

## Documentation Standards

### 1. Code Comments

```python
class ModelTrainer:
    """Train AI models for game decision making.
    
    This class handles the training process for AI models,
    including data preparation, training loops, and evaluation.
    
    Attributes:
        model: Neural network model
        optimizer: Model optimizer
        batch_size: Training batch size
        
    Example:
        >>> trainer = ModelTrainer(model, optimizer)
        >>> trainer.train(dataset, epochs=10)
    """
    
    def train_step(self,
                  batch: TrainingBatch) -> float:
        """Perform single training step.
        
        Args:
            batch: Batch of training data
            
        Returns:
            Training loss for this step
            
        Raises:
            ValueError: If batch is invalid
        """
        if not self._validate_batch(batch):
            raise ValueError("Invalid batch")
        
        loss = self._compute_loss(batch)
        self._update_model(loss)
        
        return loss.item()
```

### 2. API Documentation

```typescript
/**
 * Game networking interface.
 * 
 * @remarks
 * This interface handles all network communication between
 * client and server components.
 * 
 * @example
 * ```typescript
 * const network = new NetworkManager(config);
 * await network.connect();
 * network.send(message);
 * ```
 */
interface NetworkManager {
    /**
     * Connect to game server.
     * 
     * @param config - Connection configuration
     * @returns Promise resolving when connected
     * @throws ConnectionError if connection fails
     */
    connect(config: ConnectionConfig): Promise<void>;
    
    /**
     * Send message to server.
     * 
     * @param message - Message to send
     * @returns Promise resolving when sent
     * @throws NetworkError if send fails
     */
    send(message: GameMessage): Promise<void>;
}
```

## Best Practices

### 1. Error Handling

```go
// Go error handling
func ProcessAction(action Action) error {
    if err := action.Validate(); err != nil {
        return fmt.Errorf("invalid action: %w", err)
    }
    
    if err := executeAction(action); err != nil {
        return fmt.Errorf("execute action: %w", err)
    }
    
    return nil
}

// Python error handling
def process_state(state: GameState) -> Action:
    """Process game state safely."""
    try:
        validated_state = validate_state(state)
        action = select_action(validated_state)
        return action
    except ValidationError as e:
        logger.error(f"State validation failed: {e}")
        raise
    except ActionError as e:
        logger.error(f"Action selection failed: {e}")
        raise
```

### 2. Testing Patterns

```python
# Unit test structure
class TestAIAgent(unittest.TestCase):
    """Test AI agent functionality."""
    
    def setUp(self):
        """Set up test environment."""
        self.agent = AIAgent(test_config)
    
    def test_action_selection(self):
        """Test action selection process."""
        # Arrange
        state = create_test_state()
        
        # Act
        action = self.agent.select_action(state)
        
        # Assert
        self.assertIsNotNone(action)
        self.assertTrue(self.is_valid_action(action))
```

## Related Documentation
- [Contributing Guide](contributing.md)
- [Testing Guide](../implementation/testing/overview.md)
- [Project Overview](../overview/project-scope.md)

## Version History
- v1.0: Initial style guide
- v1.1: Added language-specific guidelines
- v1.2: Enhanced documentation standards
