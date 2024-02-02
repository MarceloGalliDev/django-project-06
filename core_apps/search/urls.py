from django.urls import path
from .views import ArticleElasticSearchView


urlpatterns = [
    # aqui estamos referenciando o method HTTP get ao elasticsearch com referencia de list
    path(
        "search/",
        ArticleElasticSearchView.as_view({"get": "list"}),
        name="article_search",
    ),
]
