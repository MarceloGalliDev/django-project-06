"""
URL configuration for authors_api project.
"""
from django.contrib import admin  # type: ignore
from django.urls import path  # type: ignore
from django.conf import settings  # type: ignore

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
]
