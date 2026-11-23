# Network access model

## Local HTTP example

The only host-published port is `127.0.0.1:8080` -> Caddy container port 80. Requests from another machine on the LAN cannot use this binding directly. It deliberately avoids implying a publicly available website.

Caddy reaches `demo-app:80` over the Docker `proxy` network. PostgreSQL and Redis have no published ports, and are attached only to a separate `data` network with `internal: true`.

## VPN and public access

WireGuard is **not** provided by the example. Do not expose Docker database or Redis ports to implement remote administration. If VPN access is required, create a separate host-level plan with access control, keys and tested routing.

For an Internet-facing service, review HTTPS/TLS, firewall, routing, authentication, proxy headers, updates and threat model. Binding `0.0.0.0` or exposing ports 80/443 changes the exposure significantly and must not be treated as a simple default step.

## Verification checklist

1. Check `docker compose ... config` for port bindings and network membership.
2. Confirm the host has not published database/cache ports.
3. Verify access from host loopback; test any other expected path deliberately.
4. Validate host firewall rules separately. Docker's published ports can interact with host firewall policies in unexpected ways.
