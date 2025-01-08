# Data Schema Definition

## Core Types
```go
// Base types used throughout the system
type ID string
type Timestamp int64
type Version string

// Common interfaces
type Serializable interface {
    Marshal() ([]byte, error)
    Unmarshal([]byte) error
}

type Validatable interface {
    Validate() error
}
```

## Game State Schema

### Battle State
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

### Character State
```go
type CharacterState struct {
    ID          ID              `json:"id"`
    Name        string          `json:"name"`
    Stats       Stats           `json:"stats"`
    Position    Position        `json:"position"`
    Status      []StatusEffect  `json:"status"`
    Abilities   []Ability       `json:"abilities"`
    Resources   Resources       `json:"resources"`
    Team        TeamID          `json:"team"`
}

type Stats struct {
    Health      int     `json:"health"`
    MaxHealth   int     `json:"maxHealth"`
    Attack      int     `json:"attack"`
    Defense     int     `json:"defense"`
    Speed       int     `json:"speed"`
    Initiative  float64 `json:"initiative"`
}

type Position struct {
    X           int     `json:"x"`
    Y           int     `json:"y"`
    Facing      int     `json:"facing"` // Degrees 0-359
}

type Resources struct {
    Energy      int     `json:"energy"`
    MaxEnergy   int     `json:"maxEnergy"`
    Shields     int     `json:"shields,omitempty"`
    Focus       int     `json:"focus,omitempty"`
}
```

### Action Schema
```go
type Action struct {
    ID          ID          `json:"id"`
    Type        ActionType  `json:"type"`
    Source      ID          `json:"source"`
    Target      ID          `json:"target"`
    Ability     *Ability    `json:"ability,omitempty"`
    Movement    *Movement   `json:"movement,omitempty"`
    Timestamp   Timestamp   `json:"timestamp"`
}

type ActionType string

const (
    ActionTypeAbility  ActionType = "ABILITY"
    ActionTypeMove     ActionType = "MOVE"
    ActionTypeWait     ActionType = "WAIT"
    ActionTypeDefend   ActionType = "DEFEND"
)

type Ability struct {
    ID          ID              `json:"id"`
    Name        string          `json:"name"`
    Type        AbilityType     `json:"type"`
    Power       int             `json:"power"`
    Cost        Cost            `json:"cost"`
    Range       Range           `json:"range"`
    Effects     []Effect        `json:"effects"`
    Cooldown    int             `json:"cooldown"`
}

type Movement struct {
    Path        []Position  `json:"path"`
    Speed       float64     `json:"speed"`
    Animation   string      `json:"animation"`
}
```

### Effect Schema
```go
type Effect struct {
    ID          ID          `json:"id"`
    Type        EffectType  `json:"type"`
    Value       float64     `json:"value"`
    Duration    int         `json:"duration"`
    Target      EffectTarget `json:"target"`
}

type EffectType string

const (
    EffectTypeDamage    EffectType = "DAMAGE"
    EffectTypeHeal      EffectType = "HEAL"
    EffectTypeBuff      EffectType = "BUFF"
    EffectTypeDebuff    EffectType = "DEBUFF"
    EffectTypeStatus    EffectType = "STATUS"
)

type EffectTarget string

const (
    TargetSelf      EffectTarget = "SELF"
    TargetSingle    EffectTarget = "SINGLE"
    TargetArea      EffectTarget = "AREA"
    TargetAll       EffectTarget = "ALL"
)
```

### Battle Result Schema
```go
type BattleResult struct {
    BattleID    ID              `json:"battleId"`
    Winner      TeamID          `json:"winner"`
    Duration    int             `json:"duration"` // In turns
    Rounds      int             `json:"rounds"`
    MVP         ID              `json:"mvp"`
    Statistics  BattleStats     `json:"statistics"`
    Replay      ReplayData      `json:"replay"`
}

type BattleStats struct {
    DamageDealt     map[ID]int  `json:"damageDealt"`
    DamageTaken     map[ID]int  `json:"damageTaken"`
    HealingDone     map[ID]int  `json:"healingDone"`
    KillCount       map[ID]int  `json:"killCount"`
    AbilitiesUsed   map[ID]int  `json:"abilitiesUsed"`
}

type ReplayData struct {
    InitialState    BattleState     `json:"initialState"`
    Actions         []Action        `json:"actions"`
    FinalState      BattleState     `json:"finalState"`
    Timestamps      []Timestamp     `json:"timestamps"`
}
```

## Database Schema

### Game Records
```go
type GameRecord struct {
    ID              ID              `json:"id"`
    Timestamp       Timestamp       `json:"timestamp"`
    Version         Version         `json:"version"`
    Players         []PlayerInfo    `json:"players"`
    Result          BattleResult    `json:"result"`
    Settings        GameSettings    `json:"settings"`
    AIMetrics       *AIMetrics      `json:"aiMetrics,omitempty"`
}

type GameSettings struct {
    Difficulty      float64         `json:"difficulty"`
    AIPersonality   string          `json:"aiPersonality"`
    GameSpeed       int             `json:"gameSpeed"`
    Environment     string          `json:"environment"`
}

type AIMetrics struct {
    DecisionTimes   []float64       `json:"decisionTimes"`
    Confidence      []float64       `json:"confidence"`
    StrategyScore   float64         `json:"strategyScore"`
    ErrorRate       float64         `json:"errorRate"`
}
```

### Player Records
```go
type PlayerRecord struct {
    ID              ID              `json:"id"`
    Username        string          `json:"username"`
    Created         Timestamp       `json:"created"`
    Stats           PlayerStats     `json:"stats"`
    History         []GameRecord    `json:"history"`
}

type PlayerStats struct {
    GamesPlayed     int             `json:"gamesPlayed"`
    Wins            int             `json:"wins"`
    Losses          int             `json:"losses"`
    WinRate         float64         `json:"winRate"`
    AvgGameLength   float64         `json:"avgGameLength"`
    FavoriteChar    string          `json:"favoriteChar"`
}
```

## API Schemas

### Request/Response Types
```go
type ActionRequest struct {
    GameID      ID          `json:"gameId"`
    PlayerID    ID          `json:"playerId"`
    Action      Action      `json:"action"`
    Timestamp   Timestamp   `json:"timestamp"`
}

type ActionResponse struct {
    Success     bool            `json:"success"`
    NewState    BattleState     `json:"newState"`
    Effects     []Effect        `json:"effects"`
    Messages    []string        `json:"messages"`
}

type GameStateResponse struct {
    State       BattleState     `json:"state"`
    ValidMoves  []Action        `json:"validMoves"`
    Timeline    []TimelineEntry `json:"timeline"`
}
```

## Validation Rules
```go
// Character validation
func (c *CharacterState) Validate() error {
    if c.ID == "" {
        return errors.New("character ID required")
    }
    if c.Stats.Health < 0 {
        return errors.New("health cannot be negative")
    }
    if c.Stats.MaxHealth < c.Stats.Health {
        return errors.New("current health exceeds max health")
    }
    return nil
}

// Action validation
func (a *Action) Validate() error {
    if a.ID == "" {
        return errors.New("action ID required")
    }
    if a.Source == "" {
        return errors.New("action source required")
    }
    switch a.Type {
    case ActionTypeAbility:
        if a.Ability == nil {
            return errors.New("ability details required for ability action")
        }
    case ActionTypeMove:
        if a.Movement == nil {
            return errors.New("movement details required for move action")
        }
    }
    return nil
}
```