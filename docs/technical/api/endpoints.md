---

title: API Endpoints Reference
description: Complete reference documentation for all API endpoints, including request/response formats and authentication requirements

---

# API Endpoints

## Overview

This document defines all API endpoints and WebSocket events used in the system. All endpoints use JSON for request/response bodies.

## Implementation

### Authentication

```python
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = await validate_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user

```

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

## Usage

### Authentication

```bash

# Get authentication token

curl -X POST http://localhost:8000/token \

  -H "Content-Type: application/x-www-form-urlencoded" \

  -d "username=user&password=pass"

# Use token in subsequent requests

curl -X GET http://localhost:8000/api/v1/game/state \

  -H "Authorization: Bearer {token}"

```

### Game State Management

```python
import requests

def update_game_state(token: str, state: dict):
    response = requests.post(
        "http://localhost:8000/api/v1/game/state",
        headers={"Authorization": f"Bearer {token}"},
        json=state
    )
    return response.json()

```

### AI Interactions

```python
def get_ai_action(token: str, context: dict):
    response = requests.post(
        "http://localhost:8000/api/v1/ai/action",
        headers={"Authorization": f"Bearer {token}"},
        json=context
    )
    return response.json()

```

## Configuration

### Environment Variables

```bash

# API configuration

API_HOST=localhost
API_PORT=8000
API_DEBUG=false

# Authentication

AUTH_SECRET_KEY=your-secret-key

AUTH_ALGORITHM=HS256
AUTH_TOKEN_EXPIRE_MINUTES=30

# Rate Limiting

RATE_LIMIT_REQUESTS=100
RATE_LIMIT_PERIOD=60

```

### Rate Limiting Configuration

```python
from fastapi import FastAPI
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/api/v1/game/state")
@limiter.limit("100/minute")
async def get_game_state(request: Request):
    return {"status": "success"}
