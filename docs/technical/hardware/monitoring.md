# Hardware Monitoring

## Overview

This guide covers the monitoring system for tracking hardware performance:
- Real-time metrics
- Performance logging
- Alert system
- Visualization

## Core Components

### 1. Metric Collection

```python
@dataclass
class SystemMetrics:
    """System performance metrics"""
    timestamp: float
    cpu_usage: float
    memory_usage: float
    temperature: float
    ai_hat_usage: float
    disk_usage: float
    network_usage: float

class MetricCollector:
    """Collect system metrics"""
    def __init__(self, interval: float = 1.0):
        self.interval = interval
        self.metrics_buffer = deque(maxlen=1000)
    
    def collect_metrics(self) -> SystemMetrics:
        """Collect current system metrics"""
        return SystemMetrics(
            timestamp=time.time(),
            cpu_usage=psutil.cpu_percent(),
            memory_usage=psutil.virtual_memory().percent,
            temperature=self._get_cpu_temp(),
            ai_hat_usage=self._get_ai_hat_usage(),
            disk_usage=psutil.disk_usage('/').percent,
            network_usage=self._get_network_usage()
        )
    
    async def start_collection(self):
        """Start metric collection loop"""
        while True:
            metrics = self.collect_metrics()
            self.metrics_buffer.append(metrics)
            await asyncio.sleep(self.interval)
```

### 2. Performance Logging

```python
class PerformanceLogger:
    """Log system performance metrics"""
    def __init__(self, log_path: str = "performance.log"):
        self.log_path = log_path
        self.setup_logging()
    
    def setup_logging(self):
        """Configure logging system"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s [%(levelname)s] %(message)s',
            handlers=[
                logging.FileHandler(self.log_path),
                logging.StreamHandler()
            ]
        )
    
    def log_metrics(self, metrics: SystemMetrics):
        """Log current metrics"""
        logging.info(
            f"CPU: {metrics.cpu_usage:.1f}% | "
            f"Memory: {metrics.memory_usage:.1f}% | "
            f"Temp: {metrics.temperature:.1f}°C | "
            f"AI HAT: {metrics.ai_hat_usage:.1f}%"
        )
```

### 3. Alert System

```python
class AlertSystem:
    """Monitor and alert on system conditions"""
    def __init__(self):
        self.thresholds = {
            'cpu_usage': 80.0,
            'memory_usage': 80.0,
            'temperature': 75.0,
            'ai_hat_usage': 90.0
        }
        self.alert_history = []
    
    def check_alerts(self, metrics: SystemMetrics) -> List[str]:
        """Check for alert conditions"""
        alerts = []
        
        if metrics.cpu_usage > self.thresholds['cpu_usage']:
            alerts.append(f"High CPU usage: {metrics.cpu_usage:.1f}%")
        
        if metrics.temperature > self.thresholds['temperature']:
            alerts.append(f"High temperature: {metrics.temperature:.1f}°C")
        
        if alerts:
            self.alert_history.extend(alerts)
            self._notify_alerts(alerts)
        
        return alerts
    
    def _notify_alerts(self, alerts: List[str]):
        """Send alert notifications"""
        for alert in alerts:
            logging.warning(f"ALERT: {alert}")
```

## Implementation Guidelines

For AI-assisted development:

1. **Metric Processing**
   ```python
   class MetricProcessor:
       """Process and analyze metrics"""
       def __init__(self, window_size: int = 60):
           self.window_size = window_size
           self.metrics_window = deque(maxlen=window_size)
       
       def process_metrics(self, 
                         metrics: SystemMetrics) -> Dict[str, float]:
           """Process current metrics"""
           self.metrics_window.append(metrics)
           
           return {
               'cpu_avg': self._calculate_average('cpu_usage'),
               'memory_avg': self._calculate_average('memory_usage'),
               'temp_avg': self._calculate_average('temperature'),
               'ai_hat_avg': self._calculate_average('ai_hat_usage')
           }
       
       def _calculate_average(self, metric_name: str) -> float:
           """Calculate moving average for metric"""
           values = [getattr(m, metric_name) 
                    for m in self.metrics_window]
           return sum(values) / len(values)
   ```

2. **Data Visualization**
   ```python
   class MetricVisualizer:
       """Visualize system metrics"""
       def __init__(self):
           self.fig, self.ax = plt.subplots(2, 2)
           self.line_plots = self._setup_plots()
       
       def _setup_plots(self):
           """Setup visualization plots"""
           plots = {
               'cpu': self.ax[0, 0].plot([], [])[0],
               'memory': self.ax[0, 1].plot([], [])[0],
               'temp': self.ax[1, 0].plot([], [])[0],
               'ai_hat': self.ax[1, 1].plot([], [])[0]
           }
           
           self.ax[0, 0].set_title('CPU Usage')
           self.ax[0, 1].set_title('Memory Usage')
           self.ax[1, 0].set_title('Temperature')
           self.ax[1, 1].set_title('AI HAT Usage')
           
           return plots
       
       def update_plots(self, metrics: List[SystemMetrics]):
           """Update visualization with new data"""
           times = [m.timestamp for m in metrics]
           
           self.line_plots['cpu'].set_data(
               times, [m.cpu_usage for m in metrics])
           self.line_plots['memory'].set_data(
               times, [m.memory_usage for m in metrics])
           self.line_plots['temp'].set_data(
               times, [m.temperature for m in metrics])
           self.line_plots['ai_hat'].set_data(
               times, [m.ai_hat_usage for m in metrics])
           
           plt.draw()
   ```

3. **Error Handling**
   ```python
   class MonitoringSystem:
       """Main monitoring system"""
       def __init__(self):
           self.collector = MetricCollector()
           self.processor = MetricProcessor()
           self.logger = PerformanceLogger()
           self.alerts = AlertSystem()
       
       async def run(self):
           """Run monitoring system"""
           try:
               while True:
                   # Collect metrics
                   metrics = self.collector.collect_metrics()
                   
                   # Process and analyze
                   processed = self.processor.process_metrics(metrics)
                   
                   # Check for alerts
                   alerts = self.alerts.check_alerts(metrics)
                   
                   # Log results
                   self.logger.log_metrics(metrics)
                   
                   await asyncio.sleep(1)
           except Exception as e:
               logging.error(f"Monitoring error: {e}")
               self._handle_error(e)
   ```

## Performance Analysis

### 1. Trend Analysis

```python
class TrendAnalyzer:
    """Analyze metric trends"""
    def analyze_trends(self,
                      metrics: List[SystemMetrics]) -> Dict[str, float]:
        """Analyze metric trends"""
        return {
            'cpu_trend': self._calculate_trend(
                [m.cpu_usage for m in metrics]),
            'memory_trend': self._calculate_trend(
                [m.memory_usage for m in metrics]),
            'temp_trend': self._calculate_trend(
                [m.temperature for m in metrics])
        }
    
    def _calculate_trend(self, values: List[float]) -> float:
        """Calculate trend direction"""
        if len(values) < 2:
            return 0.0
        return (values[-1] - values[0]) / len(values)
```

## Related Documentation
- [Hardware Configuration](configuration.md)
- [Performance Optimization](optimization.md)
- [Training Pipeline](../ai-system/training-pipeline.md)

## Version History
- v1.0: Initial monitoring system
- v1.1: Added visualization
- v1.2: Enhanced trend analysis
