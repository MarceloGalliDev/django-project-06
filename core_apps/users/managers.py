# pylint: disable=all

"""configuration of custom users"""

from django.contrib.auth.base_user import BaseUserManager  # type: ignore
from django.core.exceptions import ValidationError  # type: ignore
from django.core.validators import validate_email  # type: ignore
from django.utils.translation import gettext_lazy as _  # type: ignore


class CustomUserManager(BaseUserManager):
    """class CustomUserManager for customization of user django"""
    def email_validator(self, email):
        """"validation emails"""
        try:
            validate_email(email)
            return True
        except ValidationError:
            raise ValueError(_('You must provider a valid email!'))

    def create_user(self, first_name, last_name, email, password, **extra_fields):
        if not first_name:
            raise ValueError(_('Users must have a first name.'))

        if not last_name:
            raise ValueError(_('Users must have a last name.'))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_('Users must have a valid e-mail.'))

        user = self.model(first_name=first_name, last_name=last_name, email=email, **extra_fields)
        user.set_password(password)

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
