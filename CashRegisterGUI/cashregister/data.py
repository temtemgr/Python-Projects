# a file to handle data

import os
import json

# load data
products_JSON = open(f"{os.path.dirname(__file__)}/data/Products.json")
products = json.load(products_JSON)

# header for the product list
header = ["Article Number:", "Name:", "Price:", "Currency:"]

# products in cart
cart = []
