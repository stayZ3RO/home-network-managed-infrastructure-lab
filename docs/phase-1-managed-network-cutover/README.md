# Phase 1: Managed Router/Switch Cutover

![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Phase](https://img.shields.io/badge/Phase-1%20Managed%20Cutover-purple)
![Routing](https://img.shields.io/badge/Routing-ER605-informational)
![Switching](https://img.shields.io/badge/Switching-Managed%20PoE%20Switch-informational)
![DNS](https://img.shields.io/badge/DNS-Pi--hole%20HA-purple)

## Documentation Index and Evidence Summary

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
| [Screenshots](screenshots.md) | Links screenshot evidence for Phase 1 |
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

| Evidence | Category | Purpose |
|---|---|---|
| [ER605 WAN Online](../../screenshots/phase-1-managed-network-cutover/02-er605-wan-online.png) | Router / Gateway | Confirms the ER605 WAN interface came online after the cutover. |
| [ER605 LAN DHCP Configuration](../../screenshots/phase-1-managed-network-cutover/03-er605-lan-dhcp-config.png) | DHCP | Shows LAN DHCP configuration now controlled by the ER605. |
| [ER605 Address Reservations](../../screenshots/phase-1-managed-network-cutover/04-er605-address-reservations.png) | DHCP | Documents DHCP reservations for infrastructure devices. |
| [Managed Switch Online in Omada](../../screenshots/phase-1-managed-network-cutover/05-managed-switch-online-in-omada.png) | Managed Switch | Confirms the managed switch is online and visible in Omada. |
| [Managed Switch Port Map](../../screenshots/phase-1-managed-network-cutover/06-managed-switch-port-map.png) | Managed Switch | Shows active switch ports and physical connectivity. |
| [PoE Status for Pi Nodes](../../screenshots/phase-1-managed-network-cutover/07-poe-status-pi-nodes.png) | Power / Switching | Shows PoE status for infrastructure nodes connected to the managed switch. |
| [Wired Client DHCP from ER605](../../screenshots/phase-1-managed-network-cutover/10-wired-client-dhcp-from-er605.png) | Client Validation | Confirms a wired client received DHCP from the ER605-controlled network. |
| [Wi-Fi Client DHCP from ER605](../../screenshots/phase-1-managed-network-cutover/11-wifi-client-dhcp-from-er605.png) | Wireless Validation | Confirms a wireless client received DHCP from the ER605 while Deco operated in AP mode. |
| [Pi-hole Queries After Cutover](../../screenshots/phase-1-managed-network-cutover/13-pihole-queries-after-cutover.png) | DNS | Shows Pi-hole receiving queries after the managed network cutover. |
| [HA DNS VIP Reachable After Cutover](../../screenshots/phase-1-managed-network-cutover/14-ha-dns-vip-reachable-after-cutover.png) | DNS High Availability | Confirms the HA DNS virtual IP remained reachable. |
| [Proxmox Access After Cutover](../../screenshots/phase-1-managed-network-cutover/15-proxmox-access-after-cutover.png) | Infrastructure | Confirms Proxmox remained reachable after the cutover. |
| [Grafana Access After Cutover](../../screenshots/phase-1-managed-network-cutover/16-grafana-access-after-cutover.png) | Monitoring | Confirms Grafana remained reachable after the cutover. |
| [Omada Controller After Cutover](../../screenshots/phase-1-managed-network-cutover/17-omada-controller-after-cutover.png) | Management | Confirms Omada Controller remained accessible after the cutover. |
| [RustDesk Access After Cutover](../../screenshots/phase-1-managed-network-cutover/18-rustdesk-access-after-cutover.png) | Remote Access | Confirms private remote access remained available after the cutover. |
| [Final Omada Topology and Client List](../../screenshots/phase-1-managed-network-cutover/20-final-omada-topology-client-list.png) | Topology | Shows final managed network visibility after the cutover. |

---

## Next Phase

Phase 2 will introduce VLAN segmentation, subnet planning, firewall policy, and SSID-to-VLAN mapping.
