from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from core_apps.articles.models import Article


@registry.register_document
class ArticleDocument(Document):
    # aqui estamos se referindo ao title do article.models
    title = fields.TextField(attr="title")
    description = fields.TextField(attr="description")
    body = fields.TextField(attr="body")
    author_first_name = fields.TextField()
    author_last_name = fields.TextField()
    tags = fields.KeywordField()

    class Index:
        # Name of the Elasticsearch index
        name = "articles"
        # See Elasticsearch Indices API reference for available settings_name = fields.TextField()
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Article
        # The fields of the model you want to be indexed in Elasticsearch
        fields = ["created_at"]

    # and here we have the custom fields of the article.model
    def prepare_author_first_name(self, instance):
        return instance.author_first_name

    def prepare_author_last_name(self, instance):
        return instance.author_last_name

    def prepare_tags(self, instance):
        return [tag.name for tag in instance.tags.all()]
