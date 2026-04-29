# Entwicklung

## Voraussetzungen

- Python 3.10 oder neuer
- FTP-Zugang zu einem Zielsystem mit Logdateien unter `/Log`

## Lokaler Start

Beispiel:

```powershell
python main.py --ip 192.168.1.10 --days 7 --target C:\Logs
```

Interaktiv ohne Parameter:

```powershell
python main.py
```

Mit abweichendem Port:

```powershell
python main.py --ip 192.168.1.10 --port 21 --days 3 --target C:\Logs
```

Unter Windows gibt es zusätzlich `start_log_catcher.bat`. Diese Datei kann per Doppelklick gestartet werden und öffnet einen einfachen Eingabedialog in der Konsole.
Wenn beim Zielordner keine Eingabe erfolgt, wird automatisch `C:/temp/logs` verwendet.
Wenn Python fehlt, bietet die Batch-Datei eine Installation über `winget` an. Anschließend wird automatisch eine lokale `.venv`-Umgebung vorbereitet und `requirements.txt` installiert.

## Wichtige Dateien

- `main.py`: Einstiegspunkt
- `functions/credential_store.py`: lokale Zugangsdatenverwaltung
- `functions/interactive_mode.py`: Eingaben für den einfachen Start ohne Parameter
- `functions/ftp_download.py`: FTP-Logik und Dateifilterung
- `functions/console_output.py`: Konsolenmeldungen
- `start_log_catcher.bat`: einfacher Windows-Start mit Python- und Umgebungsprüfung
- `requirements.txt`: zentrale Liste für künftig benötigte Python-Pakete

## Qualitätssicherung

Syntaxprüfung:

```powershell
python -m py_compile main.py functions\__init__.py functions\console_output.py functions\credential_store.py functions\ftp_download.py
```

## Hinweise

- Die Datei `.ftp_credentials.json` enthält lokal gespeicherte Zugangsdaten und ist nicht für das Repository gedacht.
- Der Zielordner wird automatisch erstellt, wenn er noch nicht existiert.
- Bereits vorhandene Dateien mit gleichem Namen werden bewusst überschrieben.
