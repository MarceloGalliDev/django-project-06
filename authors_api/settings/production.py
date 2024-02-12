# pylint: disable=all

"""file of local configs"""
from authors_api.settings.local import SITE_NAME
from .base import *  # noqa
from .base import env  # noqa

ADMINS = [("Marcelo Galli", "marcelolemesgalli2@gmail.com")]

# TODO: add domains in product server
CSRF_TRUSTED_ORIGINS: list[str] = ["https://gallibrothers.dev"]

SECRET_KEY = env("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["gallibrothers.dev"])

ADMIN_URL = env("DJANGO_ADMIN_URL")

DATABASES = {
    "default": env.db("DATABASE_URL"),
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

# TODO: change this later 518400
SECURE_HSTS_SECONDS = 60

SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True
)

SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    "DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True
)

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DEFAULT_FROM_EMAIL = env(
    "DJANGO_DEFAULT_FROM_EMAIL", default="Galli Brothers <no-reply@gallibrothers.dev>"
)

SITE_NAME = "Galli Brothers API"
