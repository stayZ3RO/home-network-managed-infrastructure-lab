# Phase 1 — Diagrams

## Physical Topology

The physical topology shows how network devices are connected.

```text
Internet
   |
ONT
   |
AT&T Gateway
   |
ER605 Router
   |
TL-SG2210P Managed Switch
   |
   |-- Deco AP 1
   |-- Deco AP 2
   |-- Deco AP 3
   |-- Proxmox Host
   |-- Primary Pi-hole
   |-- Secondary Pi-hole
   |-- Wired Clients
```

Recommended file:

```text
assets/diagrams/phase-1/physical-topology.png
```

---

## Logical Topology

The logical topology shows how services interact.

```text
Clients
   |
ER605 DHCP / Gateway
   |
Pi-hole VIP
   |
Active Pi-hole Node
   |
Unbound Recursive DNS
   |
Internet DNS Resolution
```

Recommended file:

```text
assets/diagrams/phase-1/logical-topology.png
```

---

## Monitoring Flow

```text
Prometheus
   |
Scrapes Targets
   |
Grafana Dashboards
   |
Alertmanager
   |
Discord Alerts
```

Recommended file:

```text
assets/diagrams/phase-1/monitoring-flow.png
```

---

## Diagram Goals

The diagrams should clearly show:

- ISP handoff
- AT&T Gateway IP Passthrough
- ER605 as main router/firewall
- TL-SG2210P as managed switch
- Deco operating as APs
- Pi-hole DNS redundancy
- Proxmox infrastructure services
- Monitoring visibility
- Future VLAN-ready foundation
