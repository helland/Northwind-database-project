from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import default



# Create your models here.

# available supliers
class Suppliers(models.Model):
    supplier_id = models.SmallIntegerField(primary_key=True, blank=False)   
    company_name = models.CharField(max_length=250, blank=False)
    contact_name = models.CharField(max_length=250)
    contact_title = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)          
    region = models.CharField(max_length=250)       
    postal_code = models.CharField(max_length=250)  
    country = models.CharField(max_length=250)       
    phone = models.CharField(max_length=250)
    fax = models.CharField(max_length=250)
    homepage = models.TextField()
    

    def __str__(self):
        return self.company_name

    class Meta:
        db_table = "suppliers"    
        managed = False

# product categories
class Categories(models.Model):
    category_id = models.SmallIntegerField(primary_key=True)   
    category_name = models.CharField(max_length=250, blank=False)           
    description = models.TextField()                             
    picture = models.BinaryField()                              # Match the bytea type

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = "categories"  # Specify the existing table name
        managed = False  # Prevent Django from trying to create or delete this table
                   
# available products
class Products(models.Model):
    product_id = models.SmallIntegerField(primary_key=True, blank=False)   #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products", null=True)
    product_name = models.CharField(max_length=250, blank=False)
    supplier_id = models.ForeignKey(Suppliers, on_delete=models.RESTRICT, db_column='supplier_id') 
    category_id = models.ForeignKey(Categories, on_delete=models.RESTRICT, db_column='category_id') 
    quantity_per_unit = models.CharField(max_length=250)
    unit_price = models.FloatField()  
    units_in_stock = models.PositiveSmallIntegerField()   
    units_on_order = models.PositiveSmallIntegerField()  
    reorder_level = models.PositiveSmallIntegerField()  
    discontinued = models.IntegerField(blank=False)  
    
    def __str__(self):
        return self.product_name

    class Meta:
        db_table = "products"    
        managed = False
            
# customers
class Customers(models.Model):
    customer_id = models.CharField(primary_key=True, blank=False)
    company_name = models.CharField(max_length=250, blank=False)
    contact_name = models.CharField(max_length=250)
    contact_title = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)         
    region = models.CharField(max_length=250)       
    postal_code = models.CharField(max_length=250)   
    country = models.CharField(max_length=250)       
    phone = models.CharField(max_length=250)
    fax = models.CharField(max_length=250)
   

    def __str__(self):
        return self.company_name

    class Meta:
        db_table = "customers"    
        managed = False
                
# employees
class Employees(models.Model):
    employee_id = models.SmallIntegerField(primary_key=True, blank=False)
    last_name = models.CharField(max_length=250, blank=False)
    first_name = models.CharField(max_length=250, blank=False)
    title = models.CharField(max_length=250)
    title_of_courtesy = models.CharField(max_length=250)
    birth_date = models.DateField(null=True, blank=True)
    hire_date = models.DateField(auto_now=True)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)          
    region = models.CharField(max_length=250)        
    postal_code = models.CharField(max_length=250)   
    country = models.CharField(max_length=250)       
    home_phone = models.CharField(max_length=250)
    extension = models.CharField(max_length=250)
    photo = models.BinaryField()     
    notes = models.TextField()
    reports_to = models.ForeignKey("self", on_delete=models.RESTRICT, db_column='reports_to', null=True, blank=True)
    photo_path = models.CharField(max_length=250)

    def __str__(self):
        return self.title + " " + self.first_name + " " + self.last_name

    class Meta:
        db_table = "employees"    
        managed = False
                    
# product, price and quantity of said product found in an order
class Order_details(models.Model):
    order_id = models.ForeignKey("Orders", on_delete=models.RESTRICT, blank=False, db_column='order_id') 
    product_id = models.ForeignKey(Products, on_delete=models.RESTRICT, blank=False, db_column='product_id') 
    unit_price = models.DecimalField(max_digits=9, decimal_places=2, blank=False)  
    quantity = models.PositiveSmallIntegerField(blank=False)
    discount = models.DecimalField(max_digits=4, decimal_places=2, blank=False)  #percentage 

    def __str__(self):
        return self.order_id

    class Meta:
        db_table = "order_details"    
        managed = False
                
# available shiping companies
class Shippers(models.Model):
    shipper_id = models.SmallIntegerField(primary_key=True, blank=False)
    company_name = models.CharField(max_length=250, blank=False)
    phone = models.CharField(max_length=250)    

    def __str__(self):
        return self.company_name

    class Meta:
        db_table = "shippers"    
        managed = False
                   
# orders
class Orders(models.Model):
    order_id = models.SmallIntegerField(primary_key=True)
    customer_id = models.ForeignKey(Customers, on_delete=models.RESTRICT, db_column='customer_id') 
    employee_id = models.ForeignKey(Employees, on_delete=models.RESTRICT, db_column='employee_id') 
    order_date = models.DateField(null=True, blank=True)
    required_date = models.DateField(null=True, blank=True)
    shipped_date = models.DateField(null=True, blank=True)
    ship_via = models.ForeignKey(Shippers, on_delete=models.RESTRICT, db_column='ship_via') 
    freight = models.FloatField()
    ship_name = models.CharField(max_length=250)
    ship_address = models.CharField(max_length=250)         # create/find list of & add to db?
    ship_city = models.CharField(max_length=250)       # create/find list of & add to db?
    ship_region = models.CharField(max_length=250)  # create/find list of & add to db?
    ship_postal_code = models.CharField(max_length=250)  # create/find list of & add to db?
    ship_country = models.CharField(max_length=250)      # create/find list of & add to db?
  
    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "orders"    
        managed = False
                
#  demographics
class Customer_demographics(models.Model):
    customer_type_id = models.CharField(primary_key=True, max_length=250, blank=False)
    customer_desc = models.TextField()
   

    def __str__(self):
        return self.customer_type_id

    class Meta:
        db_table = "customer_demographics"    
        managed = False
                
# demographic of given customer
class Customer_customer_demo(models.Model):
    customer_id = models.ForeignKey(Customers, on_delete=models.RESTRICT, blank=False, db_column='customer_id') 
    customer_type_id = models.ForeignKey(Customer_demographics, on_delete=models.RESTRICT,  blank=False, db_column='customer_type_id') 
   
    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "customer_customer_demo"    
        managed = False
                
# states
class Us_states(models.Model):
    state_id = models.SmallIntegerField(primary_key=True, blank=False)
    state_name = models.CharField(max_length=250)
    state_abbr = models.CharField(max_length=250)
    state_region = models.CharField(max_length=250)
    

    def __str__(self):
        return self.state_name

    class Meta:
        db_table = "us_states"    
        managed = False
                
# regions
class Region(models.Model):
    region_id = models.SmallIntegerField(primary_key=True, blank=False)
    region_description = models.CharField(max_length=250, blank=False)
           
    def __str__(self):
        return self.region_description

    class Meta:
        db_table = "region"    
        managed = False
                    
# territories
class Territories(models.Model):
    territory_id = models.CharField(max_length=250, primary_key=True, blank=False)
    territory_description = models.CharField(blank=False)
    region_id = models.ForeignKey(Region, on_delete=models.RESTRICT, db_column='region_id')
       
    def __str__(self):
        return self.territory_description


    class Meta:
        db_table = "territories"    
        managed = False
                
# territory related employee finds themselves in
class Employee_territories(models.Model):
    territory_id = models.ForeignKey(Territories, on_delete=models.RESTRICT, blank=False, db_column='territory_id') 
    employee_id = models.ForeignKey(Employees, on_delete=models.RESTRICT, blank=False, db_column='employee_id')     

    def __str__(self):
        return str(self.id)
    

    class Meta:
        db_table = "employee_territories"    
        managed = False
                




# models not a part of initial imported database
class ProductList(models.Model):
    product_list_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    name = models.CharField(max_length=255, null=True, blank=True)  
    created_at = models.DateTimeField(null=True, blank=True)   #auto_now_add=True

    class Meta:
        db_table = "product_lists"  
        managed = True   

    def __str__(self):
        return f"{self.name} - {self.user.username}"   


class ProductListEntry(models.Model):
    entry_id = models.AutoField(primary_key=True)
    product_list = models.ForeignKey(ProductList, on_delete=models.CASCADE, related_name='product_list')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_entries')

    class Meta:
        db_table = "product_list_entries"   
        managed = True  

    def __str__(self):
        return f"{self.product_list.name} - {self.product.product_name}"