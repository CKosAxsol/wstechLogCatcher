# ADR 0001: Dokumentationsstruktur anlegen

## Status

Angenommen

## Kontext

In `AGENTS.md` ist eine klare Projektstruktur für Dokumentation beschrieben. Das Projekt hatte zunächst nur das Skript und eine README, aber keinen `docs`-Ordner.

## Entscheidung

Es wird eine kleine, aber vollständige Dokumentationsstruktur angelegt:

- `docs/architecture.md`
- `docs/development.md`
- `docs/flows/`
- `docs/decisions/`

## Folgen

- Die Projektstruktur entspricht den Vorgaben aus `AGENTS.md`.
- Künftige Änderungen haben einen festen Ort für Architektur-, Ablauf- und Entwicklungsdokumentation.
- Die Dokumentation bleibt schlank und kann mit dem Projekt wachsen.
