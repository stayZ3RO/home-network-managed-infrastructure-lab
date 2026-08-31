# Claude Code Instructions

Read these first:

1. `CURRENT-STATUS.md`: Phase 1 complete, managed network baseline ready for VLAN segmentation
2. `ROADMAP.md`
3. `LESSONS-LEARNED.md`
4. `CHANGELOG.md`

## Scope

Project 2 of the home network lab: migration from consumer mesh/router to managed router/switch (ER605 + managed PoE switch), Omada SDN Controller, AP-mode wireless, redundant DNS, Proxmox-hosted services. Builds on `home-network-infrastructure-HA-DNS` (Project 1). This repo's own scope stops at the managed baseline. VLAN segmentation, firewall policy, and SSID-to-VLAN mapping are the next phase.

## Directories

`configs/`, `diagrams/`, `docs/`, `screenshots/`

## Rules

- Do not commit unless explicitly instructed.
- Do not modify live network/infrastructure from this repo. It's documentation/portfolio, not a control surface.
- Public-safe repo: never introduce secrets, tokens, private keys, or non-public-safe IPs/hostnames.
