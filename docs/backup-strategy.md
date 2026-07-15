# Backup strategy

A basic backup plan should include:

1. Database dumps
2. Application uploaded files
3. Docker Compose files
4. Reverse proxy configuration
5. Off-device backup copy
6. Periodic restore test

Example PostgreSQL dump:

```bash
docker exec example-postgres pg_dump -U example_user example_db > backup.sql
```
