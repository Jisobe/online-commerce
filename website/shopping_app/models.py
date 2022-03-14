from unicodedata import category, name
from django.db import models
import os
import csv

class Categories:

    def __init__(self, name, description):
        self.name = name
        self.decription = description

    @classmethod
    def load_all(cls):
        FILE_PATH = '../data/categories.csv'
        categories = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(my_path, FILE_PATH)
        
        with open(file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                categories.append(cls(**dict(row)))

        return categories

class Customers:

    def __init__(self, account_number, first_name, last_name, email, cart):
        self.account_no = account_number
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.cart = cart

    @classmethod
    def load_all(cls):
        FILE_PATH = '../data/customers.csv'
        customers = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(my_path, FILE_PATH)
        
        with open(file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                customers.append(cls(**dict(row)))

        return customers

class Orders:

    def __init__(self, order_num, order_date, ship_date, delivery_date, customer_id, shipping_address):
        self.order_num = order_num
        self.order_date = order_date 
        self.ship_date = ship_date
        self.delivery_date = delivery_date
        self.customer_id = customer_id
        self.shipping_address = shipping_address

    @classmethod
    def load_all(cls):
        FILE_PATH = '../data/orders.csv'
        orders = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(my_path, FILE_PATH)
        
        with open(file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                orders.append(cls(**dict(row)))

        return orders

class Products:

    def __init__(self, name, description, price, category):
        self.name = name
        self.description = description 
        self.price = price
        self.category = category

    @classmethod
    def load_all(cls):
        FILE_PATH = '../data/products.csv'
        products = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(my_path, FILE_PATH)
        
        with open(file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                products.append(cls(**dict(row)))

        return products

class Cart:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    @classmethod
    def load_all(cls):
        FILE_PATH = '../data/cart.csv'
        cart = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(my_path, FILE_PATH)
        
        with open(file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cart.append(cls(**dict(row)))

        return cart

    def save_to_cart(self):
        FILE_PATH = '../data/cart.csv'
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, FILE_PATH)

        with open(self.file_path_to_save_all(path), 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = ['product', 'quantity', 'price'])
            writer.writeheader()
            for object in self.customers:
                data_dict = object.__dict__
                writer.writerow(data_dict)

class Store:
    def __init__(self, name):
        self.name = name
        self.categories = Categories.load_all()
        self.products = Products.load_all()
        self.orders = Orders.load_all()
        self.customers = Customers.load_all()
        self.cart = Cart.load_all()

    def find_product_by_category(self, category_name):
        products = []
        for product in self.products:
            if product.category == category_name:
                products.append(product)
            
        return products

    def get_product_details(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product
        return None

    def add_to_cart(self, product_name):
        
