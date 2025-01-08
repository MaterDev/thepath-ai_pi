# The Path (AI-Pi) MVP Final Scope
## 4-Week Development Plan

## Project Overview
The Path (AI-Pi) is a containerized turn-based combat game with configurable AI opponents powered by the Raspberry Pi AI HAT+. The system includes comprehensive game replay capabilities and cloud-based analytics for game data collection and future AI improvement.

## Additional Key Features

### AI Difficulty System
```python
class AIDifficulty:
    BEGINNER = 0.4    # More random actions, basic strategy
    NORMAL = 0.7      # Balanced decision making
    HARD = 0.85       # Optimal strategy focus
    EXPERT = 1.0      # Maximum performance

class AIAgent:
    def __init__(self, difficulty: float):
        self.difficulty = difficulty
        self.strategy_weights = self._adjust_weights(difficulty)
        self.randomness_factor = self._calculate_randomness(difficulty)
```

### Replay System

#### Game State Recording
```go
type GameRecord struct {
    ID        string       `json:"id"`
    Timestamp time.Time    `json:"timestamp"`
    Settings  GameSettings `json:"settings"`
    InitialState BattleState `json:"initialState"`
    Turns     []TurnRecord `json:"turns"`
    Outcome   GameOutcome  `json:"outcome"`
}

type TurnRecord struct {
    Round       int           `json:"round"`
    ActingPlayer string       `json:"actingPlayer"`
    Action      BattleAction  `json:"action"`
    ResultingState BattleState `json:"resultingState"`
    AIConfidence float64      `json:"aiConfidence,omitempty"`
}

type GameSettings struct {
    AIDifficulty float64      `json:"aiDifficulty"`
    AIPersonality string      `json:"aiPersonality"`
    GameSpeed    int          `json:"gameSpeed"`
}
```

#### Database Schema Updates
```javascript
// Replay Collection
{
  gameId: ObjectId,
  timestamp: Date,
  settings: {
    aiDifficulty: Number,
    aiPersonality: String,
    gameSpeed: Number
  },
  initialState: {
    characters: [],
    battleState: Object
  },
  turns: [{
    round: Number,
    actingPlayer: String,
    action: {
      type: String,
      targetId: String,
      ability: Object
    },
    resultingState: Object,
    aiConfidence: Number
  }],
  outcome: {
    winner: String,
    finalState: Object,
    statistics: Object
  },
  performance: {
    aiResponseTimes: [Number],
    hardwareMetrics: Object
  }
}
```

## Updated Week-by-Week Plan

### Week 1: Core Game & AI Server
#### Days 1-3: Core Game
- Battle system implementation
- State serialization
- Replay recording system
- Game settings management

#### Days 4-7: AI Server
- Difficulty-aware AI model
- Strategy weight system
- Confidence scoring
- Performance optimization

### Week 2: Cloud Integration & Analytics
#### Days 8-10: Cloud Setup
- MongoDB Atlas setup
- Replay storage system
- Analytics pipeline
- Performance tracking

#### Days 11-14: Replay System
- State recording
- Replay playback
- Turn visualization
- Analytics integration

### Week 3: Containerization & Deployment
#### Days 15-17: Docker
- Game server container
- AI server container
- Data persistence
- State management

#### Days 18-21: Deployment
- Installation system
- Configuration management
- Update mechanism
- Performance monitoring

### Week 4: Testing & Release
#### Days 22-24: Testing
- Replay verification
- AI difficulty testing
- Performance benchmarking
- State consistency

#### Days 25-28: Release
- Documentation
- Installation guide
- Configuration guide
- Community setup

## Technical Implementation

### AI Difficulty Management
```python
class AIStrategy:
    def __init__(self, difficulty: float):
        self.base_weights = {
            'aggression': 0.5,
            'defense': 0.5,
            'ability_usage': 0.5,
            'target_selection': 0.5
        }
        self.difficulty = difficulty
        self.weights = self._adjust_weights()
    
    def _adjust_weights(self):
        # Adjust strategy weights based on difficulty
        adjusted = {}
        for key, base in self.base_weights.items():
            # Higher difficulty means more optimal weights
            optimal = self._get_optimal_weight(key)
            adjusted[key] = base + (optimal - base) * self.difficulty
        return adjusted

    def get_action_confidence(self, state, action):
        # Calculate confidence score for action
        # Used for replay analysis and difficulty verification
        pass
```

### Replay Management
```go
type ReplayManager struct {
    db          *mongo.Database
    cache       *lru.Cache
    currentGame *GameRecord
}

func (rm *ReplayManager) RecordTurn(turn TurnRecord) error {
    // Record turn to current game
    rm.currentGame.Turns = append(rm.currentGame.Turns, turn)
    
    // Periodic state snapshot for long games
    if len(rm.currentGame.Turns) % 10 == 0 {
        return rm.SaveSnapshot()
    }
    return nil
}

func (rm *ReplayManager) PlayReplay(gameId string, speed float64) chan BattleState {
    stateChan := make(chan BattleState)
    go rm.streamReplay(gameId, speed, stateChan)
    return stateChan
}
```

### API Endpoints
```
# Game Management
POST   /api/games/new
GET    /api/games/{id}
POST   /api/games/{id}/action
GET    /api/games/{id}/state

# Replay System
GET    /api/replays/{id}
GET    /api/replays/{id}/stream
GET    /api/replays/list
POST   /api/replays/{id}/analyze

# AI Configuration
POST   /api/ai/configure
GET    /api/ai/difficulties
GET    /api/ai/statistics
```

## User Interface Updates

### Difficulty Selection
```typescript
interface DifficultySettings {
    level: number;           // 0.0 to 1.0
    description: string;     // User-friendly description
    expectedWinRate: number; // Estimated player win rate
}

interface GameConfiguration {
    difficulty: DifficultySettings;
    aiPersonality: string;
    gameSpeed: number;
}
```

### Replay Interface
```typescript
interface ReplayControls {
    play: () => void;
    pause: () => void;
    stepForward: () => void;
    stepBack: () => void;
    setSpeed: (speed: number) => void;
    jumpToTurn: (turn: number) => void;
}
```

## Analytics Enhancements

### Performance Metrics
```javascript
{
    gameId: ObjectId,
    difficulty: Number,
    aiMetrics: {
        averageConfidence: Number,
        strategyAdherence: Number,
        responseTime: {
            average: Number,
            max: Number,
            min: Number
        }
    },
    playerMetrics: {
        averageTurnTime: Number,
        strategyPattern: String,
        abilityUsage: Object
    }
}
```

## Success Criteria Updates

### AI Performance
- Response time < 500ms across all difficulties
- Consistent strategy application based on difficulty
- Meaningful difficulty progression
- Strategy confidence tracking

### Replay System
- Complete state reconstruction
- Accurate playback at variable speeds
- Efficient storage and retrieval
- Analytics integration

### User Experience
- Intuitive difficulty selection
- Visible AI confidence indicators
- Smooth replay controls
- Clear performance feedback

## Future Enhancements

### AI Improvements
- Learning from replays
- Dynamic difficulty adjustment
- Strategy adaptation
- Personality profiles

### Replay Features
- Commentary generation
- Strategy analysis
- Learning recommendations
- Community sharing

### Analytics
- Strategy effectiveness by difficulty
- Player improvement tracking
- AI performance optimization
- Community statistics