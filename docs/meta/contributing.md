# Contributing Guide

## Overview

Welcome to The Path (AI-Pi) project! This guide will help you contribute effectively:
- Setting up your development environment
- Understanding the workflow
- Following coding standards
- Submitting changes

## Getting Started

### 1. Development Environment

```bash
# Clone repository
git clone https://github.com/MaterDev/thepath-ai_pi.git
cd thepath-ai_pi

# Install dependencies
# Server (Go)
go mod download

# Client (TypeScript)
npm install

# AI System (Python)
pip install -r requirements.txt
```

### 2. Hardware Setup

```bash
# Required hardware:
- Raspberry Pi 5 (8GB recommended)
- AI HAT+ module
- Active cooling solution

# Optional:
- 7-inch touchscreen
- GPIO accessories
```

## Development Workflow

### 1. Branching Strategy

```
main
  └── develop
       ├── feature/my-feature
       ├── bugfix/issue-123
       └── research/ai-optimization
```

Guidelines:
- Create feature branches from `develop`
- Use descriptive branch names
- Keep branches focused and small
- Update regularly from develop

### 2. Commit Messages

Follow conventional commits:
```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Code style changes
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Adding tests
- `chore`: Maintenance tasks

Example:
```
feat(ai): implement dynamic difficulty adjustment

- Add difficulty scaling based on player performance
- Implement performance metrics collection
- Add configuration options

Closes #123
```

## Code Standards

### 1. Go Guidelines

```go
// Package names
package gameserver

// Interface definitions
type GameState interface {
    Update() error
    GetState() State
    ValidateAction(Action) bool
}

// Error handling
func ProcessAction(action Action) error {
    if err := action.Validate(); err != nil {
        return fmt.Errorf("invalid action: %w", err)
    }
    return nil
}

// Comments and documentation
// PlayerManager handles player state and interactions
type PlayerManager struct {
    // Current active players
    players map[string]*Player
    
    // Synchronization
    mu sync.RWMutex
}
```

### 2. TypeScript Guidelines

```typescript
// Interfaces and types
interface GameState {
    readonly id: string;
    players: Map<string, Player>;
    status: GameStatus;
    
    update(delta: number): void;
    validate(): boolean;
}

// Class structure
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
```

### 3. Python Guidelines

```python
# Type hints
from typing import Dict, List, Optional

class AIAgent:
    def __init__(self, config: Dict[str, Any]) -> None:
        self.config = config
        self.model: Optional[Model] = None
    
    def process_state(self, 
                     state: GameState) -> List[Action]:
        """Process game state and return possible actions.
        
        Args:
            state: Current game state
            
        Returns:
            List of possible actions
            
        Raises:
            ValueError: If state is invalid
        """
        if not self.validate_state(state):
            raise ValueError("Invalid state")
        
        return self._get_actions(state)
```

## Testing Requirements

### 1. Unit Tests

```python
# Every feature needs unit tests
def test_ai_decision_making():
    """Test AI decision making process"""
    # Arrange
    ai = AIAgent(config={'difficulty': 0.5})
    state = create_test_state()
    
    # Act
    action = ai.get_action(state)
    
    # Assert
    assert action is not None
    assert is_valid_action(action, state)
```

### 2. Integration Tests

```python
# Integration tests for major features
async def test_game_flow():
    """Test complete game flow"""
    # Setup
    server = GameServer()
    client = GameClient()
    ai = AIAgent()
    
    # Connect
    await client.connect()
    
    # Play game
    while not game_complete:
        await process_turn()
    
    # Verify
    assert game_result.valid
```

## Documentation Standards

### 1. Code Documentation

```python
class AIModel:
    """AI model for game decision making.
    
    This class implements the core AI decision making process,
    including state evaluation, action selection, and learning.
    
    Attributes:
        difficulty: Float between 0 and 1 indicating AI difficulty
        personality: String indicating AI personality type
        model: Neural network model for decision making
    """
    
    def select_action(self, 
                     state: GameState,
                     valid_actions: List[Action]) -> Action:
        """Select best action from valid actions.
        
        Args:
            state: Current game state
            valid_actions: List of valid actions
            
        Returns:
            Selected action
            
        Raises:
            ValueError: If no valid actions available
        """
        pass
```

### 2. API Documentation

```typescript
/**
 * Game client API interface.
 * 
 * @remarks
 * This interface defines the core client-side API for game interactions.
 * 
 * @example
 * ```typescript
 * const client = new GameClient(config);
 * await client.connect();
 * const state = await client.getState();
 * ```
 */
interface GameClient {
    /**
     * Connect to game server.
     * 
     * @param config - Connection configuration
     * @returns Promise resolving when connected
     * @throws ConnectionError if connection fails
     */
    connect(config: ConnectionConfig): Promise<void>;
}

## Review Process

1. **Before Submitting**
   - Run all tests
   - Update documentation
   - Follow code standards
   - Add necessary tests

2. **Pull Request Template**
   ```markdown
   ## Description
   Brief description of changes
   
   ## Changes
   - Detailed list of changes
   - Technical implementation notes
   
   ## Testing
   - Test coverage details
   - Test results
   
   ## Documentation
   - Documentation updates
   - API changes
   ```

## Version History
- v1.0: Initial contributing guide
- v1.1: Added PR templates
- v1.2: Updated code review process
