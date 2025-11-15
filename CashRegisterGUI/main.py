#  A cash register with GUI

from customtkinter import *

import cashregister.CashRegisterGUI as gui
import cashregister.CashRegisterLogic as core

screen_width = 910
screen_height = 550

# create root window
app = CTk()
app.title("Cash Register")

# set window dimensions
gui.set_window(app, screen_width, screen_height, app._get_window_scaling())

# configure FRAMES -> returns dict with frames (table, cart, product_id)
frames: dict = gui.configure_frames(app)

# FRAME product_id - widgets
add_product_btn: CTkButton = gui.configure_add_product_button(frames["product_id"])
product_id_label: CTkLabel = gui.configure_product_id_label(frames["product_id"])
product_id_entry: CTkEntry = gui.configure_product_id_entry(frames["product_id"])

# FRAME table - widgets
tab_view: CTkTabview = gui.configure_tab_view(frames["table"])
# configures TABS -> returns dict with tabs (all_products, fruits, vegetables, bakery, other)
all_tabs: dict = gui.configure_tabs(tab_view)

# FRAME cart - widgets
cart_label: CTkLabel = gui.configure_cart_label(frames["cart"])
cart_frame: CTkFrame = gui.configure_cart_frame(frames["cart"])
cart_total_label: CTkLabel = gui.configure_cart_total_label(frames["cart"])
cart_sum_label: CTkLabel = gui.configure_cart_sum_label(frames["cart"])
cart_buy_btn: CTkButton = gui. configure_buy_button(frames["cart"])

value = [[1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5]]

# Execute tkinter mainloop
app.mainloop()