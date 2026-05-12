# Phase 1 — Managed Router/Switch Cutover

![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Phase](https://img.shields.io/badge/Phase-1%20Managed%20Cutover-purple)
![Docs](https://img.shields.io/badge/Docs-Portfolio%20Ready-informational)

## Phase 1 Documentation Index and Evidence Summary

---

## Overview

Phase 1 documents the migration from a consumer mesh/router-controlled network to a managed network foundation using a dedicated router/firewall, managed switch, Omada SDN Controller, AP-mode wireless, redundant DNS, monitoring, and post-cutover validation.

The purpose of this phase was to complete the managed router/switch cutover first, confirm all core services survived the change, and create a stable baseline before introducing VLAN segmentation.

---

## Documentation Index

| Document | Purpose |
|---|---|
| [Overview](overview.md) | Explains the purpose, target state, and final result of Phase 1 |
| [Implementation](implementation.md) | Documents the cutover process and major implementation steps |
| [Validation](validation.md) | Captures post-cutover validation checks and results |
| [Screenshots](screenshots.md) | Links sanitized screenshot evidence for Phase 1 |
| [Diagrams](diagrams.md) | Links physical, logical, DNS, and monitoring diagrams |
| [Rollback Plan](rollback-plan.md) | Documents the recovery strategy if the cutover failed |
| [Lessons Learned](lessons-learned.md) | Summarizes operational takeaways from the cutover |

---

## Phase 1 Result

| Area | Result |
|---|---:|
| ER605 router/firewall cutover | ✅ Complete |
| TL-SG2210P managed switch integration | ✅ Complete |
| Deco AP mode migration | ✅ Complete |
| DHCP validation | ✅ Passed |
| DNS validation through Pi-hole VIP | ✅ Passed |
| Pi-hole HA DNS availability | ✅ Passed |
| Proxmox service reachability | ✅ Passed |
| Grafana monitoring access | ✅ Passed |
| Omada Controller access | ✅ Passed |
| RustDesk remote access | ✅ Passed |
| Rollback required | ❌ No |

---

## Evidence Summary

| Evidence | Category | Status | Purpose |
|---|---|---:|---|
| [ER605 WAN Online](../../screenshots/phase-1-managed-network-cutover/02-er605-wan-online.png) | Router / Gateway | ✅ Linked | Confirms the ER605 WAN interface came online after the cutover. |
| [ER605 LAN DHCP Configuration](../../screenshots/phase-1-managed-network-cutover/03-er605-lan-dhcp-config.png) | DHCP | ✅ Linked | Shows the LAN DHCP configuration now controlled by the ER605. |
| [ER605 Address Reservations](../../screenshots/phase-1-managed-network-cutover/04-er605-address-reservations.png) | DHCP | ✅ Linked | Documents DHCP reservations for infrastructure devices. |
| [Managed Switch Online in Omada](../../screenshots/phase-1-managed-network-cutover/05-managed-switch-online-in-omada.png) | Managed Switch | ✅ Linked | Confirms the managed switch is visible and online in Omada. |
| [Managed Switch Port Map](../../screenshots/phase-1-managed-network-cutover/06-managed-switch-port-map.png) | Managed Switch | ✅ Linked | Shows active switch ports and physical connectivity. |
| [PoE Status for Pi Nodes](../../screenshots/phase-1-managed-network-cutover/07-poe-status-pi-nodes.png) | Power / Switching | ✅ Linked | Shows PoE status for infrastructure nodes connected to the managed switch. |
| [Wired Client DHCP from ER605](../../screenshots/phase-1-managed-network-cutover/10-wired-client-dhcp-from-er605.png) | Client Validation | ✅ Linked | Confirms a wired client received DHCP from the ER605-controlled network. |
| [Wi-Fi Client DHCP from ER605](../../screenshots/phase-1-managed-network-cutover/11-wifi-client-dhcp-from-er605.png) | Wireless Validation | ✅ Linked | Confirms a wireless client received DHCP from the ER605 while Deco operated in AP mode. |
| `screenshots/phase-1-managed-network-cutover/12-dns-validation-pi-hole-vip.png` | DNS | ⏳ Missing | Confirms DNS resolution through the Pi-hole virtual IP. |
| [Pi-hole Queries After Cutover](../../screenshots/phase-1-managed-network-cutover/13-pihole-queries-after-cutover.png) | DNS | ✅ Linked | Shows Pi-hole receiving queries after the managed network cutover. |
| [HA DNS VIP Reachable After Cutover](../../screenshots/phase-1-managed-network-cutover/14-ha-dns-vip-reachable-after-cutover.png) | DNS High Availability | ✅ Linked | Confirms the high-availability DNS virtual IP remained reachable. |
| [Proxmox Access After Cutover](../../screenshots/phase-1-managed-network-cutover/15-proxmox-access-after-cutover.png) | Infrastructure | ✅ Linked | Confirms Proxmox remained reachable after the cutover. |
| [Grafana Access After Cutover](../../screenshots/phase-1-managed-network-cutover/16-grafana-access-after-cutover.png) | Monitoring | ✅ Linked | Confirms Grafana remained reachable after the cutover. |
| [Omada Controller After Cutover](../../screenshots/phase-1-managed-network-cutover/17-omada-controller-after-cutover.png) | Management | ✅ Linked | Confirms Omada Controller remained accessible after the cutover. |
| [RustDesk Access After Cutover](../../screenshots/phase-1-managed-network-cutover/18-rustdesk-access-after-cutover.png) | Remote Access | ✅ Linked | Confirms private remote access remained available after the cutover. |
| [Final Omada Topology and Client List](../../screenshots/phase-1-managed-network-cutover/20-final-omada-topology-client-list.png) | Topology | ✅ Linked | Shows final managed network visibility after the cutover. |

---

## Diagram Summary

| Diagram | Status | Purpose |
|---|---:|---|
| `diagrams/phase-1-managed-network-cutover/physical-topology.png` | ⏳ Pending | Shows ISP handoff, AT&T Gateway, ER605, managed switch, APs, and infrastructure devices. |
| `diagrams/phase-1-managed-network-cutover/logical-topology.png` | ⏳ Pending | Shows routing, DNS, DHCP, monitoring, and management relationships. |
| `diagrams/phase-1-managed-network-cutover/dns-resolution-flow.png` | ⏳ Pending | Shows client DNS path through Pi-hole VIP, active Pi-hole node, and Unbound. |
| `diagrams/phase-1-managed-network-cutover/monitoring-flow.png` | ⏳ Pending | Shows Prometheus, Grafana, Alertmanager, and alerting flow. |

---

## Next Phase

Phase 2 will introduce VLAN segmentation, subnet planning, firewall policy, and SSID-to-VLAN mapping.
