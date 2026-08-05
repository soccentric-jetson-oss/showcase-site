# Jetson AGX Orin — Capability Showcase

This repository is the central showcase website for five open-source projects that demonstrate full exploitation of the NVIDIA Jetson AGX Orin's hardware capabilities. Each project follows a three-tier architecture including a Linux kernel driver in C providing direct hardware access, a C++17 gRPC server exposing functionality over the network, and a cross-platform PySide6 desktop GUI for user interaction. The five projects cover machine learning acceleration with Cortex Forge, camera and vision pipelining with Iris Flow, video encode and decode processing with Reel Forge, peripheral bus access with Nexus Bus, and power management with Volt Guard.

## Features

- Showcases five complete open-source projects that demonstrate full exploitation of the Jetson AGX Orin hardware platform
- Implements a consistent three-tier architecture per project with kernel driver, gRPC server, and desktop GUI components
- Demonstrates machine learning acceleration with Cortex Forge using NVDLA v2.0 and PVA v2.0 accelerators
- Demonstrates camera and ISP vision pipelining with Iris Flow using the 16-lane MIPI CSI-2 interface
- Demonstrates hardware video encode and decode processing with Reel Forge supporting H.264, H.265, and AV1 codecs
- Demonstrates unified peripheral bus access with Nexus Bus supporting GPIO, I2C, SPI, UART, and CAN interfaces
- Demonstrates power management and monitoring with Volt Guard supporting 15W to 60W configurable power envelope
- Includes 15 Linux kernel drivers with clean platform abstraction layers for SoC portability
- Includes 15 C++17 gRPC servers with Catch2 unit tests and strict compiler warning enforcement
- Includes 15 PySide6 desktop GUIs with dark theme design and cross-platform compatibility
- All projects have been audited using a 20-category scoring system and achieved scores of 90 percent or higher
- Each repository includes comprehensive documentation with README, CHANGELOG, DEPENDENCIES, and audit reports
- All repositories are CI/CD ready with setup guides for GitHub Actions automation
- Projects are open source under MIT and GPL-2.0 licenses for maximum community adoption and contribution

## Quick Start

### Prerequisites
- Linux operating system (x86_64 for development, aarch64 for target deployment)
- Build tools including make, cmake, gcc or clang, and python3 as needed
- Linux kernel headers for kernel module compilation on target hardware

### Build and Test
```bash
make all      # Build all targets including library, tests, and binaries
make test     # Run the test suite to verify all functionality
make clean    # Clean all build artifacts and temporary files
```

## Repository Structure

| Directory | Contents |
|-----------|----------|
| src/ | Source code for the project |
| include/ | Public API header files |
| lib/ | Userspace library source and headers |
| test/ or tests/ | Unit tests and test utilities |
| proto/ | gRPC protocol buffer definitions |
| packaging/ | Distribution packaging files for deb, rpm, and ipk |
| docs/ | Documentation including Doxygen configuration |

## Project Status

**Version:** 0.1.0 — Initial release
**License:** MIT
**Audit Score:** 90/100 across 20 criteria

## Ecosystem

This project is part of the [Jetson AGX Orin Capability Showcase](https://github.com/soccentric-jetson-oss/soccentric-jetson-oss) — five open-source projects demonstrating full exploitation of NVIDIA's flagship edge AI platform.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. All contributions are welcome.

## License

MIT. See [LICENSE](LICENSE) for details.
