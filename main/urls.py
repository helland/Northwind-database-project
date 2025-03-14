from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    #path("<int:id>", views.index, name="index"),                    # 
    path("", views.home, name="home"),                              # home page
    path("orders/", views.orders_view, name="Orders"),              # users can see a list of all orders here
    path("suppliers/", views.suppliers_view, name="Suppliers"),     # anyone can see a list of all suppliers here
    path("products/", views.products_view, name="Products"),        # anyone can see a list of all available products here
    path("categories/", views.categories_view, name="Categories"),  # anyone can see a list of all product categories here, but it has not been linked anywhere yet
    path("customers/", views.customers_view, name="Customers"),     # users can see a list of all customers here
    path("employees/", views.employees_view, name="Employees"),     # users can see a list of all employees here
    path("shippers/", views.shippers_view, name="shippers"),        # anyone can see a list of all shipping companies used here
    path("demographics/", views.demo_view, name="demographics"),    # users can see customer types here, or they could have, but the database table is currently empty
    path("misc/", views.misc, name="misc"),                         # users can find functions here that hasn't been given a proper link to it yet. currently it contains two functions. The user can create a list of products (and give that list a name) and they can view all lists they have created.
    path("orders-in-detail/", views.order_details_view, name="orders-in-detail"), # not implemented yet
    #path("misc/", views.misc_tools, name="misc"),
    path("login/", views.login, name="login"),                      # users can log in here. If they don't have an account, it links to 'sign-up'
    path("sign-up", views.sign_up, name="sign-up"),                 # anyone can sign up here, with a username, email and password.
    path('create-product-list/', views.create_product_list, name='create-product-list'),    # Users can create a list of products here. The products can be found in a drop-down menu and be added to the list with an add button. When all items have been added, the user can give the list a name.  if no name is added, the date of creation becomes the list's name.
    path('save-product-list/', views.save_product_list, name='save-product-list'),          # Users who create a list in the former url is sent here when they click the "save list" button. the list displayed in the table will be stored in the database, linked to the user who created it.
        
     ]   


