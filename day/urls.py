from django.urls import path 
from .import views 


urlpatterns =[
    path("",views.home,name="home"),
    path("details/",views.product,name="product"),
   path("details/product/<int:id>/", views.detail, name="detail"),
    path('details/item/', views.item, name='item_detail'),
    path("details/<int:id>/", views.one, name='one')

]