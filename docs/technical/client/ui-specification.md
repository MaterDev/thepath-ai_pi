# Client UI Specification

## Overview

The client interface is a simple, Material-UI based battle system focusing on turn-based combat mechanics.

## Core Components

### 1. Authentication

- Login form

- Basic user profile display

- Session management

### 2. Battle Management

```typescript
interface BattleControls {
    // Core battle actions
    createBattle(): void
    joinBattle(id: string): void
    forfeitBattle(): void
    exitBattle(): void
}

```

### 3. Battle Interface

- Health/Energy displays

- Action buttons (Attack, Defend, Special)

- Status effect indicators

- Turn indicator

- Opponent state display

### 4. State Indicators

```typescript
interface UIStates {
    isPlayerTurn: boolean      // Enable/disable controls
    isWaiting: boolean         // Show loading state
    battleStatus: 'active' | 'victory' | 'defeat'
    availableActions: string[]
}

```

## Component Structure

### 1. Layout

```typescript
interface BattleLayout {
    header: {
        playerInfo: PlayerDisplay
        battleStatus: StatusBar
    }
    main: {
        battlefield: BattleView
        actionPanel: ActionButtons
    }
    footer: {
        statusEffects: EffectList
        exitButton: Button
    }
}

```

### 2. Material-UI Components

```typescript
// Core components used
import {
    Button,
    Card,
    CircularProgress,
    Dialog,
    LinearProgress,
    Typography
} from '@mui/material'

```

## State Management

### 1. Redux Store

```typescript
interface BattleState {
    // Core state
    battleId: string | null
    playerState: PlayerState
    opponentState: OpponentState
    turnState: TurnState

    // UI state
    loading: boolean
    error: string | null
    activeAction: string | null
}

```

### 2. Actions

```typescript
type BattleAction =
    | { type: 'CREATE_BATTLE' }
    | { type: 'JOIN_BATTLE', payload: string }
    | { type: 'SUBMIT_ACTION', payload: GameAction }
    | { type: 'FORFEIT_BATTLE' }
    | { type: 'UPDATE_STATE', payload: GameState }

```

## User Interactions

### 1. Battle Flow

1. User logs in
2. Creates or joins battle
3. Waits for turn
4. Selects action when available
5. Waits for opponent
6. Repeats until battle ends

### 2. Action States

- Buttons disabled during opponent's turn

- Loading indicator during AI processing

- Clear victory/defeat states

- Forfeit available during player's turn

## Error Handling

### 1. Basic Error States

- Connection lost

- Invalid action

- Battle ended

- Server error

### 2. User Feedback

- Error messages

- Action confirmations

- Status updates

- Battle results

## Styling

### 1. Material-UI Theme

```typescript
const theme = createTheme({
    palette: {
        primary: {
            main: '#1976d2'

        },
        secondary: {
            main: '#dc004e'

        }
    },
    components: {
        MuiButton: {
            styleOverrides: {
                root: {
                    margin: '8px'
                }
            }
        }
    }
})

```

### 2. Layout Structure

```css
.battle-container {

    display: grid;
    grid-template-rows: auto 1fr auto;

    height: 100vh;
    padding: 16px;
}

.action-panel {

    display: flex;
    justify-content: center;

    gap: 16px;
    padding: 16px;
}

```
