# Entwicklung

## Voraussetzungen

- Python 3.10 oder neuer
- FTP-Zugang zu einem Zielsystem mit Logdateien unter `/Log`

## Lokaler Start

Beispiel:

```powershell
python main.py --ip 192.168.1.10 --days 7 --target C:\Logs
```

Mit abweichendem Port:

```powershell
python main.py --ip 192.168.1.10 --port 21 --days 3 --target C:\Logs
```

## Wichtige Dateien

- `main.py`: Einstiegspunkt
- `functions/credential_store.py`: lokale Zugangsdatenverwaltung
- `functions/ftp_download.py`: FTP-Logik und Dateifilterung
- `functions/console_output.py`: Konsolenmeldungen

## Qualitätssicherung

Syntaxprüfung:

```powershell
python -m py_compile main.py functions\__init__.py functions\console_output.py functions\credential_store.py functions\ftp_download.py
```

## Hinweise

- Die Datei `.ftp_credentials.json` enthält lokal gespeicherte Zugangsdaten und ist nicht für das Repository gedacht.
- Der Zielordner wird automatisch erstellt, wenn er noch nicht existiert.
- Bereits vorhandene Dateien mit gleichem Namen werden bewusst überschrieben.
