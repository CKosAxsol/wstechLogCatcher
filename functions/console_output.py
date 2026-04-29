from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from functions.ftp_download import DownloadResult


def print_header(ip: str, port: int, days: int, target_directory: Path) -> None:
    print("Starte FTP-Log-Abruf")
    print(f"Quelle: {ip}:{port}/Log/")
    print(f"Zeitraum: letzte {days} Tage")
    print(f"Zielordner: {target_directory}")
    print("-" * 60)


def print_progress(current: int, total: int, filename: str) -> None:
    print(f"[{current}/{total}] Verarbeite {filename}")


def print_activity(message: str) -> None:
    print(f"  -> {message}")


def print_summary(result: "DownloadResult") -> None:
    print("-" * 60)
    print("Fertig")
    print(f"Gefundene Dateien: {result.found_files}")
    print(f"Heruntergeladene Dateien: {result.downloaded_files}")
    print(f"Ueberschriebene Dateien: {result.overwritten_files}")
