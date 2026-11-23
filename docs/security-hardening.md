# Host hardening — review checklist (not applied automatically)

## SSH

- Use key-based authentication and disable root password login after confirming an alternative administrative path.
- Limit management access to a trusted LAN or VPN when appropriate.
- Test a second active SSH session and a recovery path **before** changing remote access policy.
- Keep packages and firmware updated on a documented schedule.

## Firewall and Docker

- Start from an inventory of deliberately exposed services and host interfaces.
- This lab publishes only `127.0.0.1:8080` for local HTTP testing. No database/cache ports are published.
- Docker port publishing can bypass assumptions about host firewall rules; validate host rules and actual exposure together.
- Do not blindly run example UFW commands on a remote server: an incorrect rule can lock out SSH access.

## Secrets and updates

- Do not commit `.env`, private keys, tokens, database dumps or real IP/domain configurations.
- Use a different, unique PostgreSQL password in each lab environment. The Compose file refuses missing/empty passwords.
- Image tags here are examples, not immutable version pins. Review updates and use digests for deployment reproducibility.
- Redis has no authentication in this isolated lab example. Never expose it to untrusted networks.
