# Home Server Infrastructure

Documentation and sanitized configuration examples for a self-hosted Linux server environment.

## Why I built it

A home server is a useful laboratory for learning Linux administration, networking, reverse proxy configuration, containers, VPN access and security hardening.

## Components

- Ubuntu Server / Debian Linux
- Docker Compose
- Caddy reverse proxy
- PostgreSQL
- Redis
- WireGuard VPN
- UFW firewall
- SSH hardening
- Basic backup strategy

## Repository structure

```text
home-server-infrastructure/
├── docker-compose.example.yml
├── caddy/
│   └── Caddyfile.example
└── docs/
    ├── network-diagram.md
    ├── security-hardening.md
    └── backup-strategy.md
```

## Security note

This repository contains only sanitized examples. Do not publish real IP addresses, domains, credentials, private keys, tokens or production configuration files.
