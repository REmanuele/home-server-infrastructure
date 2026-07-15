# Network diagram

```text
Internet
   |
Router / Firewall
   |
Home Server
   |-- Caddy reverse proxy :80/:443
   |-- Docker network
   |   |-- Web app
   |   |-- PostgreSQL
   |   |-- Redis
   |
   |-- WireGuard VPN
```

## Notes

- Public services should go through the reverse proxy.
- Internal services should not be exposed directly to the internet.
- Administration should be restricted to LAN or VPN.
