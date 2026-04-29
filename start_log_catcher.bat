@echo off
setlocal
cd /d "%~dp0"

set "DEFAULT_TARGET_DIRECTORY=C:/temp/logs"
set "VENV_DIR=.venv"
set "REQUIREMENTS_FILE=requirements.txt"

REM Dieser Einstieg fuehrt auch unerfahrene Benutzer sicher durch die Vorbereitung.
call :resolve_python
if errorlevel 1 goto :end

if not exist "%VENV_DIR%\Scripts\python.exe" (
    echo Erstelle lokale Python-Umgebung...
    call %PYTHON_CMD% -m venv "%VENV_DIR%"
    if errorlevel 1 (
        echo Die lokale Python-Umgebung konnte nicht erstellt werden.
        goto :end
    )
)

echo Pruefe benoetigte Python-Bibliotheken...
call "%VENV_DIR%\Scripts\python.exe" -m pip install -r "%REQUIREMENTS_FILE%"
if errorlevel 1 (
    echo Die benoetigten Python-Bibliotheken konnten nicht installiert werden.
    goto :end
)

echo Starte wstechLogCatcher...
echo Wenn beim Zielordner nichts eingegeben wird, wird %DEFAULT_TARGET_DIRECTORY% verwendet.
call "%VENV_DIR%\Scripts\python.exe" main.py

echo.
:end
pause
goto :eof

:resolve_python
where py >nul 2>nul
if not errorlevel 1 (
    set "PYTHON_CMD=py -3"
    exit /b 0
)

where python >nul 2>nul
if not errorlevel 1 (
    set "PYTHON_CMD=python"
    exit /b 0
)

echo Python wurde auf diesem Rechner nicht gefunden.
set /p INSTALL_PYTHON="Soll Python jetzt installiert werden? [J/N]: "
if /i "%INSTALL_PYTHON%"=="J" goto :install_python
if /i "%INSTALL_PYTHON%"=="Y" goto :install_python

echo Ohne Python kann das Skript nicht gestartet werden.
exit /b 1

:install_python
echo Installiere Python ueber winget...
winget install Python.Python.3.13
if errorlevel 1 (
    echo Die Python-Installation wurde nicht erfolgreich abgeschlossen.
    exit /b 1
)

echo Python wurde installiert. Es wird erneut geprueft, ob der Befehl verfuegbar ist.
where py >nul 2>nul
if not errorlevel 1 (
    set "PYTHON_CMD=py -3"
    exit /b 0
)

where python >nul 2>nul
if not errorlevel 1 (
    set "PYTHON_CMD=python"
    exit /b 0
)

echo Python wurde installiert, ist aber in diesem Fenster noch nicht verfuegbar.
echo Bitte die Batch-Datei erneut starten.
exit /b 1
