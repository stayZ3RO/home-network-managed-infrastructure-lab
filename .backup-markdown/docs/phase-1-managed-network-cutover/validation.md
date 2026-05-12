# Phase 1 — Validation

## Objective

Validate that the managed network cutover was successful and that all core services remained operational after moving to the ER605 router, managed switch, and AP-mode wireless design.

---

## Validation Summary

| Test | Status | Notes |
|---|---:|---|
| Internet access | Passed | Clients were able to reach external websites |
| DHCP assignment | Passed | Clients received valid LAN IP addresses |
| DNS resolution | Passed | DNS resolved through the Pi-hole virtual IP |
| Pi-hole primary node | Passed | Primary DNS node reachable |
| Pi-hole secondary node | Passed | Secondary DNS node reachable |
| DNS failover | Passed | Keepalived VIP remained functional |
| Unbound recursion | Passed | Recursive DNS remained operational |
| Proxmox access | Passed | Proxmox host reachable |
| Monitoring access | Passed | Grafana/Prometheus reachable |
| Omada Controller | Passed | Controller reachable and managing devices |
| Managed switch | Passed | Switch online and passing traffic |
| Deco AP mode | Passed | Wireless clients connected successfully |
| Remote access | Passed | Remote management path remained available |

---

## Client Network Validation

### DHCP Lease Check

Validated that clients received valid network configuration.

Expected:

```text
IP Address: LAN subnet address
Gateway: ER605 LAN IP
DNS: Pi-hole virtual IP
```

Example Windows validation:

```powershell
ipconfig /all
```

Example Linux/macOS validation:

```bash
ip addr
ip route
cat /etc/resolv.conf
```

---

## Internet Connectivity Test

Validated external connectivity using ping and browser tests.

```bash
ping 1.1.1.1
ping google.com
```

Passing result:

- IP-based ping worked
- DNS-based ping worked
- Browser access worked

---

## DNS Resolution Test

Validated DNS resolution through Pi-hole.

```bash
nslookup google.com
nslookup github.com
```

Expected result:

- Queries resolve successfully
- DNS server points to the Pi-hole virtual IP
- Pi-hole dashboard shows active client queries

---

## Pi-hole Validation

Validated both DNS nodes:

- Primary Pi-hole reachable
- Secondary Pi-hole reachable
- Virtual IP reachable
- Queries visible in Pi-hole dashboard
- Blocklists active
- DNS recursion still working through Unbound

---

## Keepalived VIP Validation

Validated that the DNS virtual IP remained available after the network cutover.

Expected path:

```text
Client DNS → Pi-hole VIP → Active Pi-hole node
```

Validation commands:

```bash
ping <PIHOLE_VIP>
nslookup google.com <PIHOLE_VIP>
```

---

## Proxmox Validation

Validated that the Proxmox host remained reachable after the cutover.

Checks performed:

- Proxmox web UI reachable
- Existing VMs/LXCs reachable
- Omada Controller reachable
- Monitoring VM reachable

---

## Monitoring Validation

Validated that monitoring services remained online.

Checks performed:

- Grafana dashboard accessible
- Prometheus accessible
- Blackbox targets reporting
- Alerting stack online
- Core infrastructure targets visible

---

## Wireless Validation

Validated that wireless clients connected successfully after Deco was moved to AP mode.

Checks performed:

- Clients connected to Wi-Fi
- Clients received DHCP leases from the ER605-controlled network
- Internet access worked
- DNS resolution worked
- No double NAT from Deco router mode

---

## Final Validation Result

The Phase 1 managed network cutover was successful.

Core infrastructure remained stable after the migration, including DNS, DHCP, wireless access, Proxmox services, monitoring, and remote access.

The network is now ready for Phase 2: VLAN segmentation.
