# Backup and restore strategy — planning guide

Backups are useful only if they can be restored. The Compose example includes a PostgreSQL named volume, but **does not install scheduled backups**. Redis is used as a disposable cache without a persistence volume.

## Include in a real backup plan

- PostgreSQL logical dumps or an application-consistent backup process
- Application uploads and data volumes, if introduced later
- Sanitized Compose and reverse-proxy configurations
- Encrypted off-device copy with restricted access
- A retention policy and periodic restore test

## PostgreSQL lab-only example (Linux shell)

The following illustrates a logical dump in an **isolated disposable lab**, not an automated production solution. Run from the repository root after confirming the database is initialized:

```bash
mkdir -p backups
chmod 700 backups
docker compose -f docker-compose.example.yml exec -T postgres   pg_dump -U lab_user -d lab_db --no-owner --no-acl > backups/lab_db.sql
chmod 600 backups/lab_db.sql
```

Do not run the redirection example unchanged in **Windows PowerShell 5.1**, where output encoding behavior can differ. Never commit `backups/` or upload raw dumps: they can contain sensitive information.

## Restore rehearsal

1. On a disposable test stack, create a **different empty test database**, such as `lab_db_restore`.
2. Import the dump into the empty database, never over the active database.
3. Verify sample rows, schema and application behavior against expectations.
4. Record the elapsed time, required permissions and any failure without exposing dataset contents.
5. Delete test data only after successful verification and explicit approval.

Plan a separate recovery procedure for Docker volumes, backup encryption, off-device copies and lost credentials. Do not mistake a successful dump command for proof of recoverability.
