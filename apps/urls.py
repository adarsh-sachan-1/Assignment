"""
apps views urls file
"""
# django import
from django.urls import path
# local import
from .views import ScrapeArticleView, ArticleListView, ArticleDetailView

urlpatterns = [
    path('scrape-article/', ScrapeArticleView.as_view(), name='scrape-article'),
    path('article-list/', ArticleListView.as_view(), name='article-list'),
    path('article-detail/<str:pk>/', ArticleDetailView.as_view(), name='article-detail'),
]
