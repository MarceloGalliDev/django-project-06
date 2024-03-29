# pylint: disable=C0115, C0114, E1101, C0301, C0116

from django.db import models
from django.contrib.auth import get_user_model
from autoslug import AutoSlugField
from taggit.managers import TaggableManager
from core_apps.common.models import TimeStampedModel
from .read_time_engine import ArticleReadTimeEngine
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Clap(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey("Article", on_delete=models.CASCADE)

    class Meta:
        unique_together = ["user", "article"]
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.first_name} clapped {self.article.title}"


class Article(TimeStampedModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    title = models.CharField(verbose_name=_("title"), max_length=255)
    slug = AutoSlugField(populate_from="title", always_update=True, unique=True)
    description = models.CharField(verbose_name=_("description"), max_length=255)
    body = models.TextField(verbose_name=_("article_content"))
    banner_image = models.ImageField(
        verbose_name=_("banner_image"), default="/profile_default.png"
    )
    tags = TaggableManager()

    claps = models.ManyToManyField(User, through=Clap, related_name="clapped_articles")

    def __str__(self):
        return f"{self.author.first_name}`s article"

    @property
    def estimated_reading_time(self):
        return ArticleReadTimeEngine.estimate_reading_time(self)

    def view_count(self):
        return self.articles_views.count()

    def average_rating(self):
        # here we have the connection with related_name
        ratings = self.ratings.all()

        if ratings.count() > 0:
            total_rating = sum(rating.rating for rating in ratings)
            avarege_rating = total_rating / ratings.count()
            return round(avarege_rating, 2)
        return None


class ArticleView(TimeStampedModel):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="articles_views"
    )
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="user_views"
    )
    viewer_ip = models.GenericIPAddressField(
        verbose_name=_("viewer_ip"), null=True, blank=True
    )

    class Meta:
        verbose_name = _("Article View")
        verbose_name_plural = _("Article Views")
        unique_together = ("article", "user", "viewer_ip")

    def __str__(self):
        return f"{self.article.title} viewed by {self.user.first_name if self.user else 'Anonymous'} from IP {self.viewer_ip}"

    @classmethod
    def record_view(cls, article, user, viewer_ip):
        view, _ = cls.objects.get_or_create(
            article=article, user=user, viewer_ip=viewer_ip
        )
        view.save()
