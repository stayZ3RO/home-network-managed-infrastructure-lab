# Phase 1 — Screenshots

![Status](https://img.shields.io/badge/Status-Evidence%20Linked-brightgreen)
![Phase](https://img.shields.io/badge/Phase-1%20Managed%20Cutover-purple)
![Security](https://img.shields.io/badge/Security-Sanitized%20Docs-red)
![Docs](https://img.shields.io/badge/Docs-Portfolio%20Ready-informational)

## Sanitized Screenshot Evidence for the Managed Network Cutover

---

## Overview

This document links the sanitized screenshot evidence captured during Phase 1.

These screenshots validate that the managed router/switch cutover was completed successfully and that core services remained operational after the change.

---

## Screenshot Evidence Table

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

## Screenshot Gallery

### ER605 WAN Online

![ER605 WAN Online](../../screenshots/phase-1-managed-network-cutover/02-er605-wan-online.png)

**Category:** Router / Gateway  
**Purpose:** Confirms the ER605 WAN interface came online after the cutover.

---

### ER605 LAN DHCP Configuration

![ER605 LAN DHCP Configuration](../../screenshots/phase-1-managed-network-cutover/03-er605-lan-dhcp-config.png)

**Category:** DHCP  
**Purpose:** Shows the LAN DHCP configuration now controlled by the ER605.

---

### ER605 Address Reservations

![ER605 Address Reservations](../../screenshots/phase-1-managed-network-cutover/04-er605-address-reservations.png)

**Category:** DHCP  
**Purpose:** Documents DHCP reservations for infrastructure devices.

---

### Managed Switch Online in Omada

![Managed Switch Online in Omada](../../screenshots/phase-1-managed-network-cutover/05-managed-switch-online-in-omada.png)

**Category:** Managed Switch  
**Purpose:** Confirms the managed switch is visible and online in Omada.

---

### Managed Switch Port Map

![Managed Switch Port Map](../../screenshots/phase-1-managed-network-cutover/06-managed-switch-port-map.png)

**Category:** Managed Switch  
**Purpose:** Shows active switch ports and physical connectivity.

---

### PoE Status for Pi Nodes

![PoE Status for Pi Nodes](../../screenshots/phase-1-managed-network-cutover/07-poe-status-pi-nodes.png)

**Category:** Power / Switching  
**Purpose:** Shows PoE status for infrastructure nodes connected to the managed switch.

---

### Wired Client DHCP from ER605

![Wired Client DHCP from ER605](../../screenshots/phase-1-managed-network-cutover/10-wired-client-dhcp-from-er605.png)

**Category:** Client Validation  
**Purpose:** Confirms a wired client received DHCP from the ER605-controlled network.

---

### Wi-Fi Client DHCP from ER605

![Wi-Fi Client DHCP from ER605](../../screenshots/phase-1-managed-network-cutover/11-wifi-client-dhcp-from-er605.png)

**Category:** Wireless Validation  
**Purpose:** Confirms a wireless client received DHCP from the ER605 while Deco operated in AP mode.

---

### Pi-hole Queries After Cutover

![Pi-hole Queries After Cutover](../../screenshots/phase-1-managed-network-cutover/13-pihole-queries-after-cutover.png)

**Category:** DNS  
**Purpose:** Shows Pi-hole receiving queries after the managed network cutover.

---

### HA DNS VIP Reachable After Cutover

![HA DNS VIP Reachable After Cutover](../../screenshots/phase-1-managed-network-cutover/14-ha-dns-vip-reachable-after-cutover.png)

**Category:** DNS High Availability  
**Purpose:** Confirms the high-availability DNS virtual IP remained reachable.

---

### Proxmox Access After Cutover

![Proxmox Access After Cutover](../../screenshots/phase-1-managed-network-cutover/15-proxmox-access-after-cutover.png)

**Category:** Infrastructure  
**Purpose:** Confirms Proxmox remained reachable after the cutover.

---

### Grafana Access After Cutover

![Grafana Access After Cutover](../../screenshots/phase-1-managed-network-cutover/16-grafana-access-after-cutover.png)

**Category:** Monitoring  
**Purpose:** Confirms Grafana remained reachable after the cutover.

---

### Omada Controller After Cutover

![Omada Controller After Cutover](../../screenshots/phase-1-managed-network-cutover/17-omada-controller-after-cutover.png)

**Category:** Management  
**Purpose:** Confirms Omada Controller remained accessible after the cutover.

---

### RustDesk Access After Cutover

![RustDesk Access After Cutover](../../screenshots/phase-1-managed-network-cutover/18-rustdesk-access-after-cutover.png)

**Category:** Remote Access  
**Purpose:** Confirms private remote access remained available after the cutover.

---

### Final Omada Topology and Client List

![Final Omada Topology and Client List](../../screenshots/phase-1-managed-network-cutover/20-final-omada-topology-client-list.png)

**Category:** Topology  
**Purpose:** Shows final managed network visibility after the cutover.


---

## Sanitization Notes

Before publishing screenshots, redact:

- Public WAN IP addresses
- MAC addresses
- Serial numbers
- Hostnames that identify personal devices
- Email addresses
- Tailscale device names if sensitive
- API keys, tokens, and authentication strings
- Any private domain or account information that should not be public

---

## Screenshot Folder

```text
screenshots/phase-1-managed-network-cutover/
```
