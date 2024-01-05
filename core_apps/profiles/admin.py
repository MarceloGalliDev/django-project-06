# pylint: disable = C0115, C0114

from django.contrib import admin  # type: ignore
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["pkid", "id", "user", "gender", "phone_number", "country", "city"]
    list_display_links = ["pkid", "id", "user"]
    list_filter = ["pkid", "id"]


admin.site.register(Profile, ProfileAdmin)
