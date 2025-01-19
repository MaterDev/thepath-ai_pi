# Project Dependencies

## Overview

This document lists all project dependencies and their versions to ensure consistent development and deployment.

## Server Dependencies (Go)

```go
// go.mod
module github.com/mater-dev/thepath-ai_pi

go 1.21

require (
    github.com/gorilla/websocket v1.5.1
    github.com/gin-gonic/gin v1.9.1
    github.com/golang-jwt/jwt/v5 v5.2.0
    github.com/google/uuid v1.5.0
    go.mongodb.org/mongo-driver v1.13.1
)
```

## Client Dependencies (TypeScript)

```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "redux": "^5.0.0",
    "react-redux": "^9.0.4",
    "@reduxjs/toolkit": "^2.0.1",
    "@mui/material": "^5.15.0",
    "@mui/icons-material": "^5.15.0",
    "@emotion/react": "^11.11.1",
    "@emotion/styled": "^11.11.0",
    "typescript": "^5.3.3",
    "axios": "^1.6.2",
    "socket.io-client": "^4.7.2"
  },
  "devDependencies": {
    "@types/react": "^18.2.45",
    "@types/react-dom": "^18.2.18",
    "@typescript-eslint/eslint-plugin": "^6.15.0",
    "@typescript-eslint/parser": "^6.15.0",
    "eslint": "^8.56.0",
    "jest": "^29.7.0",
    "@testing-library/react": "^14.1.2",
    "vite": "^5.0.10"
  }
}
```

## AI System Dependencies (Python)

```python
# requirements.txt

# Core Dependencies
tensorflow-lite==2.14.0
numpy==1.24.3
pandas==2.1.3
scikit-learn==1.3.2
python-socketio==5.10.0
pydantic==2.5.2
```

## Hardware Dependencies

```yaml
Raspberry_Pi_5:
  model: "BCM2712"
  cpu: "2.4GHz quad-core 64-bit Arm Cortex-A76"
  memory: "8GB LPDDR4X-4267"
  gpu: "VideoCore VII"
  graphics_apis:
    - "OpenGL ES 3.1"
    - "Vulkan 1.2"
  pcie: "PCIe 2.0 x1"
  power: "5V/5A USB-C (PD)"

AI_HAT_Plus:
  model: "26 TOPS variant"
  accelerator: "Hailo-8"
  interface: "PCIe 2.0 x1"
  power_modes:
    - "26 TOPS @ 10.4W"
    - "19.5 TOPS @ 7.8W"
    - "13 TOPS @ 5.2W"
```

## Graphics Dependencies

```yaml
Vulkan_SDK: ">=1.2"
OpenGL_ES: ">=3.1"
GPU_Memory: "1GB reserved"
```

## Performance Requirements

```yaml
Minimum_Performance:
  cpu_frequency: "2.4GHz"
  memory_bandwidth: "34.1 GB/s"
  gpu_features:
    - "Vulkan 1.2 support"
    - "4Kp60 rendering"
  ai_performance: "26 TOPS"
  pcie_bandwidth: "5 Gbps"
```

## WebSocket Protocol

### Connection Events
```typescript
interface WebSocketEvents {
    // Authentication
    'auth:login': { token: string }
    'auth:logout': void
    
    // Battle Management
    'battle:create': void
    'battle:join': { battleId: string }
    'battle:leave': void
    'battle:forfeit': void
    
    // Game Actions
    'action:submit': {
        type: 'ATTACK' | 'DEFEND' | 'SPECIAL'
        targetId?: string
        data?: Record<string, any>
    }
    
    // State Updates
    'state:update': {
        battleState: BattleState
        playerState: PlayerState
        turnState: {
            currentTurn: string  // playerId
            timeRemaining?: number
            isPlayerTurn: boolean
        }
    }
    
    // Status Updates
    'status:waiting': void  // AI is thinking
    'status:ready': void    // Player can take action
    'status:error': { message: string }
    'status:victory': void
    'status:defeat': void
}

interface BattleState {
    id: string
    players: {
        id: string
        name: string
        health: number
        status: string[]
    }[]
    round: number
    status: 'ACTIVE' | 'FINISHED'
}

interface PlayerState {
    health: number
    energy: number
    status: string[]
    availableActions: string[]
}
```

### Example Flow
```typescript
// 1. Connect and authenticate
socket.emit('auth:login', { token: 'user-jwt' })

// 2. Create or join battle
socket.emit('battle:create')
// or
socket.emit('battle:join', { battleId: 'existing-id' })

// 3. Receive initial state
socket.on('state:update', (state) => {
    if (state.turnState.isPlayerTurn) {
        // Enable UI actions
    } else {
        // Disable UI, show waiting state
    }
})

// 4. Submit action when it's player's turn
socket.emit('action:submit', {
    type: 'ATTACK',
    targetId: 'opponent-id'
})

// 5. Handle game end
socket.on('status:victory', () => {
    // Show victory screen
})
socket.on('status:defeat', () => {
    // Show defeat screen
})
```

## System Requirements

### Operating System
- Raspberry Pi OS (64-bit)
- Kernel version: 6.1+
- Python 3.11+
- Node.js 20+
- Go 1.21+

### Development Tools
- Docker 24+
- Docker Compose 2.23+
- Git 2.42+
- VSCode 1.84+

## Database

```yaml
# MongoDB
version: '6.0'
replica_set: true
wiredTiger:
  engineConfig:
    cacheSizeGB: 0.5
```

## Infrastructure

```yaml
# docker-compose.yml
version: '3.8'

services:
  server:
    build: ./server
    image: thepath-ai_pi/server:latest
    depends_on:
      - mongodb
      - redis

  client:
    build: ./client
    image: thepath-ai_pi/client:latest
    depends_on:
      - server

  ai:
    build: ./ai
    image: thepath-ai_pi/ai:latest
    devices:
      - "/dev/i2c-1:/dev/i2c-1"
    depends_on:
      - server

  mongodb:
    image: mongo:6.0
    volumes:
      - mongodb_data:/data/db

  redis:
    image: redis:7.2
    volumes:
      - redis_data:/data
```

## Development Tools

### VSCode Extensions
- Go
- Python
- TypeScript and JavaScript
- ESLint
- Prettier
- Docker
- Remote - SSH
- GitLens

### Git Hooks
```bash
# pre-commit
#!/bin/sh
go fmt ./...
go vet ./...
npm run lint
black ai/
isort ai/
pylint ai/
```

## Version Control

```yaml
# .gitignore
node_modules/
dist/
venv/
__pycache__/
*.pyc
.env
.env.*
*.log
coverage/
.DS_Store
```

## Related Documentation
- [Project Setup](../implementation/setup/project-setup.md)
- [Contributing Guide](../meta/contributing.md)
- [Style Guide](../meta/style-guide.md)
