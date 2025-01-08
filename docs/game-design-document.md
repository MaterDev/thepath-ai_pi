# Game Design Document - The Path (AI-Pi)

## Core Game Mechanics

### Combat System
```go
type CombatSystem struct {
    TurnOrder      []string    `json:"turnOrder"`
    CurrentRound   int         `json:"currentRound"`
    ActivePlayer   string      `json:"activePlayer"`
    BattleState    BattleState `json:"battleState"`
}

type BattleState struct {
    Characters     map[string]Character `json:"characters"`
    Timeline      []TimelineEntry     `json:"timeline"`
    StatusEffects map[string][]Effect `json:"statusEffects"`
}
```

### Character System
```go
type Character struct {
    ID            string    `json:"id"`
    Name          string    `json:"name"`
    Stats         Stats     `json:"stats"`
    Abilities     []Ability `json:"abilities"`
    Status        Status    `json:"status"`
}

type Stats struct {
    Health        int     `json:"health"`
    MaxHealth     int     `json:"maxHealth"`
    Attack        int     `json:"attack"`
    Defense       int     `json:"defense"`
    Speed         int     `json:"speed"`
    Initiative    float64 `json:"initiative"`
}

type Status struct {
    IsAlive       bool              `json:"isAlive"`
    Position      Position          `json:"position"`
    Effects       []StatusEffect    `json:"effects"`
}
```

### Action System
```go
type Action struct {
    Type          ActionType   `json:"type"`
    Source        string       `json:"source"`
    Target        string       `json:"target"`
    Ability       *Ability     `json:"ability,omitempty"`
    Movement      *Movement    `json:"movement,omitempty"`
}

type ActionType string

const (
    ActionAbility    ActionType = "ABILITY"
    ActionMove       ActionType = "MOVE"
    ActionWait       ActionType = "WAIT"
    ActionDefend     ActionType = "DEFEND"
)

type Ability struct {
    ID            string       `json:"id"`
    Name          string       `json:"name"`
    Type          AbilityType  `json:"type"`
    Power         int          `json:"power"`
    Cost          int          `json:"cost"`
    Effects       []Effect     `json:"effects"`
}
```

## Game Flow

### Turn Structure
1. Initiative Calculation
   ```go
   func (c *Character) CalculateInitiative() float64 {
       return float64(c.Stats.Speed) * (1.0 + rand.Float64() * 0.2)
   }
   ```

2. Action Selection
3. Action Resolution
4. Status Update
5. Victory Check

### Victory Conditions
- All enemy characters defeated
- Specific objective completed
- Survival for specified turns

## Combat Mechanics

### Damage Calculation
```go
func CalculateDamage(source *Character, target *Character, ability Ability) int {
    baseDamage := source.Stats.Attack * ability.Power
    mitigation := float64(target.Stats.Defense) * 0.5
    return int(float64(baseDamage) * (1.0 - mitigation/100.0))
}
```

### Status Effects
```go
type StatusEffect struct {
    ID            string    `json:"id"`
    Type          EffectType `json:"type"`
    Duration      int       `json:"duration"`
    Strength      int       `json:"strength"`
    Source        string    `json:"source"`
}

type EffectType string

const (
    EffectBurn      EffectType = "BURN"
    EffectPoison    EffectType = "POISON"
    EffectStun      EffectType = "STUN"
    EffectBuff      EffectType = "BUFF"
    EffectDebuff    EffectType = "DEBUFF"
)
```

## Game Balance

### Base Character Stats
```go
var BaseStats = map[string]Stats{
    "Warrior": {
        Health: 100,
        Attack: 15,
        Defense: 10,
        Speed: 8,
    },
    "Mage": {
        Health: 70,
        Attack: 20,
        Defense: 5,
        Speed: 7,
    },
    "Rogue": {
        Health: 85,
        Attack: 18,
        Defense: 7,
        Speed: 12,
    },
}
```

### Ability Power Ranges
- Basic Abilities: 80-120% base damage
- Special Abilities: 150-200% base damage
- Ultimate Abilities: 250-300% base damage

## Core Game Loop
1. Battle Initialization
2. Turn Order Determination
3. Action Selection Phase
4. Action Resolution Phase
5. Status Update Phase
6. Victory Check
7. Repeat from step 3 until victory/defeat

## Implementation Notes

### Performance Targets
- Turn resolution: < 100ms
- AI decision making: < 500ms
- State updates: < 50ms

### State Management
```go
type GameState struct {
    ID            string       `json:"id"`
    Phase         GamePhase    `json:"phase"`
    Round         int          `json:"round"`
    Combat        CombatSystem `json:"combat"`
    LastAction    *Action      `json:"lastAction,omitempty"`
}

type GamePhase string

const (
    PhaseInit      GamePhase = "INIT"
    PhaseActive    GamePhase = "ACTIVE"
    PhaseVictory   GamePhase = "VICTORY"
    PhaseDefeat    GamePhase = "DEFEAT"
)