from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories, name = 'categories'),
    path('categories/<category_name>/', views.category_details, name = 'category_detail'),
    path('categories/<category_name>/<product_name>/', views.product_details, name = 'product'),
    path('cart/', views.cart, name = 'cart'),
]

# - **Category pages**
#   - There should be a separate page for each of the various product categories (e.g. "Home", "Kitchen", "Bed & Bath", "Office", etc...)
#   - These pages should show various (at least 3 per category) products with images, names, and prices. This data should come from the Django server (i.e. don't hardcode them into your HTML pages) 
#   - These pages should allow users to add products to their virtual shopping cart. The shopping cart should be persisted using CSV files, which are read and written using Django. 

