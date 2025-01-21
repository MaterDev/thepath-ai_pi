# API Endpoints

## Overview

This document defines all API endpoints and WebSocket events used in the system. All endpoints use JSON for request/response bodies.

## WebSocket Events

### Connection Events

```typescript
// Client -> Server
interface ConnectRequest {
    type: 'connect'
    playerId: string
    sessionId?: string
}

// Server -> Client
interface ConnectResponse {
    type: 'connect_response'
    success: boolean
    sessionId?: string
    error?: string
}
```

### Game Events

```typescript
// Client -> Server
interface GameAction {
    type: 'game_action'
    actionType: 'ATTACK' | 'DEFEND' | 'ABILITY' | 'ITEM'
    targetId?: string
    abilityId?: string
    itemId?: string
    position?: Position
}

// Server -> Client
interface GameUpdate {
    type: 'game_update'
    state: GameState
    lastAction?: GameAction
    nextTurn: string
    timestamp: number
}
```

### AI Events

```typescript
// Server -> AI
interface AIRequest {
    type: 'ai_request'
    gameState: GameState
    difficulty: number  // 0.2-0.95
    personality: string
    timeLimit: number  // ms
}

// AI -> Server
interface AIResponse {
    type: 'ai_response'
    action: GameAction
    confidence: number
    processingTime: number
}
```

### System Events

```typescript
// Server -> Client
interface SystemEvent {
    type: 'system_event'
    eventType: 'ERROR' | 'WARNING' | 'INFO'
    message: string
    code: number
}
```

## REST Endpoints

### Game Management

```typescript
// POST /api/games
interface CreateGameRequest {
    players: string[]
    aiDifficulty?: number
    aiPersonality?: string
    gameMode: 'PVP' | 'PVE'
}

interface CreateGameResponse {
    gameId: string
    sessionId: string
    websocketUrl: string
}

// GET /api/games/:gameId
interface GameDetailsResponse {
    gameId: string
    status: GameStatus
    players: Player[]
    currentTurn: string
    round: number
    state: GameState
}

// POST /api/games/:gameId/action
interface GameActionRequest {
    playerId: string
    action: GameAction
}

interface GameActionResponse {
    success: boolean
    newState?: GameState
    error?: string
}
```

### Replay System

```typescript
// GET /api/replays/:gameId
interface ReplayResponse {
    gameId: string
    initialState: GameState
    actions: GameAction[]
    outcomes: GameOutcome[]
    aiMetrics?: AIMetrics[]
}

// POST /api/replays/:gameId/analyze
interface AnalyzeReplayRequest {
    focus: 'AI_BEHAVIOR' | 'PLAYER_PATTERNS' | 'PERFORMANCE'
}

interface AnalyzeReplayResponse {
    analysis: ReplayAnalysis
    insights: string[]
    recommendations: string[]
}
```

### Analytics

```typescript
// GET /api/analytics/performance
interface PerformanceMetricsResponse {
    aiResponseTimes: number[]
    serverUpdateTimes: number[]
    memoryUsage: MemoryMetrics
    cpuUsage: CPUMetrics
    temperature: number
}

// GET /api/analytics/ai
interface AIMetricsResponse {
    decisionConfidence: number[]
    adaptationRate: number
    personalityMetrics: PersonalityMetrics
    difficultyProgression: number[]
}
```

## Error Handling

### Error Codes

```typescript
enum ErrorCode {
    // Client Errors (4xx)
    INVALID_REQUEST = 400,
    UNAUTHORIZED = 401,
    FORBIDDEN = 403,
    NOT_FOUND = 404,
    CONFLICT = 409,
    
    // Server Errors (5xx)
    SERVER_ERROR = 500,
    AI_ERROR = 501,
    HARDWARE_ERROR = 502,
    TIMEOUT = 504
}
```

### Error Response Format

```typescript
interface ErrorResponse {
    code: ErrorCode
    message: string
    details?: any
    timestamp: number
}
```

## Data Types

### Game State

```typescript
interface GameState {
    id: string
    version: string
    timestamp: number
    characters: Map<string, CharacterState>
    turnOrder: string[]
    currentTurn: number
    round: number
    status: GameStatus
    environment?: EnvironmentState
}
```

### Character State

```typescript
interface CharacterState {
    id: string
    name: string
    health: number
    maxHealth: number
    position: Position
    status: StatusEffect[]
    abilities: Ability[]
    inventory: Item[]
}
```

## WebSocket Connection Example

```typescript
// Client-side connection
const ws = new WebSocket('ws://server/game')

ws.onopen = () => {
    ws.send(JSON.stringify({
        type: 'connect',
        playerId: 'player1'
    }))
}

ws.onmessage = (event) => {
    const data = JSON.parse(event.data)
    switch (data.type) {
        case 'game_update':
            updateGameState(data.state)
            break
        case 'system_event':
            handleSystemEvent(data)
            break
    }
}
