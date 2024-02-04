# pylint: disable=all

"""
WSGI config for authors_api project.
"""

import os

from django.core.wsgi import get_wsgi_application  # type: ignore

# TODO: change this in production
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "authors_api.settings.local")

application = get_wsgi_application()
