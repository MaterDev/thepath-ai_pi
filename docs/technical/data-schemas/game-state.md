---
title: Game State Schema
description: Technical specification of the game state data model, including validation rules and serialization formats
---

# Game State Schemas

## Overview

This document defines the core data structures used in the battle system. These schemas are designed to be:

- Simple and focused on battles
- Language-agnostic (Go/Python)
- JSON-serializable
- WebSocket-friendly

!!! info "Related Documentation"
    For detailed information about game mechanics, refer to:
    - [Status Effects](/technical/game-mechanics/status-effects)
    - [Attack Types](/technical/game-mechanics/attack-types)
    - [Battle Conditions](/technical/game-mechanics/battle-conditions)
    - [Targeting System](/technical/game-mechanics/targeting)

## Core Types

```go
// Base types
type ID string          // Unique identifier
type Timestamp int64    // Unix milliseconds

// Common interfaces
type Serializable interface {
    Marshal() ([]byte, error)
    Unmarshal([]byte) error
}

// Attack type enums (see attack-types.md for details)
type AttackType string

const (
    // Physical
    AttackTypeSlash     AttackType = "SLASH"
    AttackTypePierce    AttackType = "PIERCE"
    AttackTypeBlunt     AttackType = "BLUNT"
    AttackTypeRend      AttackType = "REND"
    AttackTypeConstrict AttackType = "CONSTRICT"
    AttackTypeImpact    AttackType = "IMPACT"
    AttackTypeCrush     AttackType = "CRUSH"

    // Spiritual
    AttackTypeRoot      AttackType = "ROOT"
    AttackTypeSpirit    AttackType = "SPIRIT"
    AttackTypePsychic   AttackType = "PSYCHIC"
    AttackTypeCrystal   AttackType = "CRYSTAL"
    AttackTypeBlood     AttackType = "BLOOD"
    AttackTypeBone      AttackType = "BONE"
    AttackTypeBody      AttackType = "BODY"

    // Elemental
    AttackTypeFire      AttackType = "FIRE"
    AttackTypeWater     AttackType = "WATER"
    AttackTypeAir       AttackType = "AIR"
    AttackTypeEarth     AttackType = "EARTH"
    AttackTypeLightning AttackType = "LIGHTNING"
    AttackTypePoison    AttackType = "POISON"
    AttackTypeFrost     AttackType = "FROST"
)

// Status effect types (see status-effects.md for details)
type StatusEffectType string

const (
    // Damage Effects
    StatusEffectDamage      StatusEffectType = "DAMAGE"
    StatusEffectDrain       StatusEffectType = "DRAIN"
    StatusEffectBurn        StatusEffectType = "BURN"
    StatusEffectBleed       StatusEffectType = "BLEED"
    StatusEffectTrueDamage  StatusEffectType = "TRUE_DAMAGE"
    StatusEffectCounter     StatusEffectType = "COUNTER"
    StatusEffectShatter     StatusEffectType = "SHATTER"

    // Defensive Effects
    StatusEffectShield      StatusEffectType = "SHIELD"
    StatusEffectBarrier     StatusEffectType = "BARRIER"
    StatusEffectReflect     StatusEffectType = "REFLECT"
    StatusEffectImmune      StatusEffectType = "IMMUNE"
    StatusEffectGuard       StatusEffectType = "GUARD"
    StatusEffectAbsorb      StatusEffectType = "ABSORB"
    StatusEffectEvasion     StatusEffectType = "EVASION"

    // Recovery Effects
    StatusEffectHeal        StatusEffectType = "HEAL"
    StatusEffectRegenerate  StatusEffectType = "REGENERATE"
    StatusEffectCleanse     StatusEffectType = "CLEANSE"
    StatusEffectRevive      StatusEffectType = "REVIVE"
    StatusEffectLifesteal   StatusEffectType = "LIFESTEAL"
    StatusEffectRestore     StatusEffectType = "RESTORE"
    StatusEffectPurify      StatusEffectType = "PURIFY"

    // Debuffs
    StatusEffectWeaken      StatusEffectType = "WEAKEN"
    StatusEffectVulnerable  StatusEffectType = "VULNERABLE"
    StatusEffectSilence     StatusEffectType = "SILENCE"
    StatusEffectStun        StatusEffectType = "STUN"
    StatusEffectRoot        StatusEffectType = "ROOT"
    StatusEffectSlow        StatusEffectType = "SLOW"
    StatusEffectBlind       StatusEffectType = "BLIND"

    // Buffs
    StatusEffectStrengthen  StatusEffectType = "STRENGTHEN"
    StatusEffectHaste       StatusEffectType = "HASTE"
    StatusEffectEmpower     StatusEffectType = "EMPOWER"
    StatusEffectFortify     StatusEffectType = "FORTIFY"
    StatusEffectPrecision   StatusEffectType = "PRECISION"
    StatusEffectEnergize    StatusEffectType = "ENERGIZE"
    StatusEffectInspire     StatusEffectType = "INSPIRE"

    // Control Effects
    StatusEffectCharm       StatusEffectType = "CHARM"
    StatusEffectFear        StatusEffectType = "FEAR"
    StatusEffectTaunt       StatusEffectType = "TAUNT"
    StatusEffectConfuse     StatusEffectType = "CONFUSE"
    StatusEffectSleep       StatusEffectType = "SLEEP"
    StatusEffectParalyze    StatusEffectType = "PARALYZE"
    StatusEffectBanish      StatusEffectType = "BANISH"

    // Utility Effects
    StatusEffectMark        StatusEffectType = "MARK"
    StatusEffectLink        StatusEffectType = "LINK"
    StatusEffectCopy        StatusEffectType = "COPY"
    StatusEffectTransform   StatusEffectType = "TRANSFORM"
    StatusEffectStance      StatusEffectType = "STANCE"
    StatusEffectChannel     StatusEffectType = "CHANNEL"
    StatusEffectLock        StatusEffectType = "LOCK"
)
```

## Battle State

```go
// Main battle state
type BattleState struct {
    ID          ID                      `json:"id"`
    Timestamp   Timestamp               `json:"timestamp"`
    Players     map[ID]*PlayerState     `json:"players"`
    Field       *FieldState             `json:"field"`      // Current field conditions
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
    ID            ID                           `json:"id"`
    Name          string                       `json:"name"`
    Health        int                          `json:"health"`
    Energy        int                          `json:"energy"`
    StatusEffects map[StatusEffectType]*Effect `json:"statusEffects"`
    Class         string                       `json:"class"`
    IsAI         bool                         `json:"isAI"`
}

// Status effect instance
type Effect struct {
    Type      StatusEffectType `json:"type"`
    Value     float64          `json:"value"`    // Magnitude of the effect
    Duration  int             `json:"duration"`  // Rounds remaining
    Source    ID              `json:"source"`    // Who applied the effect
}

// Field conditions state
type FieldState struct {
    Conditions []FieldCondition `json:"conditions"`
    Duration   map[string]int  `json:"duration"`    // Rounds remaining per condition
}

type FieldCondition struct {
    Name        string    `json:"name"`
    Source      string    `json:"source"`   // Class or attack type that created it
    Modifiers   []Modifier `json:"modifiers"`
}

type Modifier struct {
    Type      string  `json:"type"`    // What is being modified
    Value     float64 `json:"value"`   // Modification amount
    Condition string  `json:"condition"` // When this applies
} ActionData `json:"data"`
}

type ActionData struct {
    Power        int              `json:"power"`        // Base power
    Effects      []StatusEffect   `json:"effects"`      // Status effects to apply
    Requirements Requirements     `json:"requirements"` // Costs and conditions
}

type StatusEffect struct {
    Type     StatusEffectType `json:"type"`
    Value    float64         `json:"value"`    // Magnitude
    Duration int            `json:"duration"`  // How many rounds
}

type Requirements struct {
    EnergyCost    int      `json:"energyCost"`
    HealthCost    int      `json:"healthCost"`
    Conditions    []string `json:"conditions"` // Required field conditions
    StatusEffects []string `json:"status"`     // Required status effects
}

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
    // Turn Management
    EventTurnStart    = "TURN_START"
    EventTurnEnd      = "TURN_END"
    EventRoundStart   = "ROUND_START"
    EventRoundEnd     = "ROUND_END"
    
    // Actions and Effects
    EventActionTaken  = "ACTION_TAKEN"
    EventEffectApplied = "EFFECT_APPLIED"
    EventEffectExpired = "EFFECT_EXPIRED"
    
    // Field Conditions
    EventFieldChanged = "FIELD_CHANGED"
    EventFieldExpired = "FIELD_EXPIRED"
    
    // Battle Flow
    EventStatusUpdate = "STATUS_UPDATE"
    EventBattleEnd    = "BATTLE_END"
)

// Action result with detailed effect information
type ActionResult struct {
    Success     bool                  `json:"success"`
    Message     string                `json:"message,omitempty"`
    Damage      DamageResult         `json:"damage,omitempty"`
    Effects     []EffectResult       `json:"effects,omitempty"`
    FieldEffects []FieldCondition    `json:"fieldEffects,omitempty"`
}

type DamageResult struct {
    Amount    int        `json:"amount"`
    Type      AttackType `json:"type"`
    Modifiers []Modifier `json:"modifiers"` // What modified the damage
}

type EffectResult struct {
    Type      StatusEffectType `json:"type"`
    Success   bool            `json:"success"`
    Duration  int            `json:"duration"`
    Value     float64        `json:"value"`
    Resisted  bool           `json:"resisted"` // If target was immune/resistant
}
```

## Battle Configuration

```go
// Initial battle setup
type BattleConfig struct {
    PlayerID     ID      `json:"playerId"`
    PlayerClass  string  `json:"playerClass"`  // Character class
    Difficulty   float64 `json:"difficulty"`   // 0.2-0.95
    AIPersona    string  `json:"aiPersona,omitempty"`
    InitialField []FieldCondition `json:"initialField,omitempty"`
}

// Battle result with detailed statistics
type BattleResult struct {
    BattleID    ID      `json:"battleId"`
    Winner      ID      `json:"winner"`
    Duration    int     `json:"duration"`    // Rounds
    PlayerStats Stats   `json:"playerStats"`
    AIStats     Stats   `json:"aiStats"`
    FieldStats  FieldStats `json:"fieldStats"`
}

type Stats struct {
    // Damage Stats
    DamageDealt     map[AttackType]int `json:"damageDealt"`    // By attack type
    DamageTaken     map[AttackType]int `json:"damageTaken"`    // By attack type
    EffectsApplied  map[StatusEffectType]int `json:"effectsApplied"`
    EffectsReceived map[StatusEffectType]int `json:"effectsReceived"`
    
    // Resource Stats
    EnergyUsed    int `json:"energyUsed"`
    HealthLost    int `json:"healthLost"`
    EnergyGained  int `json:"energyGained"`
    HealthGained  int `json:"healthGained"`
    
    // Battle Stats
    ActionsUsed   int `json:"actionsUsed"`
    RoundsPlayed  int `json:"roundsPlayed"`
}

type FieldStats struct {
    ConditionsTriggered map[string]int `json:"conditionsTriggered"`
    TotalDuration       int           `json:"totalDuration"`
    MaxConditions       int           `json:"maxConditions"`
}
```

## Example Usage

```go
// Initialize battle with field conditions
battle := &BattleState{
    ID:        NewID(),
    Timestamp: Now(),
    Players:   make(map[ID]*PlayerState),
    Field:     &FieldState{
        Conditions: []FieldCondition{},
        Duration:   make(map[string]int),
    },
    Status:    BattleStatusActive,
}

// Add player with status effects tracking
battle.Players[playerID] = &PlayerState{
    ID:            playerID,
    Name:          "Player",
    Health:        100,
    Energy:        100,
    Class:         "Crystal Vanguard",
    StatusEffects: make(map[StatusEffectType]*Effect),
}

// Add AI opponent
battle.Players[aiID] = &PlayerState{
    ID:            aiID,
    Name:          "AI Opponent",
    Health:        100,
    Energy:        100,
    Class:         "Wraithwood Seer",
    StatusEffects: make(map[StatusEffectType]*Effect),
    IsAI:          true,
}

// Set turn order and initial field condition
battle.TurnOrder = []ID{playerID, aiID}
battle.CurrentTurn = playerID

// Apply class-based field effect
battle.Field.Conditions = append(battle.Field.Conditions, FieldCondition{
    Name:   "Crystal Field",
    Source: "Crystal Vanguard",
    Modifiers: []Modifier{
        {Type: "CRYSTAL_DAMAGE", Value: 1.2},
        {Type: "PHYSICAL_DAMAGE", Value: 0.8},
    },
})
battle.Field.Duration["Crystal Field"] = 3 // Lasts 3 rounds
