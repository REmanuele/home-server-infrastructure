# Reverse proxy Caddy example

The committed `caddy/Caddyfile.example` contains a deliberately small **HTTP-only** reverse proxy for the lab's `demo-app` service:

```caddyfile
:80 {
    encode gzip
    reverse_proxy demo-app:80
}
```

In the Compose file, port 80 is bound only to `127.0.0.1:8080` on the host. The backend service exists in the same Compose stack and shares the `proxy` network with Caddy.

The prior illustrative upstreams `app:3000` and `immich-server:2283` were not defined in the Compose file; they are intentionally omitted to keep this example internally consistent.

This configuration **does not provide HTTPS**. Public domains, certificates, DNS, identity/access control, proxy request limits, logs and upstream health checks require separate environment-specific configuration and validation. Never copy private hostnames or credentials into the public repository.
