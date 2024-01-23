# pylint: disable=C0114

from django.contrib import admin
from .models import Bookmark


admin.site.register(Bookmark)
