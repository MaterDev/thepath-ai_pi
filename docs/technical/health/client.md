# Client Health Monitoring

## Overview

The client service implements health monitoring to track the React application's status and its connections to the server and WebSocket.

## Implementation

### 1. Health Check Endpoint

```typescript
// src/health/health.ts
import express from 'express';
import { checkServerConnection, checkWebSocket } from './checks';

const app = express();

app.get('/health', async (req, res) => {
    const serverHealth = await checkServerConnection();
    const wsHealth = await checkWebSocket();
    
    res.json({
        status: serverHealth && wsHealth ? 'healthy' : 'unhealthy',
        timestamp: Date.now(),
        version: process.env.REACT_APP_VERSION,
        service: 'client',
        dependencies: {
            server: serverHealth ? 'connected' : 'disconnected',
            websocket: wsHealth ? 'connected' : 'disconnected'
        }
    });
});
```

### 2. Connection Checks

```typescript
// src/health/checks.ts
import axios from 'axios';
import { socket } from '../websocket';

export async function checkServerConnection(): Promise<boolean> {
    try {
        const response = await axios.get(
            `${process.env.REACT_APP_API_URL}/health`,
            { timeout: 5000 }
        );
        return response.status === 200;
    } catch {
        return false;
    }
}

export function checkWebSocket(): Promise<boolean> {
    return new Promise((resolve) => {
        if (socket.connected) {
            resolve(true);
            return;
        }
        
        const timeout = setTimeout(() => resolve(false), 5000);
        
        socket.once('connect', () => {
            clearTimeout(timeout);
            resolve(true);
        });
        
        socket.connect();
    });
}
```

### 3. Health Monitor Component

```typescript
// src/components/HealthMonitor.tsx
import React, { useEffect, useState } from 'react';
import { Alert } from '@mui/material';

export const HealthMonitor: React.FC = () => {
    const [isHealthy, setIsHealthy] = useState(true);
    
    useEffect(() => {
        const checkHealth = async () => {
            try {
                const response = await fetch('/health');
                const health = await response.json();
                setIsHealthy(health.status === 'healthy');
            } catch {
                setIsHealthy(false);
            }
        };
        
        checkHealth();
        const interval = setInterval(checkHealth, 30000);
        return () => clearInterval(interval);
    }, []);
    
    if (!isHealthy) {
        return (
            <Alert severity="error">
                Connection issues detected. Please refresh the page.
            </Alert>
        );
    }
    
    return null;
};
```

## Docker Integration

### 1. Health Check Configuration

```yaml
# docker-compose.yml
services:
  client:
    build:
      context: ./client
      dockerfile: ../docker/dev/client.Dockerfile
    healthcheck:
      test: ["CMD", "wget", "-qO-", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
```

### 2. Dockerfile Setup

```dockerfile
# docker/dev/client.Dockerfile
FROM node:18-alpine

# Health check dependencies
RUN apk add --no-cache wget curl

WORKDIR /app/client
COPY package*.json ./
RUN npm install
COPY . .

# Health check setup
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD wget -qO- http://localhost:3000/health || exit 1

EXPOSE 3000
CMD ["npm", "start"]
```

## Error Handling

### 1. Connection Recovery

```typescript
// src/websocket/reconnect.ts
import { socket } from './socket';

export function setupReconnection() {
    let retries = 0;
    const maxRetries = 5;
    
    socket.on('disconnect', () => {
        if (retries < maxRetries) {
            setTimeout(() => {
                retries++;
                socket.connect();
            }, Math.min(1000 * retries, 5000));
        } else {
            console.error('Max reconnection attempts reached');
        }
    });
    
    socket.on('connect', () => {
        retries = 0;
    });
}
```

### 2. Error Boundary

```typescript
// src/components/ErrorBoundary.tsx
import React, { Component, ErrorInfo } from 'react';
import { Alert } from '@mui/material';

interface Props {
    children: React.ReactNode;
}

interface State {
    hasError: boolean;
}

export class ErrorBoundary extends Component<Props, State> {
    state = { hasError: false };
    
    static getDerivedStateFromError() {
        return { hasError: true };
    }
    
    componentDidCatch(error: Error, info: ErrorInfo) {
        console.error('Client error:', error, info);
    }
    
    render() {
        if (this.state.hasError) {
            return (
                <Alert severity="error">
                    Something went wrong. Please refresh the page.
                </Alert>
            );
        }
        
        return this.props.children;
    }
}
```

## Monitoring

### 1. Health Check Script

```bash
#!/bin/bash
# scripts/check-client-health.sh

check_client() {
    response=$(curl -s http://localhost:3000/health)
    status=$(echo $response | jq -r '.status')
    
    if [ "$status" = "healthy" ]; then
        echo "Client is healthy"
        return 0
    else
        echo "Client is unhealthy"
        echo "Response: $response"
        return 1
    fi
}

check_client
```

### 2. Logging

```typescript
// src/utils/logger.ts
export const logger = {
    error: (message: string, error?: Error) => {
        console.error(message, error);
        // Send to logging service
    },
    
    warn: (message: string) => {
        console.warn(message);
        // Send to logging service
    },
    
    info: (message: string) => {
        console.info(message);
        // Send to logging service
    }
};
```

## Best Practices

1. **Regular Health Checks**
   - Monitor every 30 seconds
   - Quick timeout (5s max)
   - Limited retries

2. **Error Recovery**
   - Automatic reconnection
   - User notifications
   - Graceful degradation

3. **Performance**
   - Lightweight checks
   - Minimal dependencies
   - Efficient logging
