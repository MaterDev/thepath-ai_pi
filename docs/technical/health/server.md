# Server Health Monitoring

## Overview

The server implements comprehensive health monitoring to track the Go application's status, database connections, and AI service integration.

## Implementation

### 1. Health Check Handler

```go
// internal/health/handler.go
package health

import (
    "encoding/json"
    "net/http"
    "time"
)

type HealthResponse struct {
    Status       string            `json:"status"`
    Timestamp    int64            `json:"timestamp"`
    Version      string           `json:"version"`
    Service      string           `json:"service"`
    Dependencies map[string]string `json:"dependencies"`
}

func NewHealthHandler(checker *HealthChecker) http.HandlerFunc {

    return func(w http.ResponseWriter, r *http.Request) {

        mongoHealth := checker.CheckMongo()
        aiHealth := checker.CheckAIService()

        health := HealthResponse{
            Status:    "healthy",
            Timestamp: time.Now().UnixMilli(),
            Version:   "1.0.0",
            Service:   "server",
            Dependencies: map[string]string{
                "mongodb":    mongoHealth,
                "ai_service": aiHealth,
            },
        }

        if mongoHealth != "connected" || aiHealth != "connected" {
            health.Status = "unhealthy"
        }

        w.Header().Set("Content-Type", "application/json")

        json.NewEncoder(w).Encode(health)
    }
}

```

### 2. Health Checker

```go
// internal/health/checker.go
package health

import (
    "context"
    "time"

    "go.mongodb.org/mongo-driver/mongo"

    "go.mongodb.org/mongo-driver/mongo/readpref"

)

type HealthChecker struct {
    mongo     *mongo.Client

    aiService string
}

func (c *HealthChecker) CheckMongo() string {

    ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)

    defer cancel()

    err := c.mongo.Ping(ctx, readpref.Primary())
    if err != nil {
        return "disconnected"
    }
    return "connected"
}

func (c *HealthChecker) CheckAIService() string {

    ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)

    defer cancel()

    req, err := http.NewRequestWithContext(ctx, "GET",
        c.aiService + "/health", nil)
    if err != nil {
        return "disconnected"
    }

    resp, err := http.DefaultClient.Do(req)
    if err != nil || resp.StatusCode != http.StatusOK {
        return "disconnected"
    }
    return "connected"
}

```

### 3. WebSocket Health

```go
// internal/websocket/health.go
package websocket

import (
    "sync"
    "time"
)

type ConnectionHealth struct {
    mu    sync.RWMutex
    conns map[string]*Connection

}

func (h *ConnectionHealth) Monitor() {

    ticker := time.NewTicker(30 * time.Second)

    for range ticker.C {
        h.mu.RLock()
        for id, conn := range h.conns {
            if !conn.IsHealthy() {
                go conn.Reconnect()
            }
        }
        h.mu.RUnlock()
    }
}

func (h *ConnectionHealth) Add(id string, conn *Connection) {

    h.mu.Lock()
    defer h.mu.Unlock()
    h.conns[id] = conn
}

func (h *ConnectionHealth) Remove(id string) {

    h.mu.Lock()
    defer h.mu.Unlock()
    delete(h.conns, id)
}

```

## Docker Integration

### 1. Health Check Configuration

```yaml

# docker-compose.yml

services:
  server:
    build:
      context: ./server
      dockerfile: ../docker/dev/server.Dockerfile
    healthcheck:
      test: ["CMD", "wget", "-qO-", "http://localhost:8080/health"]

      interval: 30s
      timeout: 10s
      retries: 3

```

### 2. Dockerfile Setup

```dockerfile

# docker/dev/server.Dockerfile

FROM golang:1.21-alpine

# Health check dependencies

RUN apk add --no-cache wget curl

WORKDIR /app/server
COPY go.* ./

RUN go mod download
COPY . .

# Health check setup

HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \

    CMD wget -qO- http://localhost:8080/health || exit 1

EXPOSE 8080
CMD ["go", "run", "cmd/main.go"]

```

## Error Handling

### 1. Middleware

```go
// internal/middleware/recovery.go
package middleware

import (
    "log"
    "net/http"
)

func Recovery(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {

        defer func() {
            if err := recover(); err != nil {
                log.Printf("panic: %v", err)
                http.Error(w,
                    "Internal server error",
                    http.StatusInternalServerError)
            }
        }()
        next.ServeHTTP(w, r)
    })
}

```

### 2. Connection Recovery

```go
// internal/websocket/connection.go
package websocket

import (
    "time"
    "github.com/gorilla/websocket"
)

type Connection struct {
    conn     *websocket.Conn

    attempts int
}

func (c *Connection) Reconnect() error {

    if c.attempts >= 5 {
        return errors.New("max reconnection attempts reached")
    }

    backoff := time.Duration(c.attempts) * time.Second

    time.Sleep(backoff)

    // Attempt reconnection
    newConn, err := c.dial()
    if err != nil {
        c.attempts++
        return err
    }

    c.conn = newConn
    c.attempts = 0
    return nil
}

```

## Monitoring

### 1. Health Check Script

```bash
#!/bin/bash

# scripts/check-server-health.sh

check_server() {
    response=$(curl -s http://localhost:8080/health)

    status=$(echo $response | jq -r '.status')

    if [ "$status" = "healthy" ]; then
        echo "Server is healthy"
        return 0
    else
        echo "Server is unhealthy"
        echo "Response: $response"
        return 1
    fi
}

check_server

```

### 2. Logging

```go
// internal/logger/logger.go
package logger

import (
    "log"
    "os"
)

type Logger struct {
    info  *log.Logger

    warn  *log.Logger

    error *log.Logger

}

func New() *Logger {

    return &Logger{
        info:  log.New(os.Stdout, "INFO: ", log.LstdFlags),
        warn:  log.New(os.Stdout, "WARN: ", log.LstdFlags),
        error: log.New(os.Stderr, "ERROR: ", log.LstdFlags),
    }
}

```

## Best Practices

1. **Regular Health Checks**

   - Monitor every 30 seconds

   - Quick timeout (5s max)

   - Limited retries

2. **Error Recovery**

   - Automatic reconnection

   - Graceful shutdown

   - Connection pooling

3. **Performance**

   - Lightweight checks

   - Connection reuse

   - Efficient logging
