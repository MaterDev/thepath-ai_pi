# Raspberry Pi 5 Hardware Specifications

## Overview

The Raspberry Pi 5 serves as the core computing platform for The Path (AI-Pi), providing the necessary processing power, graphics capabilities, and I/O interfaces for the game system.

## Hardware Specifications

```yaml
Processor:
  model: "Broadcom BCM2712"
  cpu:
    architecture: "Arm Cortex-A76"
    cores: 4
    frequency: "2.4GHz"
    features:
      - "Cryptographic Extension"
      - "512KB per-core L2 caches"
      - "2MB shared L3 cache"

Graphics:
  gpu: "VideoCore VII"
  apis:
    - "OpenGL ES 3.1"
    - "Vulkan 1.2"
  features:
    - "Dual 4Kp60 HDMI with HDR"
    - "4Kp60 HEVC decoder"

Memory:
  type: "LPDDR4X-4267"
  size: "8GB"
  bandwidth: "34.1 GB/s"
  allocation:
    gpu: "1GB reserved"
    system: "7GB available"

Connectivity:
  wifi: "Dual-band 802.11ac"
  bluetooth: "5.0 / BLE"
  ethernet: "Gigabit with PoE+ support"
  usb:
    - "2 × USB 3.0 (5Gbps)"
    - "2 × USB 2.0"

Storage:
  primary: "microSD with SDR104 mode"
  expansion: "PCIe 2.0 x1"

Display_Interfaces:
  hdmi: "2 × 4Kp60 outputs"
  mipi: "2 × 4-lane 1.5Gbps transceivers"

Power:
  input: "5V/5A via USB-C"
  features:
    - "Power Delivery support"
    - "Power button"
    - "Real-time clock (RTC)"
```

## System Configuration

### Memory Management
```bash
# /boot/config.txt
gpu_mem=1024        # Reserve 1GB for GPU
max_framebuffers=2  # For dual display support
over_voltage=6      # For 2.4GHz operation
```

### Power Management
```python
class RPi5PowerManager:
    def __init__(self):
        self.cpu_governors = ['powersave', 'ondemand', 'performance']
        self.current_governor = 'ondemand'
    
    def set_performance_mode(self):
        """Configure for maximum performance"""
        self.set_cpu_governor('performance')
        self.set_gpu_frequency('max')
        self.enable_turbo()
    
    def set_balanced_mode(self):
        """Configure for balanced operation"""
        self.set_cpu_governor('ondemand')
        self.set_gpu_frequency('auto')
        self.disable_turbo()
    
    def set_power_save_mode(self):
        """Configure for power saving"""
        self.set_cpu_governor('powersave')
        self.set_gpu_frequency('min')
        self.disable_turbo()
```

## Performance Monitoring

```python
class RPi5Monitor:
    def __init__(self):
        self.vcgencmd = '/usr/bin/vcgencmd'
    
    def get_system_metrics(self) -> dict:
        """Get comprehensive system metrics"""
        return {
            'cpu': {
                'temperature': self.get_cpu_temp(),
                'frequency': self.get_cpu_freq(),
                'governor': self.get_cpu_governor()
            },
            'gpu': {
                'memory': self.get_gpu_memory(),
                'frequency': self.get_gpu_freq()
            },
            'memory': {
                'total': self.get_memory_total(),
                'available': self.get_memory_available(),
                'gpu_reserved': self.get_gpu_memory_reserved()
            },
            'power': {
                'voltage': self.get_voltage(),
                'throttled': self.get_throttled_state()
            }
        }
    
    def check_thermal_throttling(self) -> bool:
        """Check if system is thermal throttling"""
        return self.get_cpu_temp() > 80  # Celsius
```

## Thermal Management

```yaml
Cooling_Requirements:
  idle_temp_target: "<50°C"
  load_temp_target: "<75°C"
  throttle_temp: "80°C"
  
Recommended_Cooling:
  - "Active cooling fan"
  - "Heatsink on CPU/GPU"
  - "Thermal pads on memory"
```

## Performance Targets

```yaml
CPU_Performance:
  single_thread: "2.4GHz sustained"
  multi_thread: "2.4GHz all cores"
  thermal_limit: "80°C"

GPU_Performance:
  vulkan: "Full 1.2 feature set"
  opengl: "OpenGL ES 3.1"
  display: "Dual 4K@60Hz"

Memory_Performance:
  bandwidth: "34.1 GB/s"
  latency: "<20ns"
  
IO_Performance:
  usb3: "5Gbps per port"
  ethernet: "1Gbps"
  pcie: "5Gbps (PCIe 2.0 x1)"
```

## Production Information
- Model: Raspberry Pi 5 (8GB)
- Production lifetime: Until January 2036
- Compliance: Full list at pip.raspberrypi.com
