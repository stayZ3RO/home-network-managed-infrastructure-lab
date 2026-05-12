# Lessons Learned

![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Project](https://img.shields.io/badge/Project-Managed%20Network%20Infrastructure-blue)
![Phase](https://img.shields.io/badge/Phase-1%20Managed%20Cutover-purple)
![Docs](https://img.shields.io/badge/Docs-Portfolio%20Ready-informational)

## Key Takeaways from the Managed Router/Switch Cutover

---

## Overview

This document summarizes the main lessons learned from Project 2 of the home network infrastructure lab.

Project 2 builds on the previous HA DNS and infrastructure services project by moving the network to a managed router/switch foundation. The main focus of Phase 1 was completing the router/switch cutover, validating services, and preparing the environment for VLAN segmentation.

Detailed Phase 1 notes are available here:

[Phase 1 Lessons Learned](docs/phase-1-managed-network-cutover/lessons-learned.md)

---

## Project-Level Lessons

### 1. Infrastructure projects should be built in phases

The project was stronger because it was separated into phases.

Phase 1 focused only on the managed router/switch cutover and baseline validation. VLAN segmentation was left for a later phase.

This kept the work easier to validate and made the documentation cleaner.

---

### 2. A stable DNS foundation matters before changing the network

The previous HA DNS work made this project safer.

Because Pi-hole, Keepalived, Unbound, and monitoring were already in place, there was a clear set of services to validate after the cutover.

This created a practical before-and-after comparison.

---

### 3. Managed infrastructure improves visibility

Moving to the ER605, TL-SG2210P, and Omada Controller improved visibility into the network.

The managed stack made it easier to confirm:

- Router status
- DHCP behavior
- Switch connectivity
- Port mapping
- Client visibility
- Wireless client behavior
- Infrastructure reachability

---

### 4. AP mode is the right bridge between consumer Wi-Fi and managed routing

Keeping Deco for wireless coverage but moving it into AP mode was a practical design choice.

It allowed the ER605 to become the main router and DHCP authority while still preserving existing wireless coverage.

This reduced routing overlap and prepared the environment for VLAN-aware wireless design later.

---

### 5. Validation evidence matters

Screenshots and validation tables made the project more credible.

The documentation does not just say the cutover worked. It shows evidence that DHCP, DNS, monitoring, management, and remote access remained functional after the change.

---

## What This Project Demonstrates

This project demonstrates practical skills across:

- Network cutover planning
- Managed router deployment
- Managed switch integration
- DHCP validation
- DNS validation
- Pi-hole HA DNS awareness
- AP-mode wireless design
- Proxmox service validation
- Monitoring validation
- Remote access validation
- Rollback planning
- GitHub-based technical documentation

---

## Strongest Portfolio Value

The strongest part of this project is the operational workflow.

It shows more than device configuration. It shows the process of:

1. Planning a change
2. Preparing the environment
3. Performing the cutover
4. Validating the result
5. Capturing evidence
6. Documenting lessons learned
7. Preparing for the next phase

That is closer to real infrastructure work than a simple home network diagram.

---

## Improvements for Future Phases

| Area | Improvement |
|---|---|
| VLAN planning | Define VLANs and subnets before implementation |
| Firewall policy | Build a clear inter-VLAN rule matrix |
| Wireless design | Map SSIDs to VLANs intentionally |
| Monitoring | Update monitoring targets after segmentation |
| Diagrams | Keep diagrams current with each phase |
| Screenshots | Capture validation evidence during every major change |
| Runbooks | Add troubleshooting and rollback procedures for future phases |

---

## Next Focus

The next focus is Phase 2: VLAN segmentation.

The goal is to move from a flat managed network to a segmented design with separate zones for trusted devices, infrastructure, IoT, guest access, and lab systems.
