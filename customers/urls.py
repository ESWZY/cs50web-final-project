from django.urls import path
from . import views

app_name = "customers"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("subscribe", views.subscribe, name="subscribe"),
    path("shop", views.shop, name="shop"),
]
