# Game State Schemas

## Overview

This document defines the core data structures used in the battle system. These schemas are designed to be:
- Simple and focused on battles
- Language-agnostic (Go/Python)
- JSON-serializable
- WebSocket-friendly

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

## Battle State

```go
// Main battle state
type BattleState struct {
    ID          ID                      `json:"id"`
    Timestamp   Timestamp               `json:"timestamp"`
    Players     map[ID]*PlayerState     `json:"players"`
    TurnOrder   []ID                    `json:"turnOrder"`
    CurrentTurn ID                      `json:"currentTurn"`
    Round       int                     `json:"round"`
    Status      BattleStatus            `json:"status"`
}

type BattleStatus string

const (
    BattleStatusActive   BattleStatus = "ACTIVE"
    BattleStatusFinished BattleStatus = "FINISHED"
)

// Player state in battle
type PlayerState struct {
    ID       ID       `json:"id"`
    Name     string   `json:"name"`
    Health   int      `json:"health"`
    Energy   int      `json:"energy"`
    Status   []string `json:"status"`    // Active effects
    IsAI     bool     `json:"isAI"`
}

// Available actions
type Action struct {
    Type     ActionType `json:"type"`
    TargetID ID         `json:"targetId,omitempty"`
    Data     any        `json:"data,omitempty"`
}

const (
    ActionTypeAttack  ActionType = "ATTACK"
    ActionTypeDefend  ActionType = "DEFEND"
    ActionTypeSpecial ActionType = "SPECIAL"
)
```

## Battle Events

```go
// Event sent over WebSocket
type BattleEvent struct {
    Type      string          `json:"type"`
    BattleID  ID             `json:"battleId"`
    Timestamp Timestamp       `json:"timestamp"`
    Data      any            `json:"data"`
}

// Event types
const (
    EventTurnStart    = "TURN_START"
    EventActionTaken  = "ACTION_TAKEN"
    EventStatusUpdate = "STATUS_UPDATE"
    EventBattleEnd    = "BATTLE_END"
)

// Action result
type ActionResult struct {
    Success     bool   `json:"success"`
    Message     string `json:"message,omitempty"`
    Damage      int    `json:"damage,omitempty"`
    StatusAdded string `json:"statusAdded,omitempty"`
}
```

## Battle Configuration

```go
// Initial battle setup
type BattleConfig struct {
    PlayerID    ID      `json:"playerId"`
    Difficulty  float64 `json:"difficulty"`  // 0.2-0.95
    AIPersona   string  `json:"aiPersona,omitempty"`
}

// Battle result
type BattleResult struct {
    BattleID    ID      `json:"battleId"`
    Winner      ID      `json:"winner"`
    Duration    int     `json:"duration"`    // Rounds
    PlayerStats Stats   `json:"playerStats"`
    AIStats     Stats   `json:"aiStats"`
}

type Stats struct {
    DamageDealt   int `json:"damageDealt"`
    DamageTaken   int `json:"damageTaken"`
    ActionsUsed   int `json:"actionsUsed"`
    RoundsPlayed  int `json:"roundsPlayed"`
}
```

## Example Usage

```go
// Initialize battle
battle := &BattleState{
    ID:        NewID(),
    Timestamp: Now(),
    Players:   make(map[ID]*PlayerState),
    Status:    BattleStatusActive,
}

// Add player
battle.Players[playerID] = &PlayerState{
    ID:     playerID,
    Name:   "Player",
    Health: 100,
    Energy: 100,
}

// Add AI opponent
battle.Players[aiID] = &PlayerState{
    ID:     aiID,
    Name:   "AI Opponent",
    Health: 100,
    Energy: 100,
    IsAI:   true,
}

// Set turn order
battle.TurnOrder = []ID{playerID, aiID}
battle.CurrentTurn = playerID
```

## Related Schemas
- [AI Models Schema](ai-models.md)
- [Replay System Schema](replay-system.md)

## Version History
- v1.0: Initial schema definition
- v1.1: Added environment state
- v1.2: Enhanced status effects
- v2.0: Updated game state schema to focus on core battle mechanics
