# Phase 1 — Rollback Plan

![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Phase](https://img.shields.io/badge/Phase-1%20Managed%20Cutover-purple)
![Recovery](https://img.shields.io/badge/Recovery-Rollback%20Plan-red)
![Docs](https://img.shields.io/badge/Docs-Portfolio%20Ready-informational)

## Recovery Plan for Managed Network Cutover Failure Scenarios

---

## Overview

This document outlines the rollback strategy for Phase 1 of the managed network infrastructure lab.

The purpose of the rollback plan was to define a known recovery path in case the router/switch cutover caused a loss of internet access, DHCP, DNS, wireless connectivity, or access to core infrastructure services.

Rollback was not required, but documenting the plan was important because the cutover affected the main network path.

---

## Cutover Risk Areas

The main risk areas during the cutover were:

| Risk Area | Potential Impact |
|---|---|
| WAN handoff issue | ER605 may not receive proper upstream connectivity |
| DHCP failure | Clients may not receive valid IP configuration |
| DNS failure | Clients may have internet connectivity but fail name resolution |
| Wireless AP mode issue | Wi-Fi clients may fail to reconnect properly |
| Managed switch issue | Wired devices may lose network connectivity |
| Core service reachability | Proxmox, Pi-hole, Grafana, and Omada could become unreachable |
| Remote access failure | Tailscale or RustDesk access could be interrupted |

---

## Rollback Triggers

Rollback would have been considered if any of the following occurred:

- Clients could not receive DHCP leases
- Multiple clients lost internet access
- DNS resolution failed through the Pi-hole virtual IP
- The Pi-hole HA DNS VIP became unreachable
- The ER605 could not route traffic properly
- The managed switch failed to pass traffic
- Deco AP mode caused a wireless outage
- Proxmox or infrastructure services became unreachable
- Omada Controller access was lost
- Remote access through Tailscale or RustDesk stopped working

---

## Previous Known-Good Topology

The rollback target was the previous known-good network path.

```text
Internet
   |
ONT
   |
AT&T Gateway
   |
Previous Router / Deco Router Mode
   |
Clients
```

This path would temporarily restore the earlier network design while isolating the issue with the managed router/switch cutover.

---

## Rollback Strategy

The rollback strategy was to remove the new managed network path from production and return routing duties to the previous working setup.

The priority order was:

1. Restore internet access
2. Restore DHCP
3. Restore DNS
4. Restore wireless connectivity
5. Restore access to core services
6. Resume troubleshooting from a stable baseline

---

## Rollback Steps

1. Disconnect the ER605 from the production network path.
2. Reconnect the previous router or Deco router-mode configuration if needed.
3. Confirm the previous router is providing DHCP.
4. Reconnect wired clients to the previous working path.
5. Confirm wireless clients can reconnect.
6. Test internet access from multiple clients.
7. Test DNS resolution.
8. Confirm Pi-hole access.
9. Confirm Proxmox access.
10. Confirm Grafana and monitoring access.
11. Confirm Omada Controller access.
12. Pause further cutover changes until the failure point is identified.

---

## Post-Rollback Validation

If rollback had been required, the following checks would confirm service recovery:

| Validation Check | Expected Result |
|---|---|
| Client DHCP lease | Client receives valid LAN IP |
| Default gateway | Client can reach gateway |
| DNS resolution | External domains resolve successfully |
| Internet access | Browser and ping tests pass |
| Pi-hole access | Dashboard and DNS service reachable |
| Proxmox access | Web UI and hosted services reachable |
| Grafana access | Monitoring dashboard reachable |
| Wireless access | Wi-Fi clients reconnect successfully |
| Remote access | Tailscale or RustDesk access restored |

---

## Final Outcome

Rollback was not required.

The managed network cutover completed successfully, and the environment remained stable after validation.

Phase 1 moved forward with the ER605 as the primary router/firewall, the TL-SG2210P as the managed switch, Deco operating in AP mode, and core services remaining reachable.
