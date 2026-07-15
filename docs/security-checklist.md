# Security Checklist

This checklist summarizes the security decisions used in the home server environment.

## Access control

- SSH disabled for root login
- SSH limited to LAN or VPN access
- Public exposure limited to HTTP/HTTPS and VPN
- Firewall default deny policy

## Network

- WireGuard VPN for private access
- Reverse proxy used for HTTPS termination
- Internal services not directly exposed to the internet

## Services

- Docker Compose for service isolation
- Environment variables for sensitive configuration
- No credentials committed to the repository

## Maintenance

- Regular updates
- Backup strategy
- Log monitoring
- Service status checks
