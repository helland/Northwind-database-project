from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    #path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("orders/", views.orders_view, name="Orders"),
    path("suppliers/", views.suppliers_view, name="Suppliers"),
    path("products/", views.products_view, name="Products"),
    path("categories/", views.categories_view, name="Categories"),
    path("customers/", views.customers_view, name="Customers"),
    path("employees/", views.employees_view, name="Employees"),
    path("shippers/", views.shippers_view, name="shippers"),
    path("demographics/", views.demo_view, name="demographics"),
    path("misc/", views.misc, name="misc"),
    path("orders-in-detail/", views.order_details_view, name="orders-in-detail"),
    #path("misc/", views.misc_tools, name="misc"),
    path("login/", views.login, name="login"),
    path("sign-up", views.sign_up, name="sign-up"),
    path('create-product-list/', views.create_product_list, name='create-product-list'),
    path('save-product-list/', views.save_product_list, name='save-product-list'),
        
     ]   


