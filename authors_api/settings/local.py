# pylint: disable=all

"""file of local configs"""
from .base import *  # noqa
from .base import env  # noqa

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="0YMAJpQvgM85mB7cjzLMCw3VEmZnekDAFtnOAc1ZTafKRKhoRQAACfubOmhVGwNZEUI",
)

DEBUG = True

CSRF_TRUSTED_ORIGINS: list[str] = ["http://localhost:8080"]

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "suporte@goat.tech.com.br"
DOMAIN = env("DOMAIN")
SITE_NAME = "Authors Haven"
