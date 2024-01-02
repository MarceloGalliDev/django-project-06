# pylint: disable=W0511, C0114, E0401

import os

from celery import Celery  # type: ignore
from django.conf import settings  # type: ignore


# TODO: change this to production
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "authors_api.settings.local")

app = Celery("authors_api")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
