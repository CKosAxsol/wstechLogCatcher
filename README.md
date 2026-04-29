# wstechLogCatcher

Kleines Python-Werkzeug zum Herunterladen von Logfile-CSV-Dateien per FTP.

Das Skript verbindet sich mit einem konfigurierbaren FTP-Ziel, filtert Dateien anhand ihres Zeitstempels im Dateinamen und kopiert nur die Dateien der letzten `x` Tage in einen Zielordner.

## Voraussetzungen

- Python 3.10 oder neuer
- Zugriff auf einen FTP-Server mit Logdateien unter `/Log/`

## Setup

Es werden keine zusätzlichen Python-Abhängigkeiten benötigt.

## Wichtige Befehle

Syntax prüfen:

```powershell
python -m py_compile main.py functions\*.py
```

Logdateien herunterladen:

```powershell
python main.py --ip 192.168.1.10 --days 7 --target C:\Logs
```

Optionalen FTP-Port angeben:

```powershell
python main.py --ip 192.168.1.10 --port 21 --days 3 --target C:\Logs
```

## Nutzung

Beim ersten Aufruf fragt das Skript nach `username` und `password`. Die Daten werden lokal pro FTP-Ziel in `.ftp_credentials.json` gespeichert.

Wenn eine gespeicherte Kombination nicht mehr funktioniert, fragt das Skript erneut nach den Zugangsdaten und aktualisiert den Eintrag.

Während des Downloads zeigt das Skript:

- einen kleinen Aktivitäts-Log in der Konsole
- den Fortschritt über alle ausgewählten Dateien
- einen Hinweis, wenn vorhandene Zieldateien überschrieben werden

## Dokumentation

Weiterführende Projektinformationen liegen unter `docs/`:

- `docs/architecture.md`
- `docs/development.md`
- `docs/flows/ftp-log-download.md`
- `docs/decisions/0001-dokumentationsstruktur.md`
