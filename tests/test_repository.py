"""Static checks for the published lab examples (no Docker required)."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


class RepositoryContractTests(unittest.TestCase):
    def setUp(self):
        self.compose = read("docker-compose.example.yml")

    def test_required_password_without_default(self):
        self.assertIn("${POSTGRES_PASSWORD:?", self.compose)
        self.assertNotIn("POSTGRES_PASSWORD: change_me", self.compose)
        self.assertEqual(read(".env.example").split("POSTGRES_PASSWORD=", 1)[-1].strip(), "")

    def test_localhost_only_published_port(self):
        self.assertIn('"127.0.0.1:8080:80"', self.compose)
        self.assertNotIn('"80:80"', self.compose)
        self.assertNotIn('"443:443"', self.compose)

    def test_backend_services_do_not_publish_ports(self):
        # Guardrail against accidental host exposure; Compose CLI performs real parsing in CI.
        for service in ("postgres", "redis"):
            match = re.search(r"(?ms)^  " + service + r":\n(.*?)(?=^  [a-zA-Z0-9_-]+:\n|^volumes:\n)", self.compose)
            self.assertIsNotNone(match, service)
            self.assertNotRegex(match.group(1), r"(?m)^    ports:")

    def test_data_network_is_internal(self):
        self.assertIn("  data:\n    internal: true", self.compose)
        self.assertIn("      - data", self.compose)
        self.assertIn("      - proxy", self.compose)

    def test_caddy_upstream_exists(self):
        self.assertIn("reverse_proxy demo-app:80", read("caddy/Caddyfile.example"))
        self.assertRegex(self.compose, r"(?m)^  demo-app:")

    def test_gitignore_covers_private_files(self):
        ignored = read(".gitignore")
        for pattern in (".env", "backups/", "*.key", "*.pem"):
            self.assertIn(pattern, ignored)

    def test_required_documentation_is_not_empty(self):
        paths = (
            "README.md", "docs/architecture-overview.md", "docs/network-access-model.md",
            "docs/network-diagram.md", "docs/reverse-proxy-caddy.md", "docs/wireguard-vpn.md",
            "docs/security-hardening.md", "docs/security-checklist.md", "docs/backup-strategy.md",
        )
        for path in paths:
            with self.subTest(path=path):
                self.assertGreater(len(read(path).strip()), 150)

    def test_readme_explains_no_production_or_https(self):
        readme = read("README.md").lower()
        self.assertIn("not a production deployment", readme)
        self.assertIn("http on localhost", readme)


if __name__ == "__main__":
    unittest.main()
