from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SearchConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.search"
    verbose_name = _("Search")

    # quando temos signals na aplicação é necessario inclui-lo aqui
    def ready(self):
        import core_apps.search.signals
