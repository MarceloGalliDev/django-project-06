# pylint: disable=all

from django.apps import AppConfig  # type: ignore
from django.utils.translation import gettext_lazy as _  # type: ignore


class ProfilesConfig(AppConfig):
    """file for apps config"""
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.profiles"
    verbose_name = _("Profiles")

    # modificando a função padrão ready()
    def ready(self):
        from core_apps.profiles import signals  # noqa
