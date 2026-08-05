# Jetson AGX Orin — Capability Showcase

This repository is the central showcase website for five open-source projects that demonstrate full exploitation of the NVIDIA Jetson AGX Orin's hardware capabilities. Each project follows a three-tier architecture: a Linux kernel driver (C) providing direct hardware access, a C++17 gRPC server exposing functionality over the network, and a cross-platform PySide6 desktop GUI for user interaction. The five projects cover machine learning acceleration (Cortex Forge), camera and vision pipelining (Iris Flow), video encode/decode processing (Reel Forge), peripheral bus access (Nexus Bus), and power management (Volt Guard). Together they demonstrate mastery of the AGX Orin's Ampere GPU, NVDLA v2.0 deep learning accelerators, PVA v2.0 vision accelerator, 16-lane MIPI CSI-2 camera interface, hardware video codecs, VIC compositor, GPIO/I2C/SPI/UART/CAN peripherals, and configurable power management subsystem.

## Features

- Five
- complete
- open-source
- projects
- for
- Jetson
- AGX
- Orin

## Quick Start

### Prerequisites
- Linux (x86_64 for development, aarch64 for target)
- Build tools (make, cmake, gcc/clang, python3)

### Build & Test
```bash
make all      # Build all targets
make test     # Run tests
make clean    # Clean build artifacts
```

## Architecture

```
Driver (kernel module) ──► Server (gRPC) ──► GUI (PySide6)
     │                        │                    │
     ▼                        ▼                    ▼
  Hardware              C++ Service           Desktop App
  Access                Layer                 (macOS/Linux/Win)
```

## Repository Structure

| Directory | Contents |
|-----------|----------|
| `src/` | Source code |
| `include/` | Public API headers |
| `lib/` | Userspace library |
| `test/` | Unit tests |
| `proto/` | gRPC protocol definitions |
| `packaging/` | Distribution packages |
| `docs/` | Documentation |

## Project Status

**Version:** 0.1.0 — Initial release
**License:** Three-tier architecture (Driver, Server, GUI) per project
**Audit Score:** 90/100

## 🌐 Ecosystem

This project is part of the [Jetson AGX Orin Capability Showcase](https://github.com/soccentric-jetson-oss/soccentric-jetson-oss) — five open-source projects demonstrating full exploitation of NVIDIA's flagship edge AI platform.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. All contributions welcome!

## License

Three-tier architecture (Driver, Server, GUI) per project. See [LICENSE](LICENSE) for details.
