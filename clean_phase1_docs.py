from pathlib import Path
from textwrap import dedent

PHASE_DIR = Path("docs/phase-1-managed-network-cutover")
SCREENSHOT_DIR = Path("screenshots/phase-1-managed-network-cutover")

PHASE_DIR.mkdir(parents=True, exist_ok=True)

BADGES_SCREENSHOTS = """![Status](https://img.shields.io/badge/Status-Evidence%20Linked-brightgreen)
![Phase](https://img.shields.io/badge/Phase-1%20Managed%20Cutover-purple)
![Docs](https://img.shields.io/badge/Docs-Portfolio%20Ready-informational)"""

BADGES_VALIDATION = """![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Phase](https://img.shields.io/badge/Phase-1%20Managed%20Cutover-purple)
![DNS](https://img.shields.io/badge/DNS-Pi--hole%20HA-purple)
![Platform](https://img.shields.io/badge/Platform-Proxmox-orange)
![Docs](https://img.shields.io/badge/Docs-Portfolio%20Ready-informational)"""

BADGES_PHASE = """![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Phase](https://img.shields.io/badge/Phase-1%20Managed%20Cutover-purple)
![Routing](https://img.shields.io/badge/Routing-ER605-informational)
![Switching](https://img.shields.io/badge/Switching-Managed%20PoE%20Switch-informational)
![DNS](https://img.shields.io/badge/DNS-Pi--hole%20HA-purple)"""

SCREENSHOTS = [
    ("02-er605-wan-online.png", "ER605 WAN Online", "Router / Gateway", "Confirms the ER605 WAN interface came online after the cutover."),
    ("03-er605-lan-dhcp-config.png", "ER605 LAN DHCP Configuration", "DHCP", "Shows LAN DHCP configuration now controlled by the ER605."),
    ("04-er605-address-reservations.png", "ER605 Address Reservations", "DHCP", "Documents DHCP reservations for infrastructure devices."),
    ("05-managed-switch-online-in-omada.png", "Managed Switch Online in Omada", "Managed Switch", "Confirms the managed switch is online and visible in Omada."),
    ("06-managed-switch-port-map.png", "Managed Switch Port Map", "Managed Switch", "Shows active switch ports and physical connectivity."),
    ("07-poe-status-pi-nodes.png", "PoE Status for Pi Nodes", "Power / Switching", "Shows PoE status for infrastructure nodes connected to the managed switch."),
    ("10-wired-client-dhcp-from-er605.png", "Wired Client DHCP from ER605", "Client Validation", "Confirms a wired client received DHCP from the ER605-controlled network."),
    ("11-wifi-client-dhcp-from-er605.png", "Wi-Fi Client DHCP from ER605", "Wireless Validation", "Confirms a wireless client received DHCP from the ER605 while Deco operated in AP mode."),
    ("12-dns-validation-pi-hole-vip.png", "DNS Validation Through Pi-hole VIP", "DNS", "Confirms DNS resolution through the Pi-hole virtual IP."),
    ("13-pihole-queries-after-cutover.png", "Pi-hole Queries After Cutover", "DNS", "Shows Pi-hole receiving queries after the managed network cutover."),
    ("14-ha-dns-vip-reachable-after-cutover.png", "HA DNS VIP Reachable After Cutover", "DNS High Availability", "Confirms the HA DNS virtual IP remained reachable."),
    ("15-proxmox-access-after-cutover.png", "Proxmox Access After Cutover", "Infrastructure", "Confirms Proxmox remained reachable after the cutover."),
    ("16-grafana-access-after-cutover.png", "Grafana Access After Cutover", "Monitoring", "Confirms Grafana remained reachable after the cutover."),
    ("17-omada-controller-after-cutover.png", "Omada Controller After Cutover", "Management", "Confirms Omada Controller remained accessible after the cutover."),
    ("18-rustdesk-access-after-cutover.png", "RustDesk Access After Cutover", "Remote Access", "Confirms private remote access remained available after the cutover."),
    ("20-final-omada-topology-client-list.png", "Final Omada Topology and Client List", "Topology", "Shows final managed network visibility after the cutover."),
]

def phase_link(filename):
    return f"../../{SCREENSHOT_DIR.as_posix()}/{filename}"

def existing_items():
    items = []
    for filename, title, category, purpose in SCREENSHOTS:
        if (SCREENSHOT_DIR / filename).exists():
            items.append((filename, title, category, purpose))
    return items

items = existing_items()

def evidence_table():
    rows = [
        "| Evidence | Category | Purpose |",
        "|---|---|---|",
    ]

    for filename, title, category, purpose in items:
        rows.append(f"| [{title}]({phase_link(filename)}) | {category} | {purpose} |")

    return "\n".join(rows)

def gallery():
    blocks = []

    for filename, title, category, purpose in items:
        blocks.append(f"""### {title}

![{title}]({phase_link(filename)})

{purpose}
""")

    return "\n---\n\n".join(blocks)

# screenshots.md - clean evidence-only version
(PHASE_DIR / "screenshots.md").write_text(dedent(f"""\
# Phase 1 — Screenshots

{BADGES_SCREENSHOTS}

## Screenshot Evidence for the Managed Network Cutover

---

## Overview

This page contains screenshot evidence captured after the managed network cutover.

The screenshots validate that routing, switching, DHCP, DNS, monitoring, management access, and remote access remained operational after moving to the ER605 router, managed switch, and AP-mode wireless design.

---

## Evidence Table

{evidence_table()}

---

## Evidence Gallery

{gallery()}
"""), encoding="utf-8")

# validation.md - remove generic notes and keep evidence-focused validation
(PHASE_DIR / "validation.md").write_text(dedent(f"""\
# Phase 1 — Validation

{BADGES_VALIDATION}

## Post-Cutover Validation for DNS, DHCP, Internet, Monitoring, and Remote Access

---

## Objective

Validate that the managed network cutover was successful and that all core services remained operational after moving to the ER605 router, managed switch, and AP-mode wireless design.

---

## Validation Summary

| Validation Area | Status | Evidence |
|---|---:|---|
| ER605 WAN online | ✅ Passed | [ER605 WAN Online]({phase_link("02-er605-wan-online.png")}) |
| ER605 DHCP configuration | ✅ Passed | [ER605 LAN DHCP Configuration]({phase_link("03-er605-lan-dhcp-config.png")}) |
| DHCP reservations | ✅ Passed | [ER605 Address Reservations]({phase_link("04-er605-address-reservations.png")}) |
| Managed switch online | ✅ Passed | [Managed Switch Online in Omada]({phase_link("05-managed-switch-online-in-omada.png")}) |
| Switch port mapping | ✅ Passed | [Managed Switch Port Map]({phase_link("06-managed-switch-port-map.png")}) |
| PoE status for Pi nodes | ✅ Passed | [PoE Status for Pi Nodes]({phase_link("07-poe-status-pi-nodes.png")}) |
| Wired client DHCP | ✅ Passed | [Wired Client DHCP from ER605]({phase_link("10-wired-client-dhcp-from-er605.png")}) |
| Wireless client DHCP | ✅ Passed | [Wi-Fi Client DHCP from ER605]({phase_link("11-wifi-client-dhcp-from-er605.png")}) |
| DNS through Pi-hole VIP | ✅ Passed | [DNS Validation Through Pi-hole VIP]({phase_link("12-dns-validation-pi-hole-vip.png")}) |
| Pi-hole query visibility | ✅ Passed | [Pi-hole Queries After Cutover]({phase_link("13-pihole-queries-after-cutover.png")}) |
| HA DNS VIP reachability | ✅ Passed | [HA DNS VIP Reachable After Cutover]({phase_link("14-ha-dns-vip-reachable-after-cutover.png")}) |
| Proxmox access | ✅ Passed | [Proxmox Access After Cutover]({phase_link("15-proxmox-access-after-cutover.png")}) |
| Grafana access | ✅ Passed | [Grafana Access After Cutover]({phase_link("16-grafana-access-after-cutover.png")}) |
| Omada Controller access | ✅ Passed | [Omada Controller After Cutover]({phase_link("17-omada-controller-after-cutover.png")}) |
| RustDesk remote access | ✅ Passed | [RustDesk Access After Cutover]({phase_link("18-rustdesk-access-after-cutover.png")}) |
| Final Omada visibility | ✅ Passed | [Final Omada Topology and Client List]({phase_link("20-final-omada-topology-client-list.png")}) |

---

## DHCP Validation

DHCP was validated from both wired and wireless clients.

| Client Type | Result | Evidence |
|---|---:|---|
| Wired client | ✅ Passed | [Wired Client DHCP from ER605]({phase_link("10-wired-client-dhcp-from-er605.png")}) |
| Wireless client | ✅ Passed | [Wi-Fi Client DHCP from ER605]({phase_link("11-wifi-client-dhcp-from-er605.png")}) |

---

## DNS Validation

DNS was validated through the Pi-hole high-availability virtual IP.

| Test | Result | Evidence |
|---|---:|---|
| DNS resolution through VIP | ✅ Passed | [DNS Validation Through Pi-hole VIP]({phase_link("12-dns-validation-pi-hole-vip.png")}) |
| Pi-hole receiving queries | ✅ Passed | [Pi-hole Queries After Cutover]({phase_link("13-pihole-queries-after-cutover.png")}) |
| HA DNS VIP reachable | ✅ Passed | [HA DNS VIP Reachable After Cutover]({phase_link("14-ha-dns-vip-reachable-after-cutover.png")}) |

---

## Infrastructure Validation

Core infrastructure services remained reachable after the cutover.

| Service | Result | Evidence |
|---|---:|---|
| Proxmox | ✅ Passed | [Proxmox Access After Cutover]({phase_link("15-proxmox-access-after-cutover.png")}) |
| Grafana | ✅ Passed | [Grafana Access After Cutover]({phase_link("16-grafana-access-after-cutover.png")}) |
| Omada Controller | ✅ Passed | [Omada Controller After Cutover]({phase_link("17-omada-controller-after-cutover.png")}) |
| RustDesk | ✅ Passed | [RustDesk Access After Cutover]({phase_link("18-rustdesk-access-after-cutover.png")}) |

---

## Final Result

Phase 1 was successful.

The network was moved to a managed router/switch foundation while preserving DHCP, DNS, Pi-hole HA DNS, Proxmox access, Grafana monitoring, Omada management, wireless connectivity, and private remote access.

The environment is ready for Phase 2: VLAN segmentation.
"""), encoding="utf-8")

# README.md - clean Phase 1 landing page
(PHASE_DIR / "README.md").write_text(dedent(f"""\
# Phase 1 — Managed Router/Switch Cutover

{BADGES_PHASE}

## Documentation Index and Evidence Summary

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
| [Screenshots](screenshots.md) | Links screenshot evidence for Phase 1 |
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

{evidence_table()}

---

## Next Phase

Phase 2 will introduce VLAN segmentation, subnet planning, firewall policy, and SSID-to-VLAN mapping.
"""), encoding="utf-8")

print(f"Cleaned Phase 1 docs. Linked screenshots found: {len(items)}")
