from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("details/", views.product, name="product"),
    path("details/product/<int:id>/", views.detail, name="detail"),
    path("details/item/", views.item, name="item"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("login", views.one, name="one"),
    path("login", views.two, name="two"),
    path("login", views.three, name="three"),
    path("login", views.four, name="four"),
    path("login", views.five, name="five"),
    path("login", views.six, name="six"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("logout", views.logout, name="logout"),
    path("map", views.map, name="map"),
    path("add", views.cart_add, name="cart_add"),
    path("details/<int:id>/", views.category_view, name="category_view"),  # Updated line
]
