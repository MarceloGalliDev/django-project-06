# pylint: disable=all

import uuid
from django.db import models  # type: ignore
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin  # type: ignore
from django.utils import timezone  # type: ignore
from django.utils.translation import gettext_lazy as _  # type: ignore
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    pkid = models.AutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=50, verbose_name="first name")
    last_name = models.CharField(max_length=50, verbose_name="last name")
    email = models.EmailField(
        max_length=50, verbose_name=_("Email address"), db_index=True, unique=True
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(default=timezone.now)  # Corrected field name

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.first_name

    @property
    def get_full_name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"

    @property
    def get_short_name(self):
        return self.first_name
