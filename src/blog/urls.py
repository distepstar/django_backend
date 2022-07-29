from django.urls import path

from .views import (
    blog_main_view,
    blog_article_view,
    BlogArticleCreateView,
    BlogArticleListView,
    BlogArticleDetailView,
    BlogArticleUpdateView,
    BlogArticleDeleteView,
    BlogMainView
)

app_name = 'blog'

urlpatterns = [
    path('', BlogMainView.as_view(), name='blog_main'),
    path('article/', blog_article_view, name='blog_article'),
    path('article-class-list/', BlogArticleListView.as_view(), name='blog_article_list'),
    path('article-class-list/<slug:pk>/', BlogArticleDetailView.as_view(), name='blog_article_detail'),
    path('article-class-create/', BlogArticleCreateView.as_view(), name='blog_article_create'),
    path('article-class-update/<slug:pk>/', BlogArticleUpdateView.as_view(), name='blog_article_update'),
    path('article-class-delete/<slug:pk>/', BlogArticleDeleteView.as_view(), name='blog_article_delete'),
]
