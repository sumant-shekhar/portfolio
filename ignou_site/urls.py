from django.urls import path
from django.views.generic import TemplateView


PAGE_TEMPLATES = {
    "December_2024.html": "December_2024.html",
    "July_2025.html": "July_2025.html",
    "December_2025.html": "December_2025.html",
    "july_2026.html": "july_2026.html",
    "grade-card.html": "grade-card.html",
    "assignment-status.html": "assignment-status.html",
    "exam-courses.html": "exam-courses.html",
    "profile.html": "profile.html",
}

urlpatterns = [
    path("", TemplateView.as_view(template_name="Homepage.html"), name="home"),
]

urlpatterns += [
    path(url, TemplateView.as_view(template_name=template), name=url.removesuffix(".html"))
    for url, template in PAGE_TEMPLATES.items()
]