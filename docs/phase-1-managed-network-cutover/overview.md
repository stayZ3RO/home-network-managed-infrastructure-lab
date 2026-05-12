# Phase 1 — Managed Router/Switch Cutover and Baseline Validation

## Overview

Phase 1 focused on migrating the home network from a consumer mesh/router-controlled design to a managed network foundation using a dedicated router/firewall, managed switch, Omada Controller, and access points operating in AP mode.

The goal was not to introduce VLANs immediately. The priority was to complete the physical and logical cutover first, then validate that core services remained stable before moving into segmentation.

---

## Why This Phase Was Needed

Before introducing VLANs and firewall policy, the network needed a stable managed foundation.

The previous design relied heavily on the consumer mesh system for routing and wireless coverage. While functional, that design limited visibility, segmentation capability, and enterprise-style network control.

This phase created a clean baseline for:

- Managed routing
- Managed switching
- Future VLAN segmentation
- Centralized network visibility
- Better infrastructure documentation
- Cleaner troubleshooting workflows

---

## Starting State

Before the cutover, the network already had several infrastructure services in place:

- Redundant Pi-hole DNS
- Keepalived DNS virtual IP
- Unbound recursive DNS
- Gravity Sync
- Proxmox-hosted monitoring
- Grafana dashboards
- Prometheus and Blackbox monitoring
- Tailscale remote access
- Omada Controller prepared for managed network hardware

The network was intentionally stabilized before changing the router and switch layer.

---

## Target State

The target Phase 1 topology was:

```text
Internet
   |
ONT
   |
AT&T Gateway
IP Passthrough
   |
TP-Link ER605 Router
   |
TP-Link TL-SG2210P Managed Switch
   |
   |-- Deco Mesh APs
   |-- Proxmox Host
   |-- Pi-hole Primary Node
   |-- Pi-hole Secondary Node
   |-- Wired Clients
   |-- Wireless Clients
```

---

## Phase 1 Objectives

- Cut over routing from the previous consumer router design to the TP-Link ER605
- Place Deco mesh into AP mode
- Bring the managed switch into the production network path
- Preserve DNS availability through the Pi-hole virtual IP
- Validate internet access
- Validate DHCP assignment
- Validate DNS resolution
- Validate Pi-hole functionality
- Validate monitoring visibility
- Validate remote access
- Confirm stable baseline before VLAN segmentation

---

## Completion Criteria

Phase 1 was considered complete after the following were validated:

- Clients received valid DHCP leases
- Clients reached the internet successfully
- DNS resolution worked through the Pi-hole virtual IP
- Primary and secondary DNS nodes remained reachable
- Proxmox services remained reachable
- Grafana and monitoring remained available
- Omada Controller could see/adopt/manage network devices
- Wireless clients connected successfully through Deco AP mode
- No critical services were lost during the cutover
- Rollback was no longer required after stable operation was confirmed

---

## Final Result

The managed network cutover was completed successfully.

The network now has a stable managed foundation using dedicated routing, managed switching, AP-mode wireless, redundant DNS, and infrastructure monitoring. This creates the required baseline for the next phase: VLAN segmentation.
