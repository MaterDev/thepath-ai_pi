# AI Service Health Monitoring

## Overview

The AI service implements health monitoring to track model loading, inference performance, and system resources on the Raspberry Pi.

## Implementation

### 1. Health Check Endpoint

```python
# src/health/routes.py
from flask import jsonify
from time import time
import psutil
import tensorflow as tf

from .model import check_model_loaded
from .system import check_system_resources

@app.route('/health')
def health():
    model_status = check_model_loaded()
    system_status = check_system_resources()
    
    return jsonify({
        'status': 'healthy' if model_status and system_status else 'unhealthy',
        'timestamp': int(time() * 1000),
        'version': '1.0.0',
        'service': 'ai',
        'dependencies': {
            'model': 'loaded' if model_status else 'unloaded',
            'system': system_status
        }
    })
```

### 2. Model Health

```python
# src/health/model.py
import tensorflow as tf
import numpy as np
from typing import Dict

class ModelHealth:
    def __init__(self, model_path: str):
        self.interpreter = tf.lite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        self.last_inference = 0
        self.inference_times = []
        
    def check_model_loaded(self) -> bool:
        try:
            # Test inference with dummy input
            input_details = self.interpreter.get_input_details()
            dummy_input = np.zeros(input_details[0]['shape'], dtype=np.float32)
            
            self.interpreter.set_tensor(input_details[0]['index'], dummy_input)
            self.interpreter.invoke()
            return True
        except Exception as e:
            print(f"Model health check failed: {e}")
            return False
            
    def track_inference(self, duration_ms: float):
        """Track inference times for monitoring"""
        self.inference_times.append(duration_ms)
        if len(self.inference_times) > 100:
            self.inference_times.pop(0)
            
    def get_stats(self) -> Dict[str, float]:
        """Get inference statistics"""
        if not self.inference_times:
            return {
                'avg_inference_ms': 0,
                'max_inference_ms': 0,
                'min_inference_ms': 0
            }
            
        return {
            'avg_inference_ms': np.mean(self.inference_times),
            'max_inference_ms': np.max(self.inference_times),
            'min_inference_ms': np.min(self.inference_times)
        }
```

### 3. System Health

```python
# src/health/system.py
import psutil
from typing import Dict

def check_system_resources() -> Dict[str, float]:
    """Check system resource usage"""
    try:
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        # Check thresholds
        if (cpu_percent > 90 or 
            memory.percent > 90 or 
            disk.percent > 90):
            return 'overloaded'
            
        return 'normal'
    except Exception as e:
        print(f"System health check failed: {e}")
        return 'unknown'
```

## Docker Integration

### 1. Health Check Configuration

```yaml
# docker-compose.yml
services:
  ai:
    build:
      context: ./ai
      dockerfile: ../docker/dev/ai.Dockerfile
    healthcheck:
      test: ["CMD", "wget", "-qO-", "http://localhost:5000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
```

### 2. Dockerfile Setup

```dockerfile
# docker/dev/ai.Dockerfile
FROM python:3.11-slim

# Health check dependencies
RUN apt-get update && apt-get install -y wget curl

WORKDIR /app/ai
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# Health check setup
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD wget -qO- http://localhost:5000/health || exit 1

EXPOSE 5000
CMD ["python", "main.py"]
```

## Error Handling

### 1. Model Recovery

```python
# src/model/recovery.py
import time
from typing import Optional
import tensorflow as tf

class ModelRecovery:
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.interpreter: Optional[tf.lite.Interpreter] = None
        self.load_attempts = 0
        
    def load_model(self) -> bool:
        """Load model with retry logic"""
        if self.load_attempts >= 3:
            raise Exception("Failed to load model after 3 attempts")
            
        try:
            self.interpreter = tf.lite.Interpreter(model_path=self.model_path)
            self.interpreter.allocate_tensors()
            self.load_attempts = 0
            return True
        except Exception as e:
            self.load_attempts += 1
            print(f"Model load attempt {self.load_attempts} failed: {e}")
            time.sleep(self.load_attempts * 2)  # Exponential backoff
            return False
```

### 2. Resource Management

```python
# src/health/resources.py
import psutil
import gc
from typing import Dict

class ResourceManager:
    def __init__(self):
        self.warning_threshold = 80  # Percentage
        self.critical_threshold = 90  # Percentage
        
    def check_resources(self) -> Dict[str, str]:
        """Check system resources and take action if needed"""
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        
        status = {
            'cpu': 'normal',
            'memory': 'normal'
        }
        
        # Handle high CPU
        if cpu > self.critical_threshold:
            status['cpu'] = 'critical'
        elif cpu > self.warning_threshold:
            status['cpu'] = 'warning'
            
        # Handle high memory
        if memory.percent > self.critical_threshold:
            status['memory'] = 'critical'
            gc.collect()  # Force garbage collection
        elif memory.percent > self.warning_threshold:
            status['memory'] = 'warning'
            
        return status
```

## Monitoring

### 1. Health Check Script

```bash
#!/bin/bash
# scripts/check-ai-health.sh

check_ai() {
    response=$(curl -s http://localhost:5000/health)
    status=$(echo $response | jq -r '.status')
    
    if [ "$status" = "healthy" ]; then
        echo "AI service is healthy"
        return 0
    else
        echo "AI service is unhealthy"
        echo "Response: $response"
        return 1
    fi
}

check_ai
```

### 2. Logging

```python
# src/utils/logger.py
import logging
from typing import Optional
from datetime import datetime

class AILogger:
    def __init__(self, log_path: Optional[str] = None):
        self.logger = logging.getLogger('ai_service')
        self.logger.setLevel(logging.INFO)
        
        if log_path:
            handler = logging.FileHandler(log_path)
        else:
            handler = logging.StreamHandler()
            
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        
    def log_inference(self, duration_ms: float, success: bool):
        """Log inference attempt"""
        self.logger.info(
            f"Inference completed: duration={duration_ms}ms success={success}"
        )
        
    def log_health(self, health_status: dict):
        """Log health check"""
        self.logger.info(f"Health check: {health_status}")
```

## Best Practices

1. **Resource Management**
   - Monitor CPU usage
   - Track memory consumption
   - Handle resource constraints

2. **Model Health**
   - Regular inference tests
   - Performance tracking
   - Automatic recovery

3. **System Health**
   - Resource monitoring
   - Garbage collection
   - Error logging

## Version History
- v1.0: Initial health monitoring
- v1.1: Added resource management
- v1.2: Enhanced model monitoring
- v2.0: Updated for simplified battle mechanics
