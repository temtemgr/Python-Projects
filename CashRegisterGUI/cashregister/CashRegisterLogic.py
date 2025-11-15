# a file for cash register logic

import json
from customtkinter import *
import cashregister.CashRegisterGUI as gui

# header for the product list
header = ["Article Number:", "Name:", "Price:", "Currency:"]

# load data
products_JSON = open("CashRegisterGUI\cashregister\data\Products.json")
products = json.load(products_JSON)

# displays all products
def display_products(tab: CTkFrame):
    display_header(tab)

    for i, product in enumerate(products):
        for j, value in enumerate(product.values()):
            gui.configure_table_row(tab, value, j, i + 1)

# displays header
def display_header(tab: CTkFrame):
    global header
    for i, h in enumerate(header):
        gui.configure_table_row(tab, h, i, 0)