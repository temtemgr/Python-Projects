#  A cash register with GUI

from customtkinter import *
from tkinter import messagebox

from cashregister import gui as gui
from cashregister import data as data
from cashregister import logic as core

screen_width = 910
screen_height = 550

# Initialize UI

# create root window
app = CTk()
app.title("Cash Register")

# set window dimensions
gui.set_window(app, screen_width, screen_height, app._get_window_scaling())

# configure FRAMES -> returns dict with frames (table, cart, product_id)
frames: dict = gui.configure_frames(app, screen_height)

# FRAME product_id - widgets
product_id_label: CTkLabel = gui.configure_product_id_label(frames["product_id"])
product_id_entry: CTkEntry = gui.configure_product_id_entry(frames["product_id"])
add_product_btn: CTkButton = gui.configure_add_product_button(frames["product_id"])

# FRAME table - widgets
tab_view: CTkTabview = gui.configure_tab_view(app)
# configures TABS -> returns dict with tabs (all_products, fruits, vegetables, bakery, other)
all_tabs: dict = gui.configure_tabs(tab_view)

# FRAME cart - widgets
cart_label: CTkLabel = gui.configure_cart_label(app)
cart_frame: CTkFrame = gui.configure_cart_frame(app)
cart_total_label: CTkLabel = gui.configure_cart_total_label(app)
cart_sum_label: CTkLabel = gui.configure_cart_sum_label(app)
cart_buy_btn: CTkButton = gui.configure_buy_button(app)

# Handle logic

# add product btn eventlistener
# lambda wraps code in a separate function
# we need to do this since command expects a function to call instead of just code to run
add_product_btn.configure(command = lambda: add_product(product_id_entry.get()))

# cart buy btn eventlistener
cart_buy_btn.configure(command = lambda: buy_products())

# displays all products
def display_products(tab: CTkFrame):
    display_header(tab)

    for i, product in enumerate(data.products):
        for j, value in enumerate(product.values()):
            gui.configure_table_row(tab, value, j, i + 1)

# displays header
def display_header(tab: CTkFrame):
    for i, h in enumerate(data.header):
        gui.configure_table_row(tab, h, i, 0)

# displays all the products
display_products(all_tabs["all_products"])

# adds product to cart table
def add_product(product_name: str):
    global product_id_entry
    for product in data.products:
        if product["id"] == int(product_name):
            data.cart.append({
                "name": product["name"],
                "price": product["price"],
                "currency": product["currency"]
            })
            update_products_in_cart()
            product_id_entry.delete(0, END)

# displays added product in cart
def update_products_in_cart():
    for i, item in enumerate(data.cart):
        for j, value in enumerate(item.values()):
            gui.configure_table_row(cart_frame, value, j, i + 1)
    sum = core.calc_sum(data.cart)
    cart_sum_label.configure(text = f"{sum} CHF")

# buys products
def buy_products():
    if int(core.calc_sum(data.cart)) != 0:
        messagebox.showinfo("Receipt", f"Total: {cart_sum_label._text}\n\n- I hate tkinter based UI")
    data.cart = []
    update_products_in_cart()
    # destroys all the widgets
    for widget in cart_frame.winfo_children():
        widget.destroy()

# Execute tkinter mainloop
app.mainloop()