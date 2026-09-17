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

## GitHub Pages

GitHub Pages cannot run Django directly. This repository includes `build_static.py`, which renders the Django templates into a static `docs/` site, and `.github/workflows/pages.yml`, which deploys it automatically on pushes to `main`.

To build it locally:

```bash
python build_static.py
```

In GitHub repository settings, set Pages > Build and deployment > Source to **GitHub Actions**. The deployed site will use the repository's GitHub Pages URL.