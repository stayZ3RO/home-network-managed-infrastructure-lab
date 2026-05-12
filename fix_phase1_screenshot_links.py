from pathlib import Path
from textwrap import dedent

PHASE_DIR = Path("docs/phase-1-managed-network-cutover")
SCREENSHOT_DIR = Path("screenshots/phase-1-managed-network-cutover")
DIAGRAM_DIR = Path("diagrams/phase-1-managed-network-cutover")

PHASE_DIR.mkdir(parents=True, exist_ok=True)
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
DIAGRAM_DIR.mkdir(parents=True, exist_ok=True)

def rel_to_phase(path: Path) -> str:
    return f"../../{path.as_posix()}"

BADGES_COMPLETE = """![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Phase](https://img.shields.io/badge/Phase-1%20Managed%20Cutover-purple)
![Docs](https://img.shields.io/badge/Docs-Portfolio%20Ready-informational)"""

BADGES_SCREENSHOTS = """![Status](https://img.shields.io/badge/Status-Evidence%20Linked-brightgreen)
![Phase](https://img.shields.io/badge/Phase-1%20Managed%20Cutover-purple)
![Security](https://img.shields.io/badge/Security-Sanitized%20Docs-red)
![Docs](https://img.shields.io/badge/Docs-Portfolio%20Ready-informational)"""

BADGES_VALIDATION = """![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Phase](https://img.shields.io/badge/Phase-1%20Managed%20Cutover-purple)
![DNS](https://img.shields.io/badge/DNS-Pi--hole%20HA-purple)
![Platform](https://img.shields.io/badge/Platform-Proxmox-orange)
![Docs](https://img.shields.io/badge/Docs-Portfolio%20Ready-informational)"""

SCREENSHOTS = [
    ("02-er605-wan-online.png", "ER605 WAN Online", "Router / Gateway", "Confirms the ER605 WAN interface came online after the cutover."),
    ("03-er605-lan-dhcp-config.png", "ER605 LAN DHCP Configuration", "DHCP", "Shows the LAN DHCP configuration now controlled by the ER605."),
    ("04-er605-address-reservations.png", "ER605 Address Reservations", "DHCP", "Documents DHCP reservations for infrastructure devices."),
    ("05-managed-switch-online-in-omada.png", "Managed Switch Online in Omada", "Managed Switch", "Confirms the managed switch is visible and online in Omada."),
    ("06-managed-switch-port-map.png", "Managed Switch Port Map", "Managed Switch", "Shows active switch ports and physical connectivity."),
    ("07-poe-status-pi-nodes.png", "PoE Status for Pi Nodes", "Power / Switching", "Shows PoE status for infrastructure nodes connected to the managed switch."),
    ("10-wired-client-dhcp-from-er605.png", "Wired Client DHCP from ER605", "Client Validation", "Confirms a wired client received DHCP from the ER605-controlled network."),
    ("11-wifi-client-dhcp-from-er605.png", "Wi-Fi Client DHCP from ER605", "Wireless Validation", "Confirms a wireless client received DHCP from the ER605 while Deco operated in AP mode."),
    ("12-dns-validation-pi-hole-vip.png", "DNS Validation Through Pi-hole VIP", "DNS", "Confirms DNS resolution through the Pi-hole virtual IP."),
    ("13-pihole-queries-after-cutover.png", "Pi-hole Queries After Cutover", "DNS", "Shows Pi-hole receiving queries after the managed network cutover."),
    ("14-ha-dns-vip-reachable-after-cutover.png", "HA DNS VIP Reachable After Cutover", "DNS High Availability", "Confirms the high-availability DNS virtual IP remained reachable."),
    ("15-proxmox-access-after-cutover.png", "Proxmox Access After Cutover", "Infrastructure", "Confirms Proxmox remained reachable after the cutover."),
    ("16-grafana-access-after-cutover.png", "Grafana Access After Cutover", "Monitoring", "Confirms Grafana remained reachable after the cutover."),
    ("17-omada-controller-after-cutover.png", "Omada Controller After Cutover", "Management", "Confirms Omada Controller remained accessible after the cutover."),
    ("18-rustdesk-access-after-cutover.png", "RustDesk Access After Cutover", "Remote Access", "Confirms private remote access remained available after the cutover."),
    ("20-final-omada-topology-client-list.png", "Final Omada Topology and Client List", "Topology", "Shows final managed network visibility after the cutover."),
]

DIAGRAMS = [
    ("physical-topology.png", "Physical Topology", "Shows ISP handoff, AT&T Gateway, ER605, managed switch, APs, and infrastructure devices."),
    ("logical-topology.png", "Logical Topology", "Shows routing, DNS, DHCP, monitoring, and management relationships."),
    ("dns-resolution-flow.png", "DNS Resolution Flow", "Shows client DNS path through Pi-hole VIP, active Pi-hole node, and Unbound."),
    ("monitoring-flow.png", "Monitoring Flow", "Shows Prometheus, Grafana, Alertmanager, and alerting flow."),
]

def screenshot_status_table():
    rows = [
        "| Evidence | Category | Status | Purpose |",
        "|---|---|---:|---|",
    ]

    for filename, title, category, purpose in SCREENSHOTS:
        path = SCREENSHOT_DIR / filename
        if path.exists():
            link = f"[{title}]({rel_to_phase(path)})"
            status = "✅ Linked"
        else:
            link = f"`{path.as_posix()}`"
            status = "⏳ Missing"
        rows.append(f"| {link} | {category} | {status} | {purpose} |")

    return "\n".join(rows)

def screenshot_gallery():
    blocks = []

    for filename, title, category, purpose in SCREENSHOTS:
        path = SCREENSHOT_DIR / filename
        if path.exists():
            blocks.append(f"""### {title}

![{title}]({rel_to_phase(path)})

**Category:** {category}  
**Purpose:** {purpose}
""")

    if not blocks:
        return "No screenshots are currently linked. Confirm the files exist in `screenshots/phase-1-managed-network-cutover/`."

    return "\n---\n\n".join(blocks)

def diagram_status_table():
    rows = [
        "| Diagram | Status | Purpose |",
        "|---|---:|---|",
    ]

    for filename, title, purpose in DIAGRAMS:
        path = DIAGRAM_DIR / filename
        if path.exists():
            link = f"[{title}]({rel_to_phase(path)})"
            status = "✅ Linked"
        else:
            link = f"`{path.as_posix()}`"
            status = "⏳ Pending"
        rows.append(f"| {link} | {status} | {purpose} |")

    return "\n".join(rows)

def diagram_gallery():
    blocks = []

    for filename, title, purpose in DIAGRAMS:
        path = DIAGRAM_DIR / filename
        if path.exists():
            blocks.append(f"""### {title}

![{title}]({rel_to_phase(path)})

**Purpose:** {purpose}
""")

    if not blocks:
        return "No diagrams are currently linked. Add diagrams to `diagrams/phase-1-managed-network-cutover/` when ready."

    return "\n---\n\n".join(blocks)

# Phase 1 landing page
(PHASE_DIR / "README.md").write_text(dedent(f"""\
# Phase 1 — Managed Router/Switch Cutover

{BADGES_COMPLETE}

## Phase 1 Documentation Index and Evidence Summary

---

## Overview

Phase 1 documents the migration from a consumer mesh/router-controlled network to a managed network foundation using a dedicated router/firewall, managed switch, Omada SDN Controller, AP-mode wireless, redundant DNS, monitoring, and post-cutover validation.

The purpose of this phase was to complete the managed router/switch cutover first, confirm all core services survived the change, and create a stable baseline before introducing VLAN segmentation.

---

## Documentation Index

| Document | Purpose |
|---|---|
| [Overview](overview.md) | Explains the purpose, target state, and final result of Phase 1 |
| [Implementation](implementation.md) | Documents the cutover process and major implementation steps |
| [Validation](validation.md) | Captures post-cutover validation checks and results |
| [Screenshots](screenshots.md) | Links sanitized screenshot evidence for Phase 1 |
| [Diagrams](diagrams.md) | Links physical, logical, DNS, and monitoring diagrams |
| [Rollback Plan](rollback-plan.md) | Documents the recovery strategy if the cutover failed |
| [Lessons Learned](lessons-learned.md) | Summarizes operational takeaways from the cutover |

---

## Phase 1 Result

| Area | Result |
|---|---:|
| ER605 router/firewall cutover | ✅ Complete |
| TL-SG2210P managed switch integration | ✅ Complete |
| Deco AP mode migration | ✅ Complete |
| DHCP validation | ✅ Passed |
| DNS validation through Pi-hole VIP | ✅ Passed |
| Pi-hole HA DNS availability | ✅ Passed |
| Proxmox service reachability | ✅ Passed |
| Grafana monitoring access | ✅ Passed |
| Omada Controller access | ✅ Passed |
| RustDesk remote access | ✅ Passed |
| Rollback required | ❌ No |

---

## Evidence Summary

{screenshot_status_table()}

---

## Diagram Summary

{diagram_status_table()}

---

## Next Phase

Phase 2 will introduce VLAN segmentation, subnet planning, firewall policy, and SSID-to-VLAN mapping.
"""), encoding="utf-8")

# screenshots.md
(PHASE_DIR / "screenshots.md").write_text(dedent(f"""\
# Phase 1 — Screenshots

{BADGES_SCREENSHOTS}

## Sanitized Screenshot Evidence for the Managed Network Cutover

---

## Overview

This document links the sanitized screenshot evidence captured during Phase 1.

These screenshots validate that the managed router/switch cutover was completed successfully and that core services remained operational after the change.

---

## Screenshot Evidence Table

{screenshot_status_table()}

---

## Screenshot Gallery

{screenshot_gallery()}

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
"""), encoding="utf-8")

# validation.md
(PHASE_DIR / "validation.md").write_text(dedent(f"""\
# Phase 1 — Validation

{BADGES_VALIDATION}

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
"""), encoding="utf-8")

# diagrams.md
(PHASE_DIR / "diagrams.md").write_text(dedent(f"""\
# Phase 1 — Diagrams

{BADGES_COMPLETE}

## Physical, Logical, DNS, and Monitoring Diagram References

---

## Overview

This document links Phase 1 architecture diagrams for the managed network cutover.

The diagrams should make the network easy to understand without requiring access to the actual environment.

---

## Diagram Evidence Table

{diagram_status_table()}

---

## Diagram Gallery

{diagram_gallery()}

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
"""), encoding="utf-8")

print("Phase 1 screenshot links updated with actual filenames.")
print("")
print("Screenshot files found:")
for filename, title, _, _ in SCREENSHOTS:
    path = SCREENSHOT_DIR / filename
    print(f"{'FOUND' if path.exists() else 'MISSING'} - {filename}")

print("")
print("Diagram files found:")
for filename, title, _ in DIAGRAMS:
    path = DIAGRAM_DIR / filename
    print(f"{'FOUND' if path.exists() else 'MISSING'} - {filename}")
