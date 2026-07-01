# Django Blog / Weblog App

Django aplikácia na správu blogových príspevkov s administráciou (Jazzmin dashboard), rich-text editorom (CKEditor), registráciou/prihlásením používateľov, tímami a ligami (weblog_app).

## Funkcie

- Registrácia, prihlásenie, profily používateľov
- Tvorba, úprava a mazanie príspevkov s CKEditor rich-text editorom
- Komentáre pod príspevkami
- Vyhľadávanie (vrátane live search)
- Správa tímov a líg (managers, teams, leagues, tables)
- Vlastný admin dashboard cez django-jazzmin

## Technológie

- Python, Django 4.1
- django-ckeditor, django-jazzmin, django-crispy-forms, django-smart-selects
- SQLite

## Lokálne spustenie

1. Vytvor virtuálne prostredie a nainštaluj závislosti:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r blog/requirements.txt
   ```

2. V priečinku `blog/` skopíruj `.env.example` na `.env` a doplň hodnoty (najmä `DJANGO_SECRET_KEY` — vygeneruješ ho príkazom v komentári v `.env.example`):
   ```bash
   cd blog
   cp .env.example .env
   ```

3. Spusti migrácie a appku:
   ```bash
   ./manage.py migrate
   ./manage.py createsuperuser
   ./manage.py runserver
   ```
   Aplikácia beží na `http://localhost:8000`, administrácia na `/admin/`.

## Poznámka

Cvičný/portfóliový projekt vytvorený pri učení sa Django. Databáza (`db.sqlite3`) a `sql.log` sa vytvoria automaticky pri behu a nie sú súčasťou repozitára.
