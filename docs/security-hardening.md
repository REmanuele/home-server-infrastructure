# Security hardening checklist

## SSH

- Disable root login
- Use key-based authentication where possible
- Restrict SSH to LAN/VPN when possible
- Keep the system updated

## Firewall

Example UFW baseline:

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow from 192.168.1.0/24 to any port 22 proto tcp
sudo ufw allow from 10.8.0.0/24 to any port 22 proto tcp
sudo ufw enable
```

## Secrets

- Store secrets in `.env` files not tracked by Git
- Rotate passwords periodically
- Never publish private keys or tokens
