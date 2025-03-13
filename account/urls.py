from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [

    path("product-lists/", views.my_product_lists, name="product-lists"),
    path("product-lists/list-details/<int:product_list_id>/", views.view_product_list, name="product-list-details"),    
     ]   
