# Home Server Infrastructure — documented lab examples

This repository documents a small **self-hosted Linux laboratory**, including a runnable **local Docker Compose example** and notes on networking, access, backups and security. The configuration is deliberately **not a production deployment** and is not a record of a verified enterprise infrastructure.

## What the Compose example actually runs

| Service | Role | Network | Published port |
|---|---|---|---|
| `caddy` | Local HTTP reverse proxy | `proxy` | `127.0.0.1:8080` |
| `demo-app` | Nginx page for testing the proxy | `proxy` | None |
| `postgres` | Database laboratory service | `data` | None |
| `redis` | Cache laboratory service | `data` | None |

The `data` network is marked `internal: true`. The demo application is intentionally **not connected** to PostgreSQL or Redis. WireGuard, firewall and SSH are *documentation topics*, not installed or configured by this Compose file.

## Quick start — isolated local test only

Requires Docker Engine and Docker Compose. **Do not run this on an Internet-exposed server without a separate review.** The repository can still be read and tested statically without Docker.

```powershell
Copy-Item .env.example .env
notepad .env
```

Replace the empty `POSTGRES_PASSWORD=` value with a new, unique password used only for this lab. Do not paste it into chat, a commit, a screenshot or a shell command. Compose refuses to configure the stack if the variable is empty.

```powershell
docker compose -f docker-compose.example.yml config -q
docker compose -f docker-compose.example.yml up -d
docker compose -f docker-compose.example.yml ps
curl.exe http://127.0.0.1:8080/
```

You should see the Nginx welcome page through Caddy. This is **HTTP on localhost**, not public HTTPS. To stop the containers without deleting named database volumes:

```powershell
docker compose -f docker-compose.example.yml down
```

Avoid `down -v` unless you explicitly intend to delete the lab's named volumes and their data. The example uses generic image tags; pin and review image versions or digests before any serious deployment.

## Validation without Docker

The Python checks use only the standard library and inspect repository consistency, not running services:

```powershell
py -3 -m unittest discover -s tests -p "test_*.py" -v
```

On a machine with Docker Compose, `docker compose -f docker-compose.example.yml config -q` additionally validates configuration expansion. No Docker daemon or container deployment is required for that check. The CI workflow runs both checks; it **does not deploy the stack**.

## Documentation

- [Architecture overview](docs/architecture-overview.md)
- [Network access model](docs/network-access-model.md)
- [Network diagram](docs/network-diagram.md)
- [Reverse proxy Caddy](docs/reverse-proxy-caddy.md)
- [WireGuard VPN notes](docs/wireguard-vpn.md)
- [SSH/firewall hardening notes](docs/security-hardening.md)
- [Security checklist](docs/security-checklist.md)
- [Backup and restore strategy](docs/backup-strategy.md)

## Security and limitations

- Real passwords, tokens, hostnames, public IPs, private keys and customer data must not be committed.
- PostgreSQL and Redis are not exposed through host ports. Redis does not have authentication configured in this example and **must not** be attached to untrusted networks.
- A network marked internal and a localhost port binding are useful laboratory boundaries but are **not a complete security assessment**.
- HTTPS certificates, external DNS, reverse-proxy authentication, off-device backups, VPN setup and firewall policy are not deployed by the example.
- Docker Compose examples and documentation should be validated on a disposable host before adapting them to real services.
