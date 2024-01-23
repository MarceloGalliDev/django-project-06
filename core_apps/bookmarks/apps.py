# pylint: disable=all

from django.apps import AppConfig  # type: ignore
from django.utils.translation import gettext_lazy as _  # type: ignore


class BookmarksConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.bookmarks"
    verbose_name = _("Bookmarks")
