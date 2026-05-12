# Roadmap

## Overview

This roadmap tracks the progression of the managed network infrastructure lab.

Project 2 starts with a completed managed router/switch cutover and will continue into VLAN segmentation, firewall policy, SSID mapping, and monitoring updates.

---

## Phase 1 - Managed Router/Switch Cutover and Baseline Validation

Status: ✅ Complete

Focus:

- Dedicated router/firewall introduced
- Managed switch introduced
- Deco mesh moved to AP mode
- DNS/DHCP/internet validated
- Monitoring validated
- Remote access validated

Documentation:

- [Phase 1 Overview](docs/phase-1-managed-network-cutover/overview.md)
- [Phase 1 Implementation](docs/phase-1-managed-network-cutover/implementation.md)
- [Phase 1 Validation](docs/phase-1-managed-network-cutover/validation.md)

---

## Phase 2 - VLAN Segmentation

Status: ⏳ Planned

Goals:

- Define VLAN IDs
- Create IP subnet plan
- Separate trusted, guest, IoT, infrastructure, and lab networks
- Document gateway interfaces
- Plan DHCP scopes
- Validate routing per VLAN

---

## Phase 3 - Firewall Policy

Status: ⏳ Planned

Goals:

- Define inter-VLAN access rules
- Restrict IoT and guest access
- Permit required DNS, DHCP, and NTP
- Permit management access only from trusted/admin networks
- Document firewall policy matrix
- Validate allowed and blocked traffic

---

## Phase 4 - Wireless SSID Mapping

Status: ⏳ Planned

Goals:

- Map SSIDs to VLANs
- Separate trusted Wi-Fi, guest Wi-Fi, IoT Wi-Fi, and lab Wi-Fi
- Validate wireless DHCP assignment
- Validate DNS resolution by SSID
- Confirm isolation behavior

---

## Phase 5 - Monitoring and Operations

Status: ⏳ Planned

Goals:

- Update Prometheus targets by VLAN
- Update Grafana dashboards
- Monitor gateway, switch, APs, DNS, and core services
- Document backup and restore procedures
- Build troubleshooting runbooks
- Document final validation screenshots
