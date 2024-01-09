# pylint: disable = C0115, C0114, C0301, C0116
# flake8: noqa

from django_countries.serializer_fields import CountryField
from rest_framework import serializers  # type: ignore
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(sorce="user.email")
    full_name = serializers.SerializerMethodField(read_only=True)
    profile_photo = serializers.SerializerMethodField()
    country = CountryField(name_only=True)

    class Meta:
        model = Profile
        fields = ["id", "first_name", "last_name", "email", "profile_photo", "phone_number", "gender", "country", "city", "twitter_handle", "abount_me"]

    def get_full_name(self, obj):
        first_name = obj.user.first_name.title()
        last_name = obj.user.last_name.title()
        return f"{first_name} {last_name}"

    def get_profile_photo(self, obj):
        return obj.profile_photo.url