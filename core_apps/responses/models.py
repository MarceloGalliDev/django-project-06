# pylint: disable=C0114, C0115, E1101

from django.db import models
from django.contrib.auth import get_user_model
from core_apps.common.models import TimeStampedModel
from core_apps.articles.models import Article


User = get_user_model()


class Response(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="responses")
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="responses"
    )
    parents_response = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="replies", blank=True, null=True
    )
    content = models.TextField(verbose_name="response-content")

    class Meta:
        verbose_name = "Response"
        verbose_name_plural = "Responses"
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.user.first_name} commented on {self.article.title}."
