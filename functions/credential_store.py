import json
from getpass import getpass
from pathlib import Path


class CredentialStore:
    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path
        self._data = self._load()

    def _load(self) -> dict[str, dict[str, str]]:
        if not self.file_path.exists():
            return {}

        try:
            with self.file_path.open("r", encoding="utf-8") as handle:
                content = json.load(handle)
        except (OSError, json.JSONDecodeError):
            return {}

        if isinstance(content, dict):
            return content

        return {}

    def get(self, server_key: str) -> tuple[str, str] | None:
        entry = self._data.get(server_key)
        if not isinstance(entry, dict):
            return None

        username = entry.get("username")
        password = entry.get("password")
        if not username or not password:
            return None

        return username, password

    def set(self, server_key: str, username: str, password: str) -> None:
        self._data[server_key] = {"username": username, "password": password}
        with self.file_path.open("w", encoding="utf-8") as handle:
            json.dump(self._data, handle, indent=2)


def request_credentials(server_key: str) -> tuple[str, str]:
    print(f"Bitte Zugangsdaten fuer {server_key} eingeben.")
    username = input("Username: ").strip()
    password = getpass("Password: ")
    return username, password
