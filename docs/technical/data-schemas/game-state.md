# Game State Schemas

## Overview

This document defines the core data structures used throughout the game system. These schemas are designed to be:
- Language-agnostic (implemented in both Go and Python)
- Serializable (JSON-compatible)
- Validated (with clear rules)
- Versioned (for future evolution)

## Core Types

```go
// Base types used throughout the system
type ID string          // Unique identifier
type Timestamp int64    // Unix milliseconds
type Version string     // Semantic version

// Common interfaces that all major types implement
type Serializable interface {
    Marshal() ([]byte, error)
    Unmarshal([]byte) error
}

type Validatable interface {
    Validate() error
}
```

## Battle State

The core game state during combat:

```go
type BattleState struct {
    ID              ID                      `json:"id"`
    Version         Version                 `json:"version"`
    Timestamp       Timestamp               `json:"timestamp"`
    Characters      map[ID]*CharacterState  `json:"characters"`
    TurnOrder       []ID                    `json:"turnOrder"`
    CurrentTurn     int                     `json:"currentTurn"`
    Round           int                     `json:"round"`
    Status          BattleStatus            `json:"status"`
    Environment     *EnvironmentState       `json:"environment,omitempty"`
}

type BattleStatus string

const (
    BattleStatusActive   BattleStatus = "ACTIVE"
    BattleStatusPaused   BattleStatus = "PAUSED"
    BattleStatusComplete BattleStatus = "COMPLETE"
)
```

## Character State

Individual character status and capabilities:

```go
type CharacterState struct {
    ID          ID              `json:"id"`
    Name        string          `json:"name"`
    Stats       Stats           `json:"stats"`
    Status      []StatusEffect  `json:"status"`
    Position    Position        `json:"position"`
    Actions     []Action        `json:"actions"`
    Cooldowns   map[ID]int      `json:"cooldowns"`
}

type Stats struct {
    Health      int     `json:"health"`
    MaxHealth   int     `json:"maxHealth"`
    Attack      int     `json:"attack"`
    Defense     int     `json:"defense"`
    Speed       int     `json:"speed"`
    Initiative  float64 `json:"initiative"`
}
```

## Implementation Guidelines

For AI-assisted development:

1. **Type Safety**
   - Always use defined types
   - Implement proper validation
   - Handle all error cases
   - Check for nil pointers

2. **Serialization**
   - Use standard JSON tags
   - Handle optional fields
   - Version all schemas
   - Validate after deserialize

3. **State Management**
   - Deep copy when needed
   - Validate state transitions
   - Track modifications
   - Maintain immutability

4. **Error Handling**
   ```go
   // Example validation implementation
   func (s *BattleState) Validate() error {
       if s.ID == "" {
           return errors.New("battle state must have an ID")
       }
       if len(s.Characters) == 0 {
           return errors.New("battle must have at least one character")
       }
       // ... additional validation
       return nil
   }
   ```

## Related Schemas
- [AI Models Schema](ai-models.md)
- [Replay System Schema](replay-system.md)

## Version History
- v1.0: Initial schema definition
- v1.1: Added environment state
- v1.2: Enhanced status effects
