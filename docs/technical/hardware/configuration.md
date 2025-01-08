# Hardware Configuration

## Overview

This guide covers the hardware setup and configuration for The Path (AI-Pi) project, focusing on:
- Raspberry Pi 5 setup
- AI HAT+ integration
- Performance optimization
- Monitoring setup

## Hardware Requirements

### Core Components

```yaml
raspberry_pi:
  model: "Raspberry Pi 5"
  ram: "8GB"
  storage: "32GB minimum, Class 10 SD card"
  cooling: "Active cooling solution required"

ai_hat:
  model: "AI HAT+"
  compute: "NPU acceleration"
  memory: "Dedicated LPDDR4"
  interface: "40-pin GPIO"

peripherals:
  display: "7-inch touchscreen (optional)"
  power: "5V 3A USB-C power supply"
  network: "Ethernet or WiFi"
```

## Initial Setup

### 1. Operating System

```bash
# Download and flash Raspberry Pi OS
# Recommended: 64-bit Lite version for better performance

# Enable required interfaces
sudo raspi-config
# 1. Enable I2C
# 2. Enable SPI
# 3. Enable GPIO
```

### 2. System Configuration

```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Install required packages
sudo apt install -y \
    python3-pip \
    python3-numpy \
    python3-torch \
    i2c-tools \
    htop \
    git

# Configure GPU memory split
sudo nano /boot/config.txt
# Add/modify:
gpu_mem=128
```

## AI HAT+ Setup

### 1. Hardware Installation

```bash
# Power off
sudo shutdown -h now

# Physical installation steps:
# 1. Align AI HAT+ with GPIO pins
# 2. Secure with standoffs
# 3. Connect cooling solution
# 4. Power on
```

### 2. Driver Installation

```python
# Install AI HAT+ drivers
def setup_ai_hat():
    """Setup AI HAT+ acceleration"""
    try:
        # Install dependencies
        subprocess.run([
            "sudo", "apt", "install", "-y",
            "python3-tflite-runtime"
        ])
        
        # Configure device
        with open("/boot/config.txt", "a") as f:
            f.write("\n# AI HAT+ Configuration\n")
            f.write("dtoverlay=ai-hat-plus\n")
        
        return True
    except Exception as e:
        logger.error(f"AI HAT+ setup failed: {e}")
        return False
```

## Performance Configuration

### 1. CPU Configuration

```python
def optimize_cpu():
    """Configure CPU for AI workloads"""
    try:
        # Set governor to performance
        subprocess.run([
            "sudo", "cpufreq-set", 
            "-g", "performance"
        ])
        
        # Set minimum frequency
        subprocess.run([
            "sudo", "cpufreq-set",
            "-d", "1500000"
        ])
        
        return True
    except Exception as e:
        logger.error(f"CPU optimization failed: {e}")
        return False
```

### 2. Memory Management

```python
def configure_memory():
    """Optimize memory settings"""
    try:
        # Set swappiness
        subprocess.run([
            "sudo", "sysctl", "-w",
            "vm.swappiness=10"
        ])
        
        # Configure transparent hugepages
        subprocess.run([
            "echo", "always", ">",
            "/sys/kernel/mm/transparent_hugepage/enabled"
        ])
        
        return True
    except Exception as e:
        logger.error(f"Memory configuration failed: {e}")
        return False
```

## Implementation Guidelines

For AI-assisted development:

1. **Hardware Detection**
   ```python
   def detect_hardware():
       """Detect and validate hardware configuration"""
       config = {
           'cpu_cores': os.cpu_count(),
           'memory_gb': psutil.virtual_memory().total / 1e9,
           'ai_hat': check_ai_hat_present(),
           'gpu_memory': get_gpu_memory()
       }
       
       # Validate configuration
       validate_hardware_config(config)
       
       return config
   ```

2. **Resource Management**
   ```python
   class ResourceManager:
       """Manage hardware resources"""
       def __init__(self):
           self.cpu_monitor = CPUMonitor()
           self.memory_monitor = MemoryMonitor()
           self.temperature_monitor = TemperatureMonitor()
       
       def check_resources(self) -> bool:
           """Check if resources are available"""
           cpu_ok = self.cpu_monitor.usage < 80
           memory_ok = self.memory_monitor.available > 1e9
           temp_ok = self.temperature_monitor.current < 75
           
           return all([cpu_ok, memory_ok, temp_ok])
   ```

3. **Error Handling**
   ```python
   def safe_hardware_setup():
       """Safely setup hardware components"""
       try:
           # Check hardware compatibility
           if not check_hardware_compatibility():
               raise ValueError("Incompatible hardware")
           
           # Setup components
           setup_ai_hat()
           optimize_cpu()
           configure_memory()
           
           return True
       except Exception as e:
           logger.error(f"Hardware setup failed: {e}")
           return False
   ```

## Monitoring Setup

### 1. System Metrics

```python
@dataclass
class SystemMetrics:
    """System performance metrics"""
    cpu_usage: float
    memory_usage: float
    temperature: float
    ai_hat_usage: float
    
    def to_dict(self) -> dict:
        """Convert to dictionary format"""
        return asdict(self)
    
    def is_healthy(self) -> bool:
        """Check if metrics are within healthy range"""
        return (
            self.cpu_usage < 80 and
            self.memory_usage < 80 and
            self.temperature < 75 and
            self.ai_hat_usage < 90
        )
```

### 2. Logging Configuration

```python
def setup_logging():
    """Configure system logging"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.FileHandler('system.log'),
            logging.StreamHandler()
        ]
    )
```

## Related Documentation
- [Behavior Model](../ai-system/behavior-model.md)
- [Training Pipeline](../ai-system/training-pipeline.md)
- [Performance Optimization](optimization.md)

## Version History
- v1.0: Initial configuration
- v1.1: Added AI HAT+ support
- v1.2: Enhanced monitoring
