# Wagtail Mini Project

Projekt CMS oparty na Django i Wagtail, gotowy do uruchomienia w środowisku Docker.

## Uruchomienie za pomocą Docker Compose

```bash
# Uruchomienie aplikacji
docker compose up -d

# Podgląd logów
docker compose logs -f

# Stworzenie konta administratora (superuser)
docker compose run -it --rm web python manage.py createsuperuser
```

Aplikacja będzie dostępna pod adresami:
- **Strona główna**: `http://localhost:8090/`
- **Panel Administratora Wagtail**: `http://localhost:8090/admin/`
