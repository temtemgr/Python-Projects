# a file to handle data

import json

# load data
products_JSON = open(".data\Products.json")
products = json.load(products_JSON)

# header for the product list
header = ["Article Number:", "Name:", "Price:", "Currency:"]

# products in cart
cart = []
