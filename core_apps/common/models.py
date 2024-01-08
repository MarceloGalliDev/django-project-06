# pylint: disable=C0115, C0114

import uuid
from django.db import models  # type: ignore


class TimeStampedModel(models.Model):
    pkid = models.AutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at", "-updated_at"]
