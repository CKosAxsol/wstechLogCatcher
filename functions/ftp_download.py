from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timedelta
from ftplib import FTP, all_errors
from pathlib import Path
import re

from functions.console_output import print_activity, print_progress

LOG_DIRECTORY = "/Log"
LOG_PATTERN = re.compile(r"^(?P<prefix>.+)_(?P<date>\d{8})_(?P<time>\d{6})\.csv$")


@dataclass
class DownloadResult:
    found_files: int
    downloaded_files: int
    overwritten_files: int


@contextmanager
def connect_ftp(ip: str, port: int, username: str, password: str):
    ftp = FTP()
    print_activity(f"Verbinde zu {ip}:{port}")
    try:
        ftp.connect(host=ip, port=port, timeout=15)
        ftp.login(user=username, passwd=password)
        ftp.cwd(LOG_DIRECTORY)
        print_activity("FTP-Verbindung aufgebaut")
        yield ftp
    finally:
        try:
            ftp.quit()
        except all_errors:
            ftp.close()


def parse_timestamp_from_filename(filename: str) -> datetime | None:
    match = LOG_PATTERN.match(filename)
    if match is None:
        return None

    timestamp_text = f"{match.group('date')}{match.group('time')}"
    try:
        return datetime.strptime(timestamp_text, "%Y%m%d%H%M%S")
    except ValueError:
        return None


def list_recent_log_files(ftp: FTP, days: int) -> list[str]:
    print_activity("Lese Dateiliste auf dem FTP-Server")
    filenames = ftp.nlst()
    cutoff = datetime.now() - timedelta(days=days)

    selected_files: list[str] = []
    for filename in filenames:
        timestamp = parse_timestamp_from_filename(filename)
        if timestamp is None:
            continue

        if timestamp >= cutoff:
            selected_files.append(filename)

    selected_files.sort()
    print_activity(f"{len(selected_files)} passende Logdateien gefunden")
    return selected_files


def download_logs(ftp: FTP, filenames: list[str], target_directory: Path) -> DownloadResult:
    overwritten_files = 0
    downloaded_files = 0
    total = len(filenames)

    if total == 0:
        print_activity("Keine Dateien im gewuenschten Zeitraum gefunden")
        return DownloadResult(found_files=0, downloaded_files=0, overwritten_files=0)

    for index, filename in enumerate(filenames, start=1):
        print_progress(index, total, filename)
        target_file = target_directory / filename

        if target_file.exists():
            overwritten_files += 1
            print_activity(f"Datei wird ueberschrieben: {target_file.name}")

        download_file(ftp, filename, target_file)
        downloaded_files += 1

    return DownloadResult(
        found_files=total,
        downloaded_files=downloaded_files,
        overwritten_files=overwritten_files,
    )


def download_file(ftp: FTP, filename: str, target_file: Path) -> None:
    print_activity(f"Lade Datei herunter: {filename}")
    with target_file.open("wb") as handle:
        ftp.retrbinary(f"RETR {filename}", handle.write)
