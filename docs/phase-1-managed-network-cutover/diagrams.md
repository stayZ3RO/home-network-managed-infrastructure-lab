# Phase 1 — Diagrams

![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Phase](https://img.shields.io/badge/Phase-1%20Managed%20Cutover-purple)
![Docs](https://img.shields.io/badge/Docs-Portfolio%20Ready-informational)

## Physical, Logical, DNS, and Monitoring Diagram References

---

## Overview

This document links Phase 1 architecture diagrams for the managed network cutover.

The diagrams should make the network easy to understand without requiring access to the actual environment.

---

## Diagram Evidence Table

| Diagram | Status | Purpose |
|---|---:|---|
| `diagrams/phase-1-managed-network-cutover/physical-topology.png` | ⏳ Pending | Shows ISP handoff, AT&T Gateway, ER605, managed switch, APs, and infrastructure devices. |
| `diagrams/phase-1-managed-network-cutover/logical-topology.png` | ⏳ Pending | Shows routing, DNS, DHCP, monitoring, and management relationships. |
| `diagrams/phase-1-managed-network-cutover/dns-resolution-flow.png` | ⏳ Pending | Shows client DNS path through Pi-hole VIP, active Pi-hole node, and Unbound. |
| `diagrams/phase-1-managed-network-cutover/monitoring-flow.png` | ⏳ Pending | Shows Prometheus, Grafana, Alertmanager, and alerting flow. |

---

## Diagram Gallery

No diagrams are currently linked. Add diagrams to `diagrams/phase-1-managed-network-cutover/` when ready.

---

## Physical Topology

```text
Internet
   |
ONT
   |
AT&T Gateway / IP Passthrough
   |
TP-Link ER605 Router
   |
TP-Link TL-SG2210P Managed Switch
   |
   |-- Deco APs
   |-- Proxmox Host
   |-- Primary Pi-hole
   |-- Secondary Pi-hole
   |-- Wired Clients
   |-- Wireless Clients
```

---

## DNS Resolution Flow

```text
Client Device
   |
ER605 DHCP-Provided DNS
   |
Pi-hole HA VIP
   |
Active Pi-hole Node
   |
Unbound Recursive Resolver
   |
Internet DNS Resolution
```

---

## Monitoring Flow

```text
Infrastructure Targets
   |
Prometheus / Blackbox Exporter
   |
Grafana Dashboards
   |
Alertmanager
   |
Discord Alerts
```

---

## Diagram Folder

```text
diagrams/phase-1-managed-network-cutover/
```
