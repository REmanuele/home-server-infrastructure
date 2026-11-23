# WireGuard VPN — planning notes only

**No WireGuard service or key material is included in this repository.** These are topics to document when building a separate, authorized VPN lab:

1. Identify whether peers need access to the host, a dedicated management subnet or individual services.
2. Use a dedicated VPN subnet that does not conflict with the LAN or Docker networks.
3. Generate peer private keys locally and keep them out of Git, logs and screenshots.
4. Restrict inbound UDP and administrative SSH access according to the specific host topology.
5. Review IP forwarding, routes, DNS behavior and firewall rules for each peer.
6. Test both authorized connectivity and denial of unauthorized access; document rollback steps.

Do not infer from this README that a working VPN, encrypted public reverse proxy or remote management channel has been deployed. Only publish sanitized topology descriptions and independently verified procedures.
