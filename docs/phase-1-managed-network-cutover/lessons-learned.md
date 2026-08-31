# Phase 1: Lessons Learned

![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Phase](https://img.shields.io/badge/Phase-1%20Managed%20Cutover-purple)
![Docs](https://img.shields.io/badge/Docs-Portfolio%20Ready-informational)

## Operational Takeaways from the Managed Network Cutover

---

## Overview

Phase 1 completed the move from a consumer mesh/router-controlled network to a managed network foundation using a dedicated router/firewall, managed switch, AP-mode wireless, redundant DNS, and post-cutover validation.

The biggest lesson from this phase was that a network cutover is not just a hardware swap. It requires preparation, validation, fallback planning, and proof that dependent services still work after the topology changes.

---

## Key Lessons

### 1. Build a stable baseline before adding VLANs

VLAN segmentation was intentionally deferred.

This was the right decision because it kept the scope of Phase 1 focused on the core network path:

```text
ISP Gateway → ER605 → Managed Switch → Clients / Infrastructure
```

Adding VLANs during the cutover would have introduced more variables and made troubleshooting harder.

---

### 2. DNS must be validated immediately after a routing change

DNS was one of the most important services to validate.

Because the environment uses Pi-hole, Keepalived, and Unbound, the network could appear connected while still failing DNS resolution.

Validating the Pi-hole HA virtual IP confirmed that clients could resolve names after the ER605 and managed switch were placed into the production path.

---

### 3. AP mode simplified the wireless design

Moving Deco into AP mode allowed the ER605 to control routing and DHCP while Deco continued to provide wireless coverage.

This reduced overlap between consumer mesh routing and managed network routing.

It also helped avoid double NAT and made the design easier to reason about before introducing VLANs.

---

### 4. Monitoring is valuable during infrastructure changes

Grafana, Prometheus, and service checks helped confirm that infrastructure services remained reachable after the cutover.

Instead of only testing from a single client, monitoring gave another way to confirm that the broader environment stayed healthy.

---

### 5. Screenshots make the project stronger

Capturing screenshots after the cutover turned the project from a general write-up into evidence-backed documentation.

The most useful screenshots were:

- ER605 WAN online
- ER605 DHCP configuration
- Managed switch online in Omada
- Switch port map
- Wired client DHCP validation
- Wireless client DHCP validation
- Pi-hole DNS validation
- HA DNS VIP reachability
- Proxmox access
- Grafana access
- Omada Controller access
- RustDesk access
- Final Omada topology/client list

---

## What Went Well

| Area | Result |
|---|---|
| Router cutover | ER605 became the primary router/firewall successfully |
| Managed switch integration | TL-SG2210P passed traffic and remained visible in Omada |
| Wireless migration | Deco operated in AP mode successfully |
| DHCP | Wired and wireless clients received valid leases |
| DNS | Pi-hole HA DNS remained operational |
| Monitoring | Grafana remained reachable after the cutover |
| Infrastructure access | Proxmox and Omada remained reachable |
| Remote access | RustDesk access remained functional |
| Rollback | Not required |

---

## What Could Be Improved

| Area | Improvement |
|---|---|
| Screenshot timing | Capture before, during, and after screenshots in future phases |
| Port mapping | Maintain a clean switch port map as devices move |
| Diagrams | Update diagrams immediately after each major topology change |
| Validation log | Keep a short timestamped checklist during the change window |
| Config documentation | Add sanitized DHCP, DNS, and reservation examples where useful |

---

## Operational Takeaway

The cutover worked because the network was changed in layers.

The core services were already stable before the router and switch were moved into the production path. That made it easier to validate the environment after the change and reduced the risk of troubleshooting multiple new systems at once.

---

## Next Phase Considerations

Phase 2 should stay just as controlled.

Before implementing VLANs, the next phase should define:

- VLAN names
- VLAN IDs
- Subnet ranges
- Gateway IPs
- DHCP scopes
- DNS behavior per VLAN
- Switch access ports
- Switch trunk ports
- SSID-to-VLAN mapping
- Inter-VLAN firewall policy

The most important rule for Phase 2 is to validate one segment at a time instead of changing the entire network at once.
