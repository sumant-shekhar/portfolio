from pathlib import Path
import shutil

import django
from django.conf import settings
from django.template.loader import get_template


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "docs"
PAGES = {
    "Homepage.html": "index.html",
    "December_2024.html": "December_2024.html",
    "July_2025.html": "July_2025.html",
    "December_2025.html": "December_2025.html",
    "july_2026.html": "july_2026.html",
    "grade-card.html": "grade-card.html",
    "assignment-status.html": "assignment-status.html",
    "exam-courses.html": "exam-courses.html",
    "profile.html": "profile.html",
}


def build():
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir()

    django.setup()
    for source_name, output_name in PAGES.items():
        rendered = get_template(source_name).render()
        rendered = rendered.replace('href="Homepage.html"', 'href="index.html"')
        rendered = rendered.replace('href="/static/', 'href="static/')
        rendered = rendered.replace(
            'href="isms.ignou.ac.in_changeadmdata_StatusAssignment.ASP.pdf"',
            'href="static/pdf/isms.ignou.ac.in_changeadmdata_StatusAssignment.ASP.pdf"',
        )
        (OUTPUT_DIR / output_name).write_text(rendered, encoding="utf-8")

    shutil.copytree(BASE_DIR / "static", OUTPUT_DIR / "static")
    shutil.copytree(BASE_DIR / "pdf", OUTPUT_DIR / "static" / "pdf")
    (OUTPUT_DIR / ".nojekyll").touch()


if __name__ == "__main__":
    import os

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ignou_site.settings")
    build()