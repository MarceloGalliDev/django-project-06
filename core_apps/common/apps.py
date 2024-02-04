"""file for apps config"""

from django.apps import AppConfig  # type: ignore
from django.utils.translation import gettext_lazy as _  # type: ignore


class CommonConfig(AppConfig):
    """file for apps config"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.common"
    verbose_name = _("Common")
