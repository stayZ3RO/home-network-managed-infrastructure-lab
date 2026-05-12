# Phase 1 — Validation

![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Phase](https://img.shields.io/badge/Phase-1%20Managed%20Cutover-purple)
![DNS](https://img.shields.io/badge/DNS-Pi--hole%20HA-purple)
![Platform](https://img.shields.io/badge/Platform-Proxmox-orange)
![Docs](https://img.shields.io/badge/Docs-Portfolio%20Ready-informational)

## Post-Cutover Validation for DNS, DHCP, Internet, Monitoring, and Remote Access

---

## Objective

Validate that the managed network cutover was successful and that all core services remained operational after moving to the ER605 router, managed switch, and AP-mode wireless design.

---

## Validation Summary

| Test | Status | Evidence |
|---|---:|---|
| ER605 WAN online | ✅ Passed | [ER605 WAN Online](../../screenshots/phase-1-managed-network-cutover/02-er605-wan-online.png) |
| ER605 DHCP configuration | ✅ Passed | [ER605 LAN DHCP Configuration](../../screenshots/phase-1-managed-network-cutover/03-er605-lan-dhcp-config.png) |
| DHCP reservations | ✅ Passed | [ER605 Address Reservations](../../screenshots/phase-1-managed-network-cutover/04-er605-address-reservations.png) |
| Managed switch online | ✅ Passed | [Managed Switch Online in Omada](../../screenshots/phase-1-managed-network-cutover/05-managed-switch-online-in-omada.png) |
| Switch port map | ✅ Passed | [Managed Switch Port Map](../../screenshots/phase-1-managed-network-cutover/06-managed-switch-port-map.png) |
| PoE status for Pi nodes | ✅ Passed | [PoE Status for Pi Nodes](../../screenshots/phase-1-managed-network-cutover/07-poe-status-pi-nodes.png) |
| Wired client DHCP | ✅ Passed | [Wired Client DHCP from ER605](../../screenshots/phase-1-managed-network-cutover/10-wired-client-dhcp-from-er605.png) |
| Wireless client DHCP | ✅ Passed | [Wi-Fi Client DHCP from ER605](../../screenshots/phase-1-managed-network-cutover/11-wifi-client-dhcp-from-er605.png) |
| DNS through Pi-hole VIP | ✅ Passed | [DNS Validation Through Pi-hole VIP](../../screenshots/phase-1-managed-network-cutover/12-dns-validation-pi-hole-vip.png) |
| Pi-hole query visibility | ✅ Passed | [Pi-hole Queries After Cutover](../../screenshots/phase-1-managed-network-cutover/13-pihole-queries-after-cutover.png) |
| HA DNS VIP reachability | ✅ Passed | [HA DNS VIP Reachable After Cutover](../../screenshots/phase-1-managed-network-cutover/14-ha-dns-vip-reachable-after-cutover.png) |
| Proxmox access | ✅ Passed | [Proxmox Access After Cutover](../../screenshots/phase-1-managed-network-cutover/15-proxmox-access-after-cutover.png) |
| Grafana access | ✅ Passed | [Grafana Access After Cutover](../../screenshots/phase-1-managed-network-cutover/16-grafana-access-after-cutover.png) |
| Omada Controller access | ✅ Passed | [Omada Controller After Cutover](../../screenshots/phase-1-managed-network-cutover/17-omada-controller-after-cutover.png) |
| RustDesk access | ✅ Passed | [RustDesk Access After Cutover](../../screenshots/phase-1-managed-network-cutover/18-rustdesk-access-after-cutover.png) |
| Final Omada topology/client visibility | ✅ Passed | [Final Omada Topology and Client List](../../screenshots/phase-1-managed-network-cutover/20-final-omada-topology-client-list.png) |

---

## Client Network Validation

### Wired Client

The wired client test confirmed that clients connected to the managed switch received DHCP from the ER605-controlled network.

Evidence:

[Wired Client DHCP from ER605](../../screenshots/phase-1-managed-network-cutover/10-wired-client-dhcp-from-er605.png)

---

### Wireless Client

The wireless client test confirmed that Wi-Fi clients connected through Deco AP mode also received DHCP from the ER605-controlled network.

Evidence:

[Wi-Fi Client DHCP from ER605](../../screenshots/phase-1-managed-network-cutover/11-wifi-client-dhcp-from-er605.png)

---

## DNS Validation

DNS was validated through the Pi-hole HA virtual IP.

Evidence:

- [DNS Validation Through Pi-hole VIP](../../screenshots/phase-1-managed-network-cutover/12-dns-validation-pi-hole-vip.png)
- [Pi-hole Queries After Cutover](../../screenshots/phase-1-managed-network-cutover/13-pihole-queries-after-cutover.png)
- [HA DNS VIP Reachable After Cutover](../../screenshots/phase-1-managed-network-cutover/14-ha-dns-vip-reachable-after-cutover.png)

---

## Infrastructure Validation

Core infrastructure services remained reachable after the cutover.

Evidence:

- [Proxmox Access After Cutover](../../screenshots/phase-1-managed-network-cutover/15-proxmox-access-after-cutover.png)
- [Grafana Access After Cutover](../../screenshots/phase-1-managed-network-cutover/16-grafana-access-after-cutover.png)
- [Omada Controller After Cutover](../../screenshots/phase-1-managed-network-cutover/17-omada-controller-after-cutover.png)
- [RustDesk Access After Cutover](../../screenshots/phase-1-managed-network-cutover/18-rustdesk-access-after-cutover.png)

---

## Final Validation Result

The Phase 1 managed network cutover was successful.

Core infrastructure remained stable after the migration, including DHCP, DNS, Pi-hole HA DNS, Proxmox services, Grafana monitoring, Omada management, wireless access, and RustDesk remote access.

The network is now ready for Phase 2: VLAN segmentation.
