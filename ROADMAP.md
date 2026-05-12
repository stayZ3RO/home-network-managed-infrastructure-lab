# Roadmap

## Phase 1 — Managed Router/Switch Cutover and Baseline Validation

Status: Completed

- Dedicated router/firewall introduced
- Managed switch introduced
- Deco mesh moved to AP mode
- DNS/DHCP/internet validated
- Monitoring validated
- Remote access validated

---

## Phase 2 — VLAN Segmentation

Status: Planned

Goals:

- Define VLANs
- Create IP subnet plan
- Separate trusted, guest, IoT, infrastructure, and lab networks
- Document VLAN IDs and gateway interfaces
- Prepare migration plan

---

## Phase 3 — Firewall Policy

Status: Planned

Goals:

- Define inter-VLAN access rules
- Restrict IoT and guest traffic
- Permit required DNS/DHCP/NTP access
- Permit management access only from trusted/admin networks
- Document firewall policy matrix

---

## Phase 4 — Wireless SSID Mapping

Status: Planned

Goals:

- Map SSIDs to VLANs
- Separate trusted Wi-Fi, guest Wi-Fi, and IoT Wi-Fi
- Validate wireless DHCP and DNS per VLAN
- Confirm isolation behavior

---

## Phase 5 — Monitoring and Operations

Status: Planned

Goals:

- Update Prometheus targets by VLAN
- Update Grafana dashboards
- Monitor gateway, switch, APs, DNS, and core services
- Document backup and restore procedures
- Build operational runbooks
