import argparse
from pathlib import Path

DEFAULT_TARGET_DIRECTORY = "C:/temp/logs"


def collect_runtime_arguments() -> argparse.Namespace:
    print("Interaktiver Start fuer den FTP-Log-Abruf")
    print("Bitte die benoetigten Angaben eingeben.")

    ip = ask_non_empty_value("IP-Adresse oder Hostname: ")
    port_text = ask_non_empty_value("FTP-Port [21]: ", default_value="21")
    days_text = ask_non_empty_value("Letzte wie viele Tage?: ")
    target = ask_non_empty_value(
        f"Zielordner fuer die Dateien [{DEFAULT_TARGET_DIRECTORY}]: ",
        default_value=DEFAULT_TARGET_DIRECTORY,
    )

    return argparse.Namespace(
        ip=ip,
        port=parse_port(port_text),
        days=parse_days(days_text),
        target=str(Path(target).expanduser()),
    )


def ask_non_empty_value(prompt_text: str, default_value: str | None = None) -> str:
    while True:
        user_input = input(prompt_text).strip()
        if user_input:
            return user_input

        if default_value is not None:
            return default_value

        print("Bitte einen Wert eingeben.")


def parse_port(port_text: str) -> int:
    try:
        port = int(port_text)
    except ValueError as error:
        raise ValueError("Der FTP-Port muss eine ganze Zahl sein.") from error

    if port <= 0:
        raise ValueError("Der FTP-Port muss groesser als 0 sein.")

    return port


def parse_days(days_text: str) -> int:
    try:
        days = int(days_text)
    except ValueError as error:
        raise ValueError("Die Anzahl der Tage muss eine ganze Zahl sein.") from error

    if days < 0:
        raise ValueError("Die Anzahl der Tage darf nicht negativ sein.")

    return days
