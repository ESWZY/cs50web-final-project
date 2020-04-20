from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("index", views.index, name="index"),
    path("search", views.search, name="search"),
    path("discovery", views.discovery, name="discovery"),
    path("<title>", views.article, name="full_article"),
]
