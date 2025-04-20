from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("details/", views.product, name="product"),
    path("details/product/<int:id>/", views.detail, name="detail"),
    path("details/item/", views.item, name="item"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("logout", views.logout, name="logout"),
    path("add", views.cart_add, name="cart_add"),
    path("details/<int:id>/", views.category_view, name="category_view"),  # Updated line
]
