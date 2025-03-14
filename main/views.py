from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import RegisterForm, LoginForm, ProductSelectionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from northwind.settings import LOGIN_REDIRECT_URL
from django.utils import timezone
from django.db.models import Prefetch
from django.db.models import F, Sum

# Create your views here.


def home(request):
    return render(request, "main/home.html",{}) 



def orders_place(request):
    # request.user() get user from inside the code
    #if request.method == "POST":
        #form = Orders(request.POST)
        
        #if form.is_valid():
             
            #n = form.cleaned_data["name"]
            #t = ToDoList(name=n)
            #t.save()
            #response.user.todolist.add(t)
        
        #return HttpResponseRedirect("/%i" %t.id)
        
    #else:
    #    form = Orders()
        
    return render(request, "main/orders_create.html", {})   #"form":form

@login_required(login_url=LOGIN_REDIRECT_URL) 
def orders_view(request):
    # Create a custom queryset that combines Orders, Order_details, and Products
    order_details = (
        Order_details.objects
        .select_related('product_id', 'order_id__customer_id')  # Join with Products and Orders
        .values(
            'order_id', 
            'product_id', 
            'product_id__product_name', 
            'order_id__customer_id__company_name', 
            'quantity', 
            'unit_price'
        )
    )

    # Handle sorting
    sort_by = request.GET.get('sort_by', 'order_id')  # Default sort by order_id
    sort_order = request.GET.get('sort_order', 'asc')  # Default sort order

    # Map the sort_by to the correct field names
    if sort_by == 'customer_name':
        sort_by = 'order_id__customer_id__company_name'
    elif sort_by == 'product_name':
        sort_by = 'product_id__product_name'

    if sort_order == 'desc':
        sort_by = '-' + sort_by  # Prefix with '-' for descending order

    # Sort the queryset
    order_details = order_details.order_by(sort_by)

    return render(request, "main/orders_view.html", {
        "order_details": order_details,
        "sort_by": sort_by,
        "sort_order": sort_order
    })
  
# overview of demographics
@login_required(login_url=LOGIN_REDIRECT_URL) 
def demo_view(request):
    demographic = Customer_demographics.objects.all()
    return render(request, "main/customer_demographics_view.html", {"demographic": demographic})  

# overview of demographics
@login_required(login_url=LOGIN_REDIRECT_URL) 
def misc(request):
    return render(request, "main/misc.html", {})  
  
      
# overview of orders in detail
@login_required(login_url=LOGIN_REDIRECT_URL) 
def order_details_view(request):
    order_details = Order_details.objects.all()
    return render(request, "main/order_details_view.html", {"order_details": order_details})  
    
    
# overview of all suppliers
def suppliers_view(request):
    suppliers = Suppliers.objects.all()
    
    return render(request, "main/suppliers_view.html", {"suppliers": suppliers})  

# overview of all products
def products_view(request):
    products = Products.objects.all()
    '''
    #if request.method == "POST":
    #    if request.POST.get("save"):
    #        for item in products.item_set.all()
    #            if request.POST.get(f"c{item.id}") == "clicked":
    #                item.complete = True
    #            else:
    #                item.complete = False
    #            item.save()        
    #    elif request.POST.get("newItem"):
    #            txt = response.POST.get("new")             
    #            if len(txt) > 2:
    #                ls.item_set.create(text=txt, complete=False)
    #            else:
    #                print("invalid")
    '''                
    return render(request, "main/products_view.html", {"products": products})  

# get certain products
def products_get(request):
    products = Products.objects.all()
    suppliers = Suppliers.objects.all()   
    return render(request, "main/shippers_view.html", {})  



def create_product_list(request):
    list_name = request.session.get('list_name', '')
    
    if request.method == 'POST':
        form = ProductSelectionForm(request.POST)
        if form.is_valid():
            product = form.cleaned_data['product']
            list_name = form.cleaned_data['list_name']        
                
            # Store the selected product and name in the session
            if 'selected_products' not in request.session:
                request.session['selected_products'] = []
            request.session['selected_products'].append(product.product_id)
            request.session.modified = True
            request.session['list_name'] = list_name
            
            # Check which button was clicked
            action = request.POST.get('action')
            if action == 'save':
                return redirect('save-product-list')  # Redirect to save the list
            else:
                return redirect('create-product-list')  # Redirect to the same view
    else:
        form = ProductSelectionForm()

    # Retrieve selected products
    selected_product_ids = request.session.get('selected_products', [])
    selected_products = Products.objects.filter(product_id__in=selected_product_ids)

    return render(request, 'main/product_selection.html', {
        'form': form,
        'selected_products': selected_products,
        'list_name': list_name,
    })
    
def save_product_list(request):
    list_name = request.session.get('list_name', '')
    selected_product_ids = request.session.get('selected_products', [])
    now = timezone.now()
    
    if not list_name or list_name == None or list_name.lower() =='none':
        list_name = f"product-list-{now.year}-{now.month}-{now.day}-{now.hour}-{now.minute}"
    
    
    # create product list
    if list_name and selected_product_ids:
        product_list = ProductList.objects.create(user=request.user, name=list_name, created_at=now)
        
        # add  ProductListEntry entries to the list
        for product_id in selected_product_ids:
            product = Products.objects.get(product_id=product_id)
            ProductListEntry.objects.create(product_list=product_list, product=product)  
        
        # Clear the session
        del request.session['selected_products']
        del request.session['list_name']
        messages.info(request, "Product list was successfully created!")
        return redirect('create-product-list')  
    return redirect('create-product-list')  

# overview of all categories
def categories_view(request):
    categories = Categories.objects.all()
    return render(request, "main/categories_view.html", {"categories":categories})  

# overview of all customers
@login_required(login_url="registration/login.html") 
def customers_view(request):
    customers = Customers.objects.all()
    return render(request, "main/customers_view.html", {"customers":customers})  

# overview of all employees
@login_required(login_url="registration/login.html") 
def employees_view(request):
    employees = Employees.objects.all()
    return render(request, "main/employees_view.html", {"employees":employees})  

# overview of all shipping companies
def shippers_view(request):
    shippers = Shippers.objects.all()
    return render(request, "main/shippers_view.html", {"shippers":shippers})  


    
# register new user    
def sign_up(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(user)
            return redirect("/home")
        
    else:
        form = RegisterForm()
        
    return render(request, "registration/sign_up.html", {"form": form})    
    
# log in         
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)   
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth_login(request, user)   
                return redirect("/")
            else:
                pass #messages.info(request, "Username OR password is incorrect")
    else:
        form = LoginForm()  # Create an empty form  

    return render(request, "registration/login.html", {"form": form})
# log out
#def logout(request):
#    logout(request)
#    return redirect(request, "registration/login.html", { })        