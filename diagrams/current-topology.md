# Current Topology: Managed Network (Omada, flat)

The network as it runs today: a single flat `192.168.68.0/24`, managed by
the Omada Controller, with the Pi-hole HA pair providing DNS behind a
Keepalived VIP.

```mermaid
flowchart TD
    ONT["AT&T Fiber ONT"]
    ER["TP-Link ER605 v2<br/>gateway / firewall, 192.168.68.1<br/>Omada-managed · DHCP + DNS source"]
    SW["TP-Link TL-SG2210P v3<br/>managed PoE switch, 192.168.68.2"]
    DECO["Deco X25, AP mode<br/>main node on switch port 8<br/>other nodes: wireless mesh"]

    ONT -->|IP passthrough| ER
    ER --> SW
    SW -->|port 8| DECO

    subgraph CLUSTER["Proxmox cluster"]
        direction LR
        P1["pve01, .80"]
        P2["pve02, .90"]
        P3["pve03, .70"]
    end
    SW --> CLUSTER

    subgraph SERVICES["Hosted VMs / LXCs"]
        direction TB
        PH["Pi-hole HA<br/>pihole01 .4 · pihole02 .5<br/>Keepalived VIP .20 → client DNS"]
        OC["Omada Controller VM, .3"]
        MON["monitoring .94 · portainer .92<br/>rustdesk .93 · ts-router01 / 02"]
    end
    CLUSTER --> SERVICES

    OC -.->|manages| ER
    OC -.->|manages| SW

    classDef ext fill:#334155,stroke:#94a3b8,color:#f1f5f9
    classDef net fill:#075985,stroke:#38bdf8,color:#e0f2fe
    classDef host fill:#92400e,stroke:#fbbf24,color:#fef3c7
    classDef svc fill:#166534,stroke:#4ade80,color:#dcfce7
    class ONT ext
    class ER,SW,DECO net
    class P1,P2,P3 host
    class PH,OC,MON svc
```

**Single flat `192.168.68.0/24` · VLAN 1 only · no segmentation.** VLAN
segmentation, inter-VLAN firewall policy, and SSID-to-VLAN mapping are the
next phase. A "Target State (UniFi)" variant of this diagram will land with
the router/switch migration. Same layout, with ER605 → UDM Pro (`.1`),
SG2210P → USW-24-PoE (`.2`), Deco unchanged.
