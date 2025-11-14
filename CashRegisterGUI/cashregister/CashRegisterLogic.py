# a file for cash register logic

import json

# header for the product list
header =["ID:", "Name:", "Price:", "Currency:"]

# load data
products_JSON = open("Cashregister\Products.json")
products = json.load(products_JSON)