# Home Network Managed Infrastructure Lab

## Overview

This project documents the migration of my home network from a consumer mesh/router-based setup to a managed network infrastructure using a dedicated router/firewall, managed switch, Omada SDN controller, Proxmox-hosted services, redundant DNS, monitoring, and future VLAN-based segmentation.

This is Project 2 in my home infrastructure lab series.

Project 1 focused on building reliable core infrastructure services, including:

- Redundant Pi-hole DNS
- Keepalived virtual IP failover
- Unbound recursive DNS
- Gravity Sync configuration synchronization
- Prometheus, Grafana, Blackbox, and Alertmanager monitoring
- Tailscale remote access
- Proxmox-hosted infrastructure services

Project 2 builds on that foundation by moving the network to managed routing and switching, creating the baseline needed for VLAN segmentation, firewall rules, SSID mapping, and enterprise-style network administration.

---

## Project Goals

- Replace consumer router-based network control with managed routing and switching
- Move the Deco mesh system into access point mode
- Introduce a dedicated Omada-managed router and switch
- Validate DNS, DHCP, internet, monitoring, and remote access after cutover
- Establish a stable baseline before VLAN segmentation
- Document physical and logical topology
- Build a portfolio-ready infrastructure project with real validation evidence

---

## Current Phase

| Phase | Status | Description |
|---|---:|---|
| Phase 1 | Completed | Managed router/switch cutover and baseline validation |
| Phase 2 | Planned | VLAN segmentation design |
| Phase 3 | Planned | Firewall policy and inter-VLAN rules |
| Phase 4 | Planned | Wireless SSID to VLAN mapping |
| Phase 5 | Planned | Monitoring, operations, and documentation refinement |

---

## Hardware Used

| Device | Purpose |
|---|---|
| AT&T Fiber Gateway | ISP handoff / IP Passthrough |
| TP-Link ER605 | Dedicated router/firewall |
| TP-Link TL-SG2210P | Managed PoE switch |
| TP-Link Deco Mesh | Wireless access points in AP mode |
| Raspberry Pi 3B+ | Primary Pi-hole / DNS node |
| Raspberry Pi 3B | Secondary Pi-hole / DNS node |
| Dell OptiPlex Proxmox Host | Virtualization host |
| Proxmox VM/LXC services | Monitoring, Omada Controller, remote access, infrastructure services |

---

## High-Level Topology

```text
Internet
   |
ONT
   |
AT&T Gateway
IP Passthrough Mode
   |
TP-Link ER605 Router
   |
TP-Link TL-SG2210P Managed Switch
   |
   |-- Deco Mesh APs
   |-- Proxmox Host
   |-- Primary Pi-hole
   |-- Secondary Pi-hole
   |-- Wired Clients
   |-- Wireless Clients
```

---

## Documentation

| Section | Description |
|---|---|
| [Phase 1 Overview](docs/phase-1-managed-network-cutover/overview.md) | Summary of the managed network cutover |
| [Phase 1 Implementation](docs/phase-1-managed-network-cutover/implementation.md) | Steps performed during the cutover |
| [Phase 1 Validation](docs/phase-1-managed-network-cutover/validation.md) | Testing and verification results |
| [Rollback Plan](docs/phase-1-managed-network-cutover/rollback-plan.md) | Recovery plan if cutover failed |
| [Lessons Learned](docs/phase-1-managed-network-cutover/lessons-learned.md) | Key takeaways from Phase 1 |
| [Screenshots](docs/phase-1-managed-network-cutover/screenshots.md) | Screenshot evidence checklist |
| [Diagrams](docs/phase-1-managed-network-cutover/diagrams.md) | Physical and logical topology diagrams |

---

## Security Notes

This public documentation intentionally excludes:

- Public IP addresses
- MAC addresses
- Serial numbers
- Full DHCP lease tables
- Authentication tokens
- VPN keys
- Raw configuration exports
- Internal credentials

Private RFC1918 addresses may be shown where useful for lab documentation, but sensitive identifiers are sanitized before publishing.

---

## Skills Demonstrated

- Network infrastructure migration
- Router and switch cutover planning
- DNS and DHCP validation
- Managed switch deployment
- Wireless AP mode conversion
- Infrastructure documentation
- Proxmox-hosted service validation
- Troubleshooting and rollback planning
- Monitoring-aware network operations
- Foundation for VLAN and firewall policy design
