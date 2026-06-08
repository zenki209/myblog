---
layout: post
title: "What is a microVM?"
date: 2026-06-08
tags: [microvm, virtualization, security, cloud]
---

Virtual machines in the cloud are designed to isolate workloads. They keep one workload from using all server resources and prevent a compromised application from taking over the entire host.

Traditional VMs are often slow and heavy. They boot full operating system images with many unused drivers and rely on hardware emulation.

Containers are lighter, but they share the host kernel. That means containerized processes can be exposed by a single kernel vulnerability.

MicroVMs are a middle ground. They are real virtual machines using hardware-assisted virtualization, but they run a minimal guest kernel with only the drivers needed for virtual devices.

The main advantage of microVMs over containers is stronger isolation. MicroVMs do not share the host kernel and each one has its own network stack, IP address, and network configuration. That makes them much harder to breach or interfere with each other.

## Key architectural components

- **Virtual Machine Monitor (VMM):** Manages the microVM lifecycle and exposes only the minimal devices needed to run, such as serial consoles, vsock, and virtio devices.
- **Kernel-based Virtual Machine (KVM):** Uses the Linux kernel as a Type-1 hypervisor. The VMM controls VMs through `/dev/kvm` and ioctl calls.
- **Lightweight Guest OS:** Boots the guest kernel directly, without a traditional BIOS or bootloader, which reduces startup overhead.
- **Minimalist Control Plane:** Often exposes a per-instance REST API over a Unix socket so vCPU, memory, and block devices can be configured dynamically.

## References

- https://kerkour.com/ai-wishlist-riscv