from django.contrib import admin
from .models import *

# Register your models here.
 
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "birth_date",)
 
class ProductListAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "created_at",)
 
  
 
admin.site.register(Suppliers)
admin.site.register(Products)
admin.site.register(Categories)
admin.site.register(Order_details)
admin.site.register(Customers)
admin.site.register(Customer_customer_demo)
admin.site.register(Customer_demographics)
admin.site.register(Orders)
admin.site.register(Employees, EmployeeAdmin)
admin.site.register(Employee_territories)
admin.site.register(Territories)
admin.site.register(Region)
admin.site.register(Shippers)
admin.site.register(Us_states)
admin.site.register(ProductList, ProductListAdmin)