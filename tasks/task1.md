beachte imemr die `AGENTS.md`

Über eine FTP Verbindung lassen sich Logfile-CSV Dateien abholen.
Die Logdateien sind namentlich mit Zeitstempeln abgelegt, z.B. `APS-001249_20260228_000000.csv`
Die Dateien liegen immer unter FTP Verbindung unter `ftp://$IP$/Log/`
Die IP-Adresse $IP$ muss konfigurierbar sein, weil es sich um mehrere FTP Verbindungen handeln kann
Der FTP Zugang ist einfach abgesichert mit `username` und `password` welches man beim Ausführen des Skripts eingeben können muss.
Idealerweise sollte das Skript eine Art `env` anlegen, in dem je IP-Adresse bekannte `username` und `password` abgelegt werden, damit man es nicht erneut eingeben muss.
Bei vorhandenen Einträgen, soll nach einem neuen `password` und `username` gefragt werden, sollte die FTP Verbindung nicht aufgebaut werden können.

# Aufgabe
Ich möchte über ein Skript die letzten x-Tage von Logdateien kopieren.
Dabei gebe ich den Zielordner an, wo die Logdateien hinkopiert werden sollen.
Logdateien mit gleichen Namen werden überschrieben, in der Ausgabe soll hierzu ein Hinweis erfolgen.

Das Skript soll in der Ausgabe eine Fortschrittsanzeige und eine Art Mini-Log haben, damit man weiß dass das Skript gerade arbeitet.

Skriptsprache soll hierbei python sein.

Ich möchte auch eine Möglichkeit das Skript auszuführen, wenn man absolut keine Ahnung von Programmieren und Konsolen hat. So etwas wie eine via Doppelklick anklickbare Datei. Die Umgebung ist hier in erster Linie Windows.
Für das `start_log_catcher.bat` soll das standard zielverzeichnis `C:/temp/logs` sein, wenn der Benutzer kein anderes angibt.

Wenn beim Ausführen der Batch-Datei festgestellt wird, dass python nicht installiert ist, soll eine abfrage kommen, ob man python nachinstallieren möchte.
Fehlende pyhton biblotheken soll das skript danach automatisch in einer `env` umgebung nachinstallieren.
