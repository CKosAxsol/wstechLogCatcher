import argparse
import sys
from pathlib import Path

from functions.console_output import print_header, print_summary
from functions.credential_store import (
    CredentialStore,
    request_credentials,
)
from functions.ftp_download import (
    connect_ftp,
    download_logs,
    list_recent_log_files,
)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Laedt Logdateien der letzten x Tage von einem FTP-Server herunter."
    )
    parser.add_argument("--ip", required=True, help="IP-Adresse oder Hostname des FTP-Servers.")
    parser.add_argument(
        "--port",
        type=int,
        default=21,
        help="FTP-Port. Standard ist 21.",
    )
    parser.add_argument(
        "--days",
        type=int,
        required=True,
        help="Anzahl der letzten Tage, aus denen Logdateien kopiert werden sollen.",
    )
    parser.add_argument(
        "--target",
        required=True,
        help="Zielordner, in den die Logdateien kopiert werden sollen.",
    )
    return parser.parse_args()


def load_working_credentials(store: CredentialStore, server_key: str) -> tuple[str, str]:
    saved_credentials = store.get(server_key)
    if saved_credentials is None:
        username, password = request_credentials(server_key)
        store.set(server_key, username, password)
        return username, password

    return saved_credentials


def ensure_valid_credentials(
    store: CredentialStore, server_key: str, ip: str, port: int
) -> tuple[str, str]:
    username, password = load_working_credentials(store, server_key)

    try:
        with connect_ftp(ip, port, username, password):
            return username, password
    except Exception:
        print("Gespeicherte Zugangsdaten konnten nicht verwendet werden.")
        username, password = request_credentials(server_key)
        with connect_ftp(ip, port, username, password):
            store.set(server_key, username, password)
            return username, password


def main() -> int:
    args = parse_arguments()
    if args.days < 0:
        print("Die Anzahl der Tage muss 0 oder groesser sein.")
        return 1

    target_directory = Path(args.target).expanduser().resolve()
    target_directory.mkdir(parents=True, exist_ok=True)

    print_header(args.ip, args.port, args.days, target_directory)

    server_key = f"{args.ip}:{args.port}"
    store = CredentialStore(Path(".ftp_credentials.json"))

    try:
        username, password = ensure_valid_credentials(store, server_key, args.ip, args.port)
        with connect_ftp(args.ip, args.port, username, password) as ftp:
            files_to_download = list_recent_log_files(ftp, args.days)
            result = download_logs(ftp, files_to_download, target_directory)
    except Exception as error:
        print(f"Fehler: {error}")
        return 1

    print_summary(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
