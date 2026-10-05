# AGENTS.md

## Overview
This repository contains a **Wagtail CMS** project powered by **Django** and **Python**.
It serves as a lightweight CMS application with custom page models (`pages` app), search functionality, and Docker deployment configuration.

---

### CRITICAL RULE FOR AGENTS
> [!IMPORTANT]
> **Always run commands and application services inside Docker.**
> Do not execute Python commands directly on the host system. Use `docker build`, `docker run`, or `docker compose` to run migrations, tests, and management commands.

---

## Technical Stack & Architecture

- **Language**: Python 3.14
- **Framework**: Django >= 6.1, Wagtail CMS >= 8.0
- **Database**: SQLite (`company_site/db.sqlite3`)
- **Server / Deployment**: Gunicorn WSGI, Docker (Multi-stage build)

---

## Directory Structure

```text
wagtail_mini_project/
├── AGENTS.md               # Instructions for AI Coding Agents
├── Dockerfile              # Production multi-stage Docker build configuration
├── README.md               # Quick setup instructions
├── manage.py               # Django CLI entrypoint
├── pages/                  # Wagtail custom pages application
│   ├── apps.py
│   ├── models.py           # Wagtail Page models (HomePage with StreamField)
│   └── templates/          # Templates for pages app
└── company_site/           # Main Wagtail project directory
    ├── db.sqlite3          # SQLite Database
    ├── requirements.txt    # Python dependencies
    ├── company_site/       # Django settings, WSGI, URLs configuration
    ├── home/               # Default home application
    └── search/             # Wagtail search integration
```

---

## Common Development Workflows (Docker-first)

### 1. Build Docker Image
```bash
docker build -t wagtail-mini-project .
```

### 2. Run Container & Application Server
```bash
docker run -p 8000:8000 wagtail-mini-project
```

### 3. Run Management Commands in Docker
```bash
# Run Django check
docker run --rm wagtail-mini-project python manage.py check

# Run migrations
docker run --rm wagtail-mini-project python manage.py migrate

# Create superuser
docker run -it --rm wagtail-mini-project python manage.py createsuperuser
```

---

## Coding Standards & Conventions for AI Agents

1. **Wagtail Models (`pages/models.py`)**:
   - Inherit from `wagtail.models.Page`.
   - Use modern `StreamField` definition with `use_json_field=True`.
   - Extend `content_panels = Page.content_panels + [...]` for admin UI editing.

2. **Templates**:
   - Store templates in standard Django app `templates/` structure.
   - Use Wagtail template tags (`{% load wagtailcore_tags wagtailimages_tags %}`).

3. **Code Safety & Verification**:
   - Before completing tasks, always test models and views using `python manage.py check`.
   - Maintain compatibility with Django 6.x and Wagtail 8.x.
