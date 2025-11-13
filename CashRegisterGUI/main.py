# cash register with GUI

from customtkinter import *

import json
from CashRegisterModules.GUI import *

screen_width = "700"
screen_height = "500"

# theme

set_default_color_theme("green")
set_appearance_mode("dark")

# load data
products_JSON = open("Cashregister\Products.json")
products = json.load(products_JSON)

# header for the product list
header =["ID:", "Name:", "Price:", "Currency:"]

# create root window
root_window = CTk()
root_window.title("Coop Online Supermatket App")

# set window dimensions -> what the fn parameters do ("widthxheight+x+y") 
root_window.geometry(f"{screen_width}x{screen_height}")
center_window(root_window, screen_width, screen_height)



def btn_click():
    print("hi")


# Label(root_window, text = "Insert Product ID:").grid(row = 0, column = 0)
product_id = Entry(root_window).grid(row = 0, column = 1)
# Button(root_window, text = "Add to cart", command = btn_click).grid(row = 0, column = 2)

# product_table = Table(root_window, header).grid(row = 1, column = 0)

# Execute tkinter mainloop
root_window.mainloop()