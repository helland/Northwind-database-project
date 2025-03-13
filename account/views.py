from django.shortcuts import render
from main.models import ProductList
from django.contrib.auth.decorators import login_required
from northwind.settings import LOGIN_REDIRECT_URL

# Create your views here.
@login_required(login_url=LOGIN_REDIRECT_URL)
def my_product_lists(request):
    if request.user.is_authenticated:
        # Retrieve all product lists for the logged-in user
        product_lists = ProductList.objects.filter(user=request.user)
    else:
        product_lists = []  # No lists if the user is not authenticated

    return render(request, 'account/product_lists.html', {
        'product_lists': product_lists,
    })

@login_required(login_url=LOGIN_REDIRECT_URL)   
def view_product_list(request, product_list_id):
    product_list = ProductList.objects.get(product_list_id=product_list_id)
    product_entries = product_list.product_list.all()  # Get related entries

    # Retrieve detailed product information
    products = []
    for entry in product_entries:
        product = entry.product  # Get the product associated with the entry
        products.append({
            'product_id': product.product_id,
            'product_name': product.product_name,
            'unit_price': product.unit_price,
            'units_in_stock': product.units_in_stock,
            'supplier_name': product.supplier_id.company_name,
            'category_name': product.category_id.category_name,
        })

    return render(request, 'account/product_list_detail.html', {
        'product_list': product_list,
        'products': products,  # Pass the detailed product information to the template
    }) 
      
'''    
def view_product_list(request, product_list_id):
    product_list = ProductList.objects.get(product_list_id=product_list_id)
    product_entries = product_list.product_list.all()  # Get related entries

    return render(request, 'account/product_list_detail.html', {
        'product_list': product_list,
        'product_entries': product_entries,
    })
'''