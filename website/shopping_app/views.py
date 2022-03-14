from django.shortcuts import render
from django.http import HttpResponse
from .models import Store

store = Store('Buy-it')


#home page lists category link and cart link
def home(request):
    my_data = {
        "store": store.name
    }
    return render(request, 'shopping/home.html', my_data)

#category pages lists links to all categories
def categories(request):
    my_data = {
        'categories': store.categories
    }
    return render(request, 'shopping/categories.html', my_data)

#category_detail lists links to all products in that category
def category_details(request, category_name):
    products = store.find_product_by_category(category_name)
    my_data = {
        'products': products
    }
    return render(request, 'shopping/category_details.html', my_data)

#product_detail shows detail for that product and link to add to cart
def product_details(request, category_name, product_name):
    product_details = store.get_product_details(product_name)
    my_data = {
        'product_details': product_details
    }
    return render(request, 'shopping/product_details.html', my_data)


def cart(request):
    return HttpResponse('cart page')
