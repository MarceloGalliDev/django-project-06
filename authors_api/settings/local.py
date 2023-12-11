# pylint: disable=all

"""file of local configs"""
from .base import *  # noqa
from .base import env  # noqa

SECRET_KEY = env(
    'DJANGO_SECRET_KEY',
    default='0YMAJpQvgM85mB7cjzLMCw3VEmZnekDAFtnOAc1ZTafKRKhoRQAACfubOmhVGwNZEUI',
)

DEBUG = True

CSRF_TRUSTED_ORIGINS: list[str] = ["http://localhost:8080"]
