# Architecture overview

This is a **minimal local lab example**, not a description of a tested production host.

`caddy` and `demo-app` share the `proxy` network. Caddy listens inside the container on port 80 and is published only to the **host loopback** interface at `127.0.0.1:8080`. It forwards HTTP requests to the Nginx demo service on container port 80.

`postgres` and `redis` share a separate Docker `data` network marked `internal: true`. Neither service publishes a host port. The demo app has no database connection, so it is not presenting a functional business application.

PostgreSQL uses the named volume `postgres_data` for persistence. Caddy has `caddy_data` and `caddy_config` volumes. Redis is deliberately a disposable cache example without a persistence volume. For a real deployment, define recovery requirements and service credentials rather than copying this topology blindly.

WireGuard VPN, UFW, SSH restrictions and public HTTPS require host-level administration outside this Compose file. They are documented as planning topics only; **the repository does not configure them automatically**.
