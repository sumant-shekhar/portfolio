# IGNOU Study Desk

A Django site for viewing the IGNOU academic dashboard and the source records used to build it.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in a browser.

The HTML templates live in `templates/` and the original PDF documents live in `pdf/`. Static assets are served from `static/` during development. Before production, set a real `SECRET_KEY`, set `DEBUG = False`, configure `ALLOWED_HOSTS`, and run `python manage.py collectstatic`.