# API Endpoints

## Overview

This document defines all API endpoints and WebSocket events used in the system. All endpoints use JSON for request/response bodies.

## REST Endpoints

### Authentication
- `POST /auth/login`: User login
- `POST /auth/register`: New user registration
- `POST /auth/refresh`: Refresh access token
- `POST /auth/logout`: User logout

### Battle Management
- `POST /battles`: Create new battle
- `GET /battles`: List available battles
- `GET /battles/{id}`: Get battle details
- `POST /battles/{id}/join`: Join existing battle
- `POST /battles/{id}/forfeit`: Forfeit battle

### User Management
- `GET /users/me`: Get current user
- `PATCH /users/me`: Update user profile
- `GET /users/{id}`: Get user details
- `GET /users/{id}/stats`: Get user stats

### Game State
- `GET /state`: Get current game state
- `GET /state/history`: Get state history
- `GET /state/replay/{id}`: Get battle replay

## WebSocket Events

### Connection Events
- `connect`: Initial connection
- `disconnect`: Client disconnect
- `reconnect`: Client reconnection
- `error`: Connection error

### Game Events
- `game:start`: Battle starts
- `game:action`: Player action
- `game:update`: State update
- `game:end`: Battle ends

### AI Events
- `ai:thinking`: AI processing
- `ai:action`: AI action taken
- `ai:error`: AI processing error
- `ai:ready`: AI ready for next turn

### System Events
- `system:maintenance`: System maintenance
- `system:error`: System error
- `system:restart`: System restart
- `system:update`: System update

## Data Schemas

### Authentication
```typescript
interface AuthRequest {
    username: string
    password: string
}

interface AuthResponse {
    token: string
    refreshToken: string
    expiresIn: number
}
```

### Battle
```typescript
interface Battle {
    id: string
    players: Player[]
    state: GameState
    status: BattleStatus
    createdAt: number
    updatedAt: number
}

type BattleStatus = 'WAITING' | 'ACTIVE' | 'FINISHED'
```

### Game State
```typescript
interface GameState {
    battleId: string
    round: number
    currentTurn: string
    players: {
        [playerId: string]: PlayerState
    }
    status: GameStatus
    lastAction?: GameAction
}

interface PlayerState {
    health: number
    energy: number
    status: StatusEffect[]
    position: Position
}
```

## Error Handling

### HTTP Status Codes
- 200: Success
- 201: Created
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 409: Conflict
- 429: Too Many Requests
- 500: Server Error

### Error Response
```typescript
interface ErrorResponse {
    code: string
    message: string
    details?: any
}
```

## Rate Limiting

### Limits
- Authentication: 5 requests/minute
- Battle Creation: 2 requests/minute
- Game Actions: 30 requests/minute
- State Queries: 60 requests/minute

### Headers
- `X-RateLimit-Limit`
- `X-RateLimit-Remaining`
- `X-RateLimit-Reset`

## WebSocket Protocol

### Connection
- Max reconnect attempts: 5
- Reconnect delay: 1000ms
- Ping interval: 30000ms
- Pong timeout: 5000ms

### Message Format
- JSON encoding
- UTF-8 character set
- Binary messages not supported
- Max message size: 16KB

## Security

### Authentication
- JWT tokens
- HTTPS required
- CORS enabled
- XSS protection

### Rate Limiting
- Per-user limits
- Per-IP limits
- Burst allowance
- Sliding window
