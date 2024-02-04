# pylint: disable=C0115, C0114, C0301, E1101, C0116

from django.contrib.auth import get_user_model  # type:ignore
from django.db import models  # type:ignore
from django.utils.translation import gettext_lazy as _  # type:ignore
from django_countries.fields import CountryField  # type:ignore
from phonenumber_field.modelfields import PhoneNumberField  # type:ignore
from core_apps.common.models import TimeStampedModel


User = get_user_model()


class Profile(TimeStampedModel):
    class Gender(models.TextChoices):
        MALE = (
            "M",
            _("Male"),
        )
        FEMALE = (
            "F",
            _("Female"),
        )
        OTHER = (
            "O",
            _("Other"),
        )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone_number = PhoneNumberField(
        verbose_name=_("phone number"), max_length=30, default="+5544999990123"
    )
    about_me = models.TextField(
        verbose_name=_("about me"), default="say something about yourself"
    )
    gender = models.CharField(
        verbose_name=_("gender"),
        choices=Gender.choices,
        default=Gender.OTHER,
        max_length=20,
    )
    country = CountryField(
        verbose_name=_("country"), default="BR", blank=False, null=False
    )
    city = models.CharField(
        verbose_name=_("city"),
        max_length=180,
        default="Maringá",
        blank=False,
        null=False,
    )
    photo_profile = models.ImageField(
        verbose_name=_("photo profile"), default="/profile_default.png"
    )
    twitter_handle = models.CharField(
        verbose_name=_("twitter handle"), max_length=20, blank=True
    )
    followers = models.ManyToManyField(
        "self", symmetrical=False, related_name="following", blank=True
    )

    def __str__(self):
        return f"{self.user.first_name}`s Profile"

    def follow(self, profile):
        self.followers.add(profile)

    def unfollow(self, profile):
        self.followers.remove(profile)

    def check_following(self, profile):
        return self.followers.filter(pkid=profile.pkid).exists()
