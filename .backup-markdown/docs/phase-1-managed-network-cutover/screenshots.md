# Phase 1 — Screenshots

## Screenshot Checklist

The following screenshots should be captured and sanitized before publishing.

---

## Network Topology

| Screenshot | Status | Notes |
|---|---:|---|
| Physical topology diagram | Needed | Show ISP, gateway, ER605, switch, APs, core devices |
| Logical topology diagram | Needed | Show routing, DNS, DHCP, monitoring flow |
| Omada topology view | Needed | Sanitize MAC addresses and public IPs |

---

## Router / Gateway

| Screenshot | Status | Notes |
|---|---:|---|
| ER605 online/adopted | Needed | Hide public WAN IP |
| WAN status | Needed | Hide public IP |
| LAN settings | Needed | Show sanitized DHCP/DNS config |
| DHCP settings | Needed | Show scope and DNS server if safe |

---

## Managed Switch

| Screenshot | Status | Notes |
|---|---:|---|
| TL-SG2210P online/adopted | Needed | Hide MAC/serial |
| Switch port overview | Needed | Useful for documenting physical layout |
| Port labels | Optional | Good for portfolio clarity |

---

## Wireless

| Screenshot | Status | Notes |
|---|---:|---|
| Deco in AP mode | Needed | Show AP mode enabled |
| Wireless client connected | Optional | Hide device names/MACs |
| Wi-Fi working after cutover | Optional | Useful validation evidence |

---

## DNS

| Screenshot | Status | Notes |
|---|---:|---|
| Pi-hole dashboard after cutover | Needed | Hide client names if needed |
| Query log sample | Optional | Sanitize domains if needed |
| Primary Pi-hole reachable | Needed | |
| Secondary Pi-hole reachable | Needed | |
| VIP reachable | Needed | |

---

## Monitoring

| Screenshot | Status | Notes |
|---|---:|---|
| Grafana dashboard after cutover | Needed | Show targets online |
| Prometheus targets page | Needed | Show core services up |
| Blackbox exporter status | Optional | Good validation evidence |
| Discord alert test | Optional | Only if sanitized |

---

## Remote Access

| Screenshot | Status | Notes |
|---|---:|---|
| Tailscale device list | Optional | Hide device names/IPs if needed |
| Remote access to Grafana/Pi-hole | Optional | Useful if sanitized |

---

## Sanitization Notes

Before publishing screenshots, hide:

- Public WAN IP
- MAC addresses
- Serial numbers
- Hostnames that identify personal devices
- Email addresses
- Tailscale device names if sensitive
- Any API keys, tokens, or auth strings
