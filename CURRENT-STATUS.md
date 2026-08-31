# Current Status

![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Project](https://img.shields.io/badge/Project-Managed%20Network%20Infrastructure-blue)
![Phase](https://img.shields.io/badge/Phase-1%20Managed%20Cutover-purple)
![Docs](https://img.shields.io/badge/Docs-Portfolio%20Ready-informational)

## Phase 1 Complete: Managed Network Baseline Ready for VLAN Segmentation

---

## Project Status

**Phase 1 is complete.**

This repository currently documents the managed network cutover from a consumer mesh/router-controlled design to a dedicated router, managed switch, AP-mode wireless, and VLAN-ready network foundation.

---

## Completed Work

| Area | Status | Notes |
|---|---:|---|
| ER605 router cutover | ✅ Complete | Router/firewall is now the primary routing device |
| Managed switch integration | ✅ Complete | TL-SG2210P is in the production network path |
| Deco AP mode migration | ✅ Complete | Deco mesh is no longer acting as the router |
| DNS validation | ✅ Complete | Pi-hole HA DNS path remained operational |
| DHCP validation | ✅ Complete | Clients received valid leases |
| Internet validation | ✅ Complete | Wired and wireless clients had internet access |
| Proxmox service validation | ✅ Complete | Proxmox-hosted services remained reachable |
| Monitoring validation | ✅ Complete | Grafana and Prometheus remained available |
| Remote access validation | ✅ Complete | Remote management path remained functional |

---

## Current Architecture

```text
Internet
  ↓
ONT
  ↓
AT&T Gateway / IP Passthrough
  ↓
TP-Link ER605 Router
  ↓
TP-Link TL-SG2210P Managed Switch
  ├── Deco Mesh APs
  ├── Proxmox Host
  ├── Primary Pi-hole
  ├── Secondary Pi-hole
  ├── Wired Clients
  └── Wireless Clients
```

---

## Current Focus

The next focus is **Phase 2: VLAN Segmentation**.

Planned work:

- Define network zones
- Assign VLAN IDs
- Create subnet plan
- Plan DHCP scopes
- Plan firewall rules
- Determine trunk/access port layout
- Prepare SSID-to-VLAN mapping

---

## Why VLANs Were Deferred

VLANs were intentionally deferred until after the router/switch cutover was completed and validated.

This keeps the project clean:

1. Establish a stable managed network baseline.
2. Validate DNS, DHCP, internet, monitoring, and remote access.
3. Introduce segmentation and firewall policy after the baseline is stable.

---

## Next Documentation Tasks

| Task | Status |
|---|---:|
| Add final physical topology diagram | ⏳ Pending |
| Add final logical topology diagram | ⏳ Pending |
| Add sanitized Omada screenshots | ⏳ Pending |
| Add switch port mapping | ⏳ Pending |
| Start VLAN/subnet design | ⏳ Pending |
| Build firewall policy matrix | ⏳ Pending |

---

## Summary

Phase 1 successfully moved the network to a managed infrastructure foundation.

The environment is now ready for VLAN design, segmentation planning, firewall policy work, and SSID-to-VLAN mapping.
