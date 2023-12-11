# pylint: disable=all

"""file of local configs"""
from .base import *  # noqa
from .base import env  # noqa

ADMINS = [("Marcelo Galli", "marcelolemesgalli2@gmail.com")]

# TODO: add domains in product server
CSRF_TRUSTED_ORIGINS: list[str] = [""]
