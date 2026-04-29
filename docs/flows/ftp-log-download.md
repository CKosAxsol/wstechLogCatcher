# FTP-Log-Download

```mermaid
sequenceDiagram
  participant U as Benutzer
  participant M as main.py
  participant S as Credential Store
  participant F as FTP-Server
  participant D as Zielordner

  U->>M: Start mit IP, Tagen und Zielordner
  M->>S: Gespeicherte Zugangsdaten laden
  alt Zugangsdaten fehlen oder sind ungültig
    M->>U: Username und Password abfragen
    M->>S: Neue Zugangsdaten speichern
  end
  M->>F: Verbindung aufbauen und /Log öffnen
  F-->>M: Dateiliste zurückgeben
  M->>M: Dateien nach Zeitstempel filtern
  loop Für jede passende Datei
    M->>D: Datei herunterladen
    M->>U: Fortschritt und Überschreiben melden
  end
  M->>U: Zusammenfassung ausgeben
```

## Ablaufbeschreibung

Der Benutzer startet das Skript über die Kommandozeile. Danach prüft das Skript zuerst, ob für das gewünschte FTP-Ziel bereits Zugangsdaten gespeichert wurden. Wenn die Verbindung damit nicht gelingt, werden neue Zugangsdaten abgefragt.

Nach erfolgreicher Verbindung liest das Skript alle Dateien im FTP-Ordner `/Log`, filtert diese über den Zeitstempel im Dateinamen und lädt nur die Dateien im gewünschten Zeitraum herunter.
