# Network diagram — local demonstration

```text
                          Host computer
                     127.0.0.1:8080 (HTTP)
                               |
                         Caddy :80
                               |
                     Docker proxy network
                               |
                         demo-app :80
                      (Nginx default page)

   Separate Docker data network (internal: true)
                |                    |
          PostgreSQL :5432       Redis :6379
          (named volume)         (no host port)
```

These networks are intentionally disconnected: the demo app does not query either database or cache. This diagram does **not** show real public DNS, a WireGuard VPN, or HTTPS deployment.
