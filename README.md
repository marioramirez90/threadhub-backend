# ThreadHub Django Backend

Ein vollständiges Python Django REST Framework Backend für das Frontend **final-project-2024-05-threadhub**.

## Übersicht

Dieses Backend ersetzt den bisherigen Node/json-server und ist 100% kompatibel zu den Erwartungen des Vue 3 Frontends:
- **Users**: /users und /users/<id>
- **Posts**: /posts und /posts/<id> (unterstützt Erstellen, Bearbeiten, Löschen, Tags und Timestamps)
- **Comments**: /comments und /comments/<id>
- **CORS**: Vollständig aktiviert für Vite Dev-Server (http://localhost:5173)
- **Trailing Slashes**: Vollständig kompatibel sowohl mit /posts als auch /posts/ (kein 301-Redirect bei POST/PUT/DELETE)
- **Standard-Port 3000**: Startet mit python manage.py runserver automatisch auf Port 3000!
- **Django Admin**: Voller Zugriff auf alle Modelle unter /admin/

---

## Schnellstart

Navigiere in diesen Ordner und starte den Server:
`powershell
cd C:\Users\mario\Desktop\final-project-2024-05-threadhub-backend
python manage.py runserver
`

Die API ist dann unter http://localhost:3000/ erreichbar.

---

## Test-Accounts für das Vue-Frontend

| Benutzername | Passwort | Rolle |
| :--- | :--- | :--- |
| **gast** | gast | Gastbenutzer |
| **Testinand** | 123456 | Standardbenutzer |
| **Poweradmin** | dmin | Administrator |
| **JaneDoe** | password123 | Standardbenutzer |
| **MaxMustermann** | maxsecure | Standardbenutzer |
| **CoderGuy** | cod3rul3s! | Standardbenutzer |

---

## Django Admin

Unter http://localhost:3000/admin/ kannst du alle Daten bequem im Browser verwalten:
- **Benutzername**: dmin
- **Passwort**: dmin

---

## Nützliche Befehle

### Daten neu initialisieren (Seeden)
Setzt die Testdaten aus db.json zurück:
`powershell
python manage.py seed_data --clear
`

### Automatisierte Tests ausführen
Führt die Kompatibilitäts- und API-Tests aus:
`powershell
python manage.py test api
`
