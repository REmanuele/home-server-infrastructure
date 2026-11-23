# Security checklist — checks to perform

These items are **checks for an example lab**, not claims that a real server was audited or secured.

## Docker/Compose

- [ ] PostgreSQL password is set locally in `.env`; `.env` is untracked.
- [ ] No database or Redis port is published to the host.
- [ ] The Caddy demonstration binds only to `127.0.0.1:8080`.
- [ ] Caddy and `demo-app` share only the proxy network.
- [ ] PostgreSQL and Redis use the isolated data network.
- [ ] `docker compose ... config -q` passes on the target machine.
- [ ] Containers start and the local HTTP route works on a disposable test host.

## Host policies (not configured here)

- [ ] SSH access uses the intended policy with a verified recovery path.
- [ ] Firewall and Docker port exposure have been tested together.
- [ ] VPN peer keys/routes have been reviewed, if a VPN is deployed separately.
- [ ] Regular updates, log review and restore drills are scheduled.

## Publishing

- [ ] No tokens, customer names, real public/private infrastructure identifiers or raw reports are committed.
- [ ] Documentation distinguishes a working local example from planning notes.
- [ ] Backups and passwords are not included in issues, screenshots or commits.
