# Phase 1: Implementation

![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Phase](https://img.shields.io/badge/Phase-1%20Managed%20Cutover-purple)
![Routing](https://img.shields.io/badge/Routing-ER605-informational)
![Switching](https://img.shields.io/badge/Switching-Managed%20PoE%20Switch-informational)
![Platform](https://img.shields.io/badge/Platform-Proxmox-orange)

## Implementation Steps for the Router, Switch, AP Mode, and Core Services Cutover

---

## Objective

Implement the managed network foundation by cutting over from the previous consumer router-based topology to a dedicated router, managed switch, and AP-mode wireless design.

---

## Devices Involved

| Device | Role |
|---|---|
| AT&T Gateway | ISP gateway using IP Passthrough |
| TP-Link ER605 | Main router/firewall |
| TP-Link TL-SG2210P | Managed switch |
| Deco Mesh | Wireless access points in AP mode |
| Omada Controller | Central network management |
| Raspberry Pi 3B+ | Primary DNS node |
| Raspberry Pi 3B | Secondary DNS node |
| Proxmox Host | Virtualization host for infrastructure services |

---

## Pre-Cutover Preparation

Before beginning the cutover, the following items were prepared:

- Verified existing internet connectivity
- Confirmed AT&T gateway IP Passthrough configuration
- Confirmed ER605 was ready for WAN handoff
- Confirmed Omada Controller was reachable
- Confirmed managed switch was ready
- Confirmed Pi-hole nodes were functional
- Confirmed DNS virtual IP was active
- Confirmed monitoring stack was online
- Confirmed remote access path was available
- Identified rollback path if cutover failed

---

## Cutover Steps

### 1. Confirm ISP Handoff

Verified the ISP path:

```text
Internet → ONT → AT&T Gateway
```

The AT&T Gateway remained in the network path and was configured for IP Passthrough to allow the ER605 to act as the main router/firewall.

---

### 2. Connect ER605 Router

The ER605 was connected downstream of the AT&T Gateway.

```text
AT&T Gateway → ER605 WAN
```

The ER605 became the primary routing device for the internal network.

---

### 3. Connect Managed Switch

The TL-SG2210P managed switch was connected to the ER605 LAN side.

```text
ER605 LAN → TL-SG2210P Managed Switch
```

This allowed wired infrastructure devices and access points to connect through the managed switching layer.

---

### 4. Move Deco Mesh to AP Mode

The Deco mesh system was moved out of router mode and into AP mode.

This prevented double NAT and allowed the ER605 to control routing and DHCP while the Deco system continued to provide wireless coverage.

---

### 5. Reconnect Core Infrastructure

The following infrastructure devices were connected back into the network:

- Proxmox host
- Primary Pi-hole
- Secondary Pi-hole
- Monitoring VM
- Omada Controller
- Wired clients
- Wireless clients

---

### 6. Validate Core Services

After reconnecting devices, core services were validated:

- DHCP
- DNS
- Internet access
- Pi-hole
- Keepalived virtual IP
- Proxmox
- Grafana
- Prometheus
- Omada Controller
- Wireless access
- Remote access

---

## Final Phase 1 Topology

```text
Internet
   |
ONT
   |
AT&T Gateway
IP Passthrough
   |
TP-Link ER605
Main Router / Firewall
   |
TP-Link TL-SG2210P
Managed Switch
   |
   |-- Deco Mesh APs
   |-- Proxmox Host
   |-- Primary Pi-hole
   |-- Secondary Pi-hole
   |-- Monitoring VM
   |-- Wired Clients
   |-- Wireless Clients
```

---

## Notes

VLANs were intentionally not introduced during this phase.

The purpose of Phase 1 was to complete the managed network cutover and validate that the environment was stable before adding segmentation complexity.
