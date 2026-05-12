# Home Network Managed Infrastructure Lab

![Status](https://img.shields.io/badge/Status-Phase%201%20Complete-brightgreen)
![Project](https://img.shields.io/badge/Project-Managed%20Network%20Infrastructure-blue)
![Routing](https://img.shields.io/badge/Routing-TP--Link%20ER605-informational)
![Switching](https://img.shields.io/badge/Switching-Managed%20PoE%20Switch-informational)
![DNS](https://img.shields.io/badge/DNS-Pi--hole%20HA-purple)
![Platform](https://img.shields.io/badge/Platform-Proxmox-orange)

## Managed Router/Switch Cutover, Omada SDN, AP Mode, and VLAN-Ready Network Foundation

This repository documents Project 2 of my home network infrastructure lab: the migration from a consumer mesh/router-controlled network to a managed network foundation using a dedicated router/firewall, managed switch, Omada SDN Controller, AP-mode wireless, redundant DNS, Proxmox-hosted services, and monitoring validation.

Project 1 focused on building reliable core infrastructure services such as HA DNS, Unbound recursive DNS, monitoring, alerting, Tailscale remote access, Proxmox-hosted services, and operational validation.

Project 2 builds on that foundation by moving the network to managed routing and switching, creating the baseline required for VLAN segmentation, firewall policy, SSID-to-VLAN mapping, and enterprise-style network administration.

---

## Quick Links

| Area | Link |
|---|---|
| Current Status | [CURRENT-STATUS.md](CURRENT-STATUS.md) |
| Roadmap | [ROADMAP.md](ROADMAP.md) |
| Changelog | [CHANGELOG.md](CHANGELOG.md) |
| Lessons Learned | [LESSONS-LEARNED.md](LESSONS-LEARNED.md) |
| Phase 1 Documentation | [docs/phase-1-managed-network-cutover/](docs/phase-1-managed-network-cutover/) |
| Architecture Diagrams | [diagrams/](diagrams/) |
| Screenshots | [screenshots/](screenshots/) |
| Config Examples | [configs/](configs/) |

---

## About This Project

This project documents the cutover from a consumer home network design into a more controlled, managed infrastructure model.

The main goal was to move routing and switching responsibilities away from the mesh system and into dedicated network infrastructure while keeping core services stable.

This phase introduced:

- Dedicated routing with TP-Link ER605
- Managed switching with TP-Link TL-SG2210P
- Deco mesh operating in AP mode
- Omada SDN-based device visibility
- Redundant Pi-hole DNS with virtual IP failover
- Proxmox-hosted infrastructure services
- Monitoring validation after the cutover
- A stable baseline for VLAN segmentation

---

## Why I Built This

I built this project to practice the kind of work that sits between service desk, network administration, systems administration, and infrastructure engineering.

Instead of only documenting a working home network, this project focuses on the operational side of infrastructure changes:

- Planning a live network cutover
- Validating DNS, DHCP, internet, and service reachability
- Reducing double NAT and consumer-router limitations
- Preserving monitoring and remote access during topology changes
- Creating a VLAN-ready foundation before introducing segmentation
- Documenting the environment in a clear, professional, portfolio-ready format

---

## Current Architecture Overview

### Physical Network Path

```text
Internet
  ↓
ONT
  ↓
AT&T Gateway / IP Passthrough
  ↓
TP-Link ER605 Router / Firewall
  ↓
TP-Link TL-SG2210P Managed PoE Switch
  ├── Deco Mesh APs
  ├── Proxmox Host
  ├── Primary Pi-hole Node
  ├── Secondary Pi-hole Node
  ├── Wired Clients
  └── Wireless Clients
```

### DNS Resolution Path

```text
Client Device
  ↓
ER605 DHCP-Provided DNS
  ↓
Pi-hole HA VIP
  ↓
Active Pi-hole Node
  ↓
Local Unbound Recursive Resolver
  ↓
Internet DNS Resolution
```

### Monitoring Path

```text
Infrastructure Targets
  ↓
Prometheus / Blackbox Exporter
  ↓
Grafana Dashboards
  ↓
Alertmanager
  ↓
Discord Alerts
```

### Management and Remote Access Path

```text
Admin Endpoint
  ↓
Trusted LAN / Tailscale
  ↓
Proxmox / Omada / Pi-hole / Monitoring Services
```

---

## Completed and Planned Phases

| Phase | Status | Focus |
|---|---:|---|
| Phase 1 - Managed Router/Switch Cutover | ✅ Complete | ER605 cutover, managed switch integration, Deco AP mode, baseline validation |
| Phase 2 - VLAN Segmentation | ⏳ Planned | VLAN IDs, subnet plan, network zones, DHCP scopes |
| Phase 3 - Firewall Policy | ⏳ Planned | Inter-VLAN rules, restricted management access, IoT/guest isolation |
| Phase 4 - Wireless SSID Mapping | ⏳ Planned | SSID-to-VLAN mapping for trusted, guest, IoT, and lab wireless |
| Phase 5 - Monitoring and Operations | ⏳ Planned | Monitoring updates, dashboards, runbooks, backups, validation procedures |

---

## Documentation

### Phase 1 - Managed Router/Switch Cutover

| Document | Link |
|---|---|
| Overview | [View](docs/phase-1-managed-network-cutover/overview.md) |
| Implementation | [View](docs/phase-1-managed-network-cutover/implementation.md) |
| Validation | [View](docs/phase-1-managed-network-cutover/validation.md) |
| Rollback Plan | [View](docs/phase-1-managed-network-cutover/rollback-plan.md) |
| Lessons Learned | [View](docs/phase-1-managed-network-cutover/lessons-learned.md) |
| Screenshots Checklist | [View](docs/phase-1-managed-network-cutover/screenshots.md) |
| Diagrams | [View](docs/phase-1-managed-network-cutover/diagrams.md) |

### Future Phases

| Phase | Link |
|---|---|
| Phase 2 - VLAN Segmentation | [View](docs/phase-2-vlan-segmentation/) |
| Phase 3 - Firewall Policy | [View](docs/phase-3-firewall-policy/) |
| Phase 4 - Wireless SSID Mapping | [View](docs/phase-4-wireless-ssid-mapping/) |
| Phase 5 - Monitoring and Operations | [View](docs/phase-5-monitoring-and-operations/) |

---

## Architecture Diagrams

| Diagram | Status | Link |
|---|---:|---|
| Phase 1 - Physical Topology | Planned | [View](diagrams/phase-1-managed-network-cutover/) |
| Phase 1 - Logical Topology | Planned | [View](diagrams/phase-1-managed-network-cutover/) |
| Phase 1 - DNS Resolution Flow | Planned | [View](diagrams/phase-1-managed-network-cutover/) |
| Phase 1 - Monitoring Flow | Planned | [View](diagrams/phase-1-managed-network-cutover/) |
| Phase 2 - VLAN Segmentation Design | Planned | Coming soon |
| Phase 3 - Firewall Policy Flow | Planned | Coming soon |

---

## Hardware and Lab Systems

| Component | Role |
|---|---|
| AT&T Fiber Connection | WAN connectivity |
| ONT / Optical Network Terminal | Fiber handoff |
| AT&T Gateway with IP Passthrough | ISP gateway |
| TP-Link ER605 | Dedicated router/firewall |
| TP-Link TL-SG2210P | Managed PoE switch |
| TP-Link Deco Mesh | Wireless access points in AP mode |
| Raspberry Pi 3B+ | Primary Pi-hole DNS node |
| Raspberry Pi 3B | Secondary Pi-hole DNS node |
| Dell OptiPlex Proxmox Host | Virtualization host |
| Omada Controller LXC | Network controller |
| Docker Monitoring VM | Monitoring service host |
| Admin Workstation / Laptop | Testing and management endpoint |

---

## Core Tools and Services

| Tool / Service | Purpose |
|---|---|
| Omada SDN Controller | Centralized management for router and switch |
| TP-Link ER605 | Routing, firewalling, DHCP, and WAN handoff |
| TP-Link TL-SG2210P | Managed switching and future VLAN trunk/access ports |
| Pi-hole | DNS filtering and visibility |
| Keepalived | DNS virtual IP failover |
| Gravity Sync | Pi-hole configuration synchronization |
| Unbound | Local recursive DNS resolution |
| Proxmox | Virtualization platform |
| Prometheus | Metrics collection |
| Grafana | Dashboard visualization |
| Blackbox Exporter | Service probing |
| Alertmanager | Alert routing |
| Tailscale | Secure remote administration |
| Docker Compose | Container orchestration |

---

## Phase 1 Validation Summary

| Validation Area | Result |
|---|---:|
| Internet access | ✅ Passed |
| DHCP assignment | ✅ Passed |
| DNS resolution | ✅ Passed |
| Pi-hole HA VIP | ✅ Passed |
| Primary Pi-hole node | ✅ Passed |
| Secondary Pi-hole node | ✅ Passed |
| Unbound recursion | ✅ Passed |
| Proxmox access | ✅ Passed |
| Omada Controller access | ✅ Passed |
| Managed switch connectivity | ✅ Passed |
| Deco AP mode wireless access | ✅ Passed |
| Grafana / Prometheus monitoring | ✅ Passed |
| Remote management access | ✅ Passed |

---

## Security Notes

- Public WAN IP addresses are not published.
- MAC addresses and serial numbers are redacted from screenshots.
- Raw configuration exports are excluded from Git.
- Secrets, tokens, passwords, and private keys are excluded from this repository.
- Management services are intended to remain LAN-only or privately reachable through trusted remote access.
- Screenshots are sanitized before publishing.
- VLAN and firewall policies will be documented in later phases before being treated as complete.

---

## What This Project Demonstrates

This project demonstrates practical infrastructure skills across:

- Network cutover planning
- Managed router deployment
- Managed switch integration
- AP-mode wireless design
- DNS and DHCP validation
- High availability DNS awareness
- Infrastructure monitoring validation
- Proxmox-hosted service continuity
- Network documentation
- Screenshot-based proof of work
- Operational rollback planning
- VLAN-ready network design

---

## Future Work

The next major phase is VLAN segmentation.

Planned work includes:

- Define VLAN IDs
- Build a subnet plan
- Separate trusted, guest, IoT, infrastructure, and lab networks
- Configure VLAN-aware switch ports
- Map SSIDs to VLANs
- Build an inter-VLAN firewall policy matrix
- Validate allowed and denied traffic
- Update monitoring targets after segmentation
- Document final diagrams and screenshots

---

## Goal

To build and document a realistic managed home network infrastructure lab that demonstrates routing, switching, DNS, monitoring, virtualization, secure administration, and future VLAN-based segmentation.
