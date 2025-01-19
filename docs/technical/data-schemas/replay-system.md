# Battle Replay System

## Overview

A simple system for recording battle events for training data collection and basic replay functionality.

## Core Types

```go
// Base types
type ID string          // Unique identifier
type Timestamp int64    // Unix milliseconds
type ActionType string  // Type of action

// Common interfaces
type Serializable interface {
    Marshal() ([]byte, error)
    Unmarshal([]byte) error
}
```

## Battle Recording

```go
// Main replay record
type BattleRecord struct {
    ID          ID              `json:"id"`
    StartTime   Timestamp       `json:"startTime"`
    EndTime     Timestamp       `json:"endTime"`
    Events      []BattleEvent   `json:"events"`
    Config      BattleConfig    `json:"config"`
    Result      BattleResult    `json:"result"`
}

// Single battle event
type BattleEvent struct {
    Type      string    `json:"type"`
    Timestamp Timestamp `json:"timestamp"`
    Data      any       `json:"data"`
}

// Event types
const (
    EventBattleStart   = "BATTLE_START"
    EventTurnStart     = "TURN_START"
    EventActionTaken   = "ACTION_TAKEN"
    EventStateUpdate   = "STATE_UPDATE"
    EventBattleEnd     = "BATTLE_END"
)

// Event data structures
type ActionEvent struct {
    ActorID    ID         `json:"actorId"`
    Action     Action     `json:"action"`
    Result     ActionResult `json:"result"`
}

type StateEvent struct {
    State      BattleState `json:"state"`
    Delta      StateDelta  `json:"delta,omitempty"`
}

type StateDelta struct {
    HealthChanges map[ID]int    `json:"healthChanges,omitempty"`
    StatusChanges map[ID][]string `json:"statusChanges,omitempty"`
}
```

## Recording System

```go
// Battle recorder
type BattleRecorder struct {
    currentBattle *BattleRecord
    events        []BattleEvent
}

func NewBattleRecorder(config BattleConfig) *BattleRecorder {
    return &BattleRecorder{
        currentBattle: &BattleRecord{
            ID:        NewID(),
            StartTime: Now(),
            Config:    config,
            Events:    make([]BattleEvent, 0),
        },
    }
}

func (r *BattleRecorder) RecordEvent(eventType string, data any) {
    event := BattleEvent{
        Type:      eventType,
        Timestamp: Now(),
        Data:      data,
    }
    r.events = append(r.events, event)
}

func (r *BattleRecorder) FinishRecording(result BattleResult) *BattleRecord {
    r.currentBattle.EndTime = Now()
    r.currentBattle.Events = r.events
    r.currentBattle.Result = result
    return r.currentBattle
}
```

## Replay System

```go
// Battle replay player
type BattlePlayer struct {
    record    *BattleRecord
    position  int
    state     *BattleState
}

func NewBattlePlayer(record *BattleRecord) *BattlePlayer {
    return &BattlePlayer{
        record:   record,
        position: 0,
        state:    nil,
    }
}

func (p *BattlePlayer) NextEvent() *BattleEvent {
    if p.position >= len(p.record.Events) {
        return nil
    }
    event := p.record.Events[p.position]
    p.position++
    return &event
}

func (p *BattlePlayer) PrevEvent() *BattleEvent {
    if p.position <= 0 {
        return nil
    }
    p.position--
    return &p.record.Events[p.position]
}

func (p *BattlePlayer) JumpToTime(timestamp Timestamp) {
    // Find closest event
    for i, event := range p.record.Events {
        if event.Timestamp >= timestamp {
            p.position = i
            break
        }
    }
}
```

## Storage

```go
// Simple file-based storage
type ReplayStorage struct {
    basePath string
}

func (s *ReplayStorage) SaveReplay(record *BattleRecord) error {
    data, err := json.Marshal(record)
    if err != nil {
        return err
    }
    
    filename := fmt.Sprintf("%s/%s.json", s.basePath, record.ID)
    return os.WriteFile(filename, data, 0644)
}

func (s *ReplayStorage) LoadReplay(id ID) (*BattleRecord, error) {
    filename := fmt.Sprintf("%s/%s.json", s.basePath, id)
    data, err := os.ReadFile(filename)
    if err != nil {
        return nil, err
    }
    
    var record BattleRecord
    if err := json.Unmarshal(data, &record); err != nil {
        return nil, err
    }
    return &record, nil
}
```

## Version History
- v1.0: Initial replay system
- v1.1: Added event recording
- v1.2: Enhanced playback
- v2.0: Simplified for basic battle recording
