# Replay System Schema

## Overview

Defines the data structures for recording, storing, and replaying game sessions. This system supports:
- Complete game state recording
- Action replay
- AI behavior analysis
- Training data generation

## Core Types

```go
type GameRecord struct {
    ID            string       `json:"id"`
    Timestamp     time.Time    `json:"timestamp"`
    Settings      GameSettings `json:"settings"`
    InitialState  BattleState  `json:"initialState"`
    Turns         []TurnRecord `json:"turns"`
    Outcome       GameOutcome  `json:"outcome"`
}

type TurnRecord struct {
    Round         int           `json:"round"`
    ActingPlayer  string        `json:"actingPlayer"`
    Action        BattleAction  `json:"action"`
    ResultState   BattleState   `json:"resultingState"`
    AIConfidence  float64       `json:"aiConfidence,omitempty"`
}

type GameSettings struct {
    AIDifficulty   float64  `json:"aiDifficulty"`
    AIPersonality  string   `json:"aiPersonality"`
    GameSpeed      int      `json:"gameSpeed"`
}
```

## Replay Manager

```go
type ReplayManager interface {
    // Recording methods
    StartRecording(gameId string) error
    RecordTurn(gameId string, turn TurnRecord) error
    EndRecording(gameId string, outcome GameOutcome) error
    
    // Playback methods
    GetReplay(gameId string) (*GameRecord, error)
    PlayReplay(gameId string, speed float64) chan BattleState
    
    // Analysis methods
    ExtractTrainingData(gameId string) ([]TrainingExample, error)
    AnalyzeAIPerformance(gameId string) (*AIAnalysis, error)
}
```

## Implementation Guidelines

For AI-assisted development:

1. **Recording Implementation**
   ```go
   func (rm *ReplayManager) RecordTurn(gameId string, turn TurnRecord) error {
       // Validate turn data
       if err := turn.Validate(); err != nil {
           return fmt.Errorf("invalid turn data: %w", err)
       }
       
       // Store turn data
       record, err := rm.store.GetRecord(gameId)
       if err != nil {
           return fmt.Errorf("failed to get record: %w", err)
       }
       
       record.Turns = append(record.Turns, turn)
       return rm.store.UpdateRecord(gameId, record)
   }
   ```

2. **Playback Implementation**
   ```go
   func (rm *ReplayManager) PlayReplay(gameId string, speed float64) chan BattleState {
       stateChan := make(chan BattleState)
       go func() {
           defer close(stateChan)
           
           record, err := rm.store.GetRecord(gameId)
           if err != nil {
               log.Printf("Failed to get record: %v", err)
               return
           }
           
           // Send initial state
           stateChan <- record.InitialState
           
           // Replay turns
           for _, turn := range record.Turns {
               time.Sleep(time.Duration(float64(time.Second) / speed))
               stateChan <- turn.ResultState
           }
       }()
       return stateChan
   }
   ```

3. **Data Validation**
   ```go
   func (t *TurnRecord) Validate() error {
       if t.Round < 0 {
           return errors.New("round cannot be negative")
       }
       if t.ActingPlayer == "" {
           return errors.New("acting player cannot be empty")
       }
       if err := t.Action.Validate(); err != nil {
           return fmt.Errorf("invalid action: %w", err)
       }
       if err := t.ResultState.Validate(); err != nil {
           return fmt.Errorf("invalid resulting state: %w", err)
       }
       return nil
   }
   ```

## Training Data Generation

```go
func ExtractTrainingData(record *GameRecord) []TrainingExample {
    examples := make([]TrainingExample, 0, len(record.Turns))
    
    for i, turn := range record.Turns {
        example := TrainingExample{
            State: GameStateVector.from_battle_state(turn.ResultState),
            Action: turn.Action.ToIndex(),
            Reward: calculateReward(turn),
        }
        
        if i < len(record.Turns)-1 {
            example.NextState = Some(GameStateVector.from_battle_state(
                record.Turns[i+1].ResultState))
            example.Done = false
        } else {
            example.NextState = None
            example.Done = true
        }
        
        examples = append(examples, example)
    }
    
    return examples
}
```

## Related Schemas
- [Game State Schema](game-state.md)
- [AI Models Schema](ai-models.md)

## Version History
- v1.0: Initial replay system
- v1.1: Added AI confidence tracking
- v1.2: Enhanced training data extraction
