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

class Products:

    def __init__(self, name, description, price, category, image):
        self.name = name
        self.description = description 
        self.price = price
        self.category = category
        self.image = image

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

    def save_to_cart(self, data):
        FILE_PATH = '../data/cart.csv'
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, FILE_PATH)

        with open(path, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = ['product', 'quantity', 'price'])
            writer.writeheader()
            for object in self.cart:
                data_dict = object.__dict__
                writer.writerow(data_dict)

    def add_to_cart(self, product_name, product_price):
        product_data = {}
        product_data['product'] = product_name
        product_data['quantity'] = 1
        product_data['price'] = product_price

        
        self.cart.append(Cart(**product_data))
        self.save_to_cart(Cart(**product_data))

        return product_data
        
    def get_image(self, product_name):
        if product_name == 'Skillet':
            path = 'images/Skillet/Skillet.jpeg'
        if product_name == 'Step Stool':
            path = 'images/Step Stool/step_stool.jpeg'
        if product_name == 'tshirt':
            path = 'images/tshirt/tshirt.jpeg'
        if product_name == 'TV':
            path = 'images/TV/tv.jpeg'
        if product_name == 'Harry Potter and the Prisoner of Azkaban':
            path = 'images/Harry Potter and the Prisoner of Azkaban/hp.jpeg'
        if product_name == 'Plumaria Fertilizer':
            path = 'images/Plumaria Fertilizer/fertilizer.jpeg'
        if product_name == 'Monopoly':
            path = 'images/Monopoly/mon.jpeg'
        if product_name == 'Kettle':
            path = 'images/Kettle/kettle.jpeg'
        if product_name == 'pants':
            path = 'images/pants/pants.jpeg'
        if product_name == 'Glasses':
            path = 'images/Glasses/glass.jpeg'
        if product_name == 'Sound Bar':
            path = 'images/Sound Bar/sound.jpeg'
        if product_name == 'Pots':
            path = 'images/Pots/pots.jpeg'
        if product_name == 'Aja by Steely Dan':
            path = 'images/Aja by Steely Dan/record.jpeg'
        if product_name == 'Mario Party':
            path = 'images/Mario Party/mario.jpeg'
        if product_name == 'Untamed by Glennon Doyle':
            path = 'images/Untamed by Glennon Doyle/book.jpeg'
        if product_name == 'Basketball':
            path = 'images/Basketball/basketball.jpeg'
        return path
