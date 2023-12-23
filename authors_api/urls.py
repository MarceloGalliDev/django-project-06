"""
URL configuration for authors_api project.
"""
from django.contrib import admin  # type: ignore
from django.urls import path  # type: ignore
from django.conf import settings, include  # type: ignore
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


get_schema_view = get_schema_view(
    openapi.Info(
        title="Authors Haven API",
        default_version="v1",
        description="API endpoint for Authors Haven API course",
        contact=openapi.Contact(email="goat.tech@gmail.com"),
        license=openapi.License(name="MIT License")
    ),
    public=True,
    permission_classes=(permissions.AllowAny)
)

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
]
