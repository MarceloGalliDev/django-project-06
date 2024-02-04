# pylint: disable=all

import logging

from django.db.models.signals import post_save  # type:ignore
from django.dispatch import receiver  # type:ignore
from authors_api.settings.base import AUTH_USER_MODEL
from core_apps.profiles.models import Profile

logger = logging.getLogger(__name__)


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        logger.info(f"{instance}`s profile has been created.")


# signals é acionado quando há criação de um user, conforme citado, ele dispara um signals
# o post_save é para quando após ser salvo no banco ele envia o signals
