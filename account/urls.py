from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [

    path("product-lists/", views.my_product_lists, name="product-lists"),                                            # Users can see a list of all their product lists here
    path("product-lists/list-details/<int:product_list_id>/", views.view_product_list, name="product-list-details"), # Users can see the details of their product lists here   
     ]   
