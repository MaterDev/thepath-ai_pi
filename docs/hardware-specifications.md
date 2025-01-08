# The Path (AI-Pi) Hardware Specifications

## Development Machine
- Apple M1 Mac
- Architecture: ARM64
- ML Acceleration: Metal Performance Shaders (MPS)

## Raspberry Pi 5
### Core Specifications
- Processor: 2.4GHz Quad-Core BCM2712 (ARM Cortex-A76)
- RAM: 8GB LPDDR4X
- PCIe 2.0 x1 interface
- GPU: VideoCore VII
- Display Outputs: Dual 4K HDMI
- Network: 
  - Gigabit Ethernet
  - Wi-Fi 5 (802.11ac)
  - Bluetooth 5.0
- Power Requirements: USB-C, 5V DC

## AI HAT+ (26 TOPS Version)
### Core Specifications
- Neural Processing Unit: Hailo-8
- Performance: 26 TOPS (Tera Operations Per Second)
- Interface: PCIe Gen 3
- Operating Temperature: 0°C to 50°C
- Production Lifetime: Until January 2030

### Key Features
- Fully integrated with Raspberry Pi OS
- Native rpicam-apps support
- Automatic NPU detection
- Compatible with Pi 5's GPIO header
- 16mm stacking header included
- Supports PCIe passthrough

### Performance Characteristics
- Power Efficient for Edge AI
- Optimized for Computer Vision
- Supports Multiple Concurrent Models
- Real-time Processing Capability

## Additional Hardware
### Display
- Touch Screen Display
  - Type: Raspberry Pi Official
  - Interface: DSI

### Camera
- Camera Module 3
  - Sensor: 12MP
  - Video: 4K30
  - Interface: CSI

### CanaKit Starter Pack Components
- Power Supply
- Cooling Solution
- MicroSD Card
- Basic Case
- Necessary Cables

## Operating Environment
### Temperature Management
- Operating Range: 0°C to 50°C
- Recommended Range: 10°C to 40°C
- Thermal Throttling Point: ~80°C

### Power Requirements
- Input Voltage: 5V DC
- Peak Current: Up to 5A
- Recommended PSU: ≥27W

### Physical Specifications
- HAT+ Dimensions: 65mm x 56.5mm
- Mounting: Compatible with Pi 5 Standoffs
- Stacking Height: 16mm (with included header)

## Software Compatibility
### Operating System
- Raspberry Pi OS (64-bit)
- Kernel: 6.1 or later
- Required Firmware: December 2023 or later

### AI Framework Support
- PyTorch
- TensorFlow Lite
- ONNX Runtime
- Hailo SDK

### Development Tools
- Hailo Model Optimizer
- Hailo Runtime
- PCIe Drivers
- GPIO Libraries

## Connectivity
### Available Interfaces
- PCIe Gen 3 (AI HAT+)
- GPIO Headers
- USB 3.0
- USB 2.0
- Ethernet
- Wi-Fi
- Bluetooth

## Notes
1. Temperature monitoring is crucial during AI operations
2. Active cooling recommended for optimal performance
3. Regular firmware updates required
4. PCIe bandwidth shared between AI HAT+ and other devices

## Performance Expectations
### AI Processing
- Inference Time: <500ms target
- Multiple Model Support: Yes
- Concurrent Operations: Supported
- Memory Bandwidth: PCIe Gen 3 x1 (8 GT/s)

### System Resources
- Available RAM: ~6GB (after OS)
- Storage: Dependent on SD card
- Network Bandwidth: Up to 1Gbps

## Maintenance Requirements
1. Regular temperature monitoring
2. Dust removal from cooling system
3. Firmware updates
4. Performance benchmarking
5. System log monitoring

## Hardware Limitations
1. PCIe bandwidth constraints
2. Temperature-dependent performance
3. Power delivery limitations
4. Memory bandwidth considerations

## Future Upgrade Paths
1. Additional cooling solutions
2. Storage expansion
3. Network improvements
4. Case modifications