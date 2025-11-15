#  A cash register with GUI

from customtkinter import *

import cashregister.CashRegisterGUI as gui
import cashregister.CashRegisterLogic as core

screen_width = 800
screen_height = 550

# create root window
app = CTk()
app.title("Cash Register")

# set window dimensions
gui.set_window(app, screen_width, screen_height, app._get_window_scaling())
# configure frames -> returns dict with frames (table, cart, product_id)
frames: dict = gui.configure_frames(app)

# FRAME product_id - widgets
add_product_btn: CTkButton = gui.configure_add_product_button(frames["product_id"])
product_id_label: CTkLabel = gui.configure_product_id_label(frames["product_id"])
product_id_entry: CTkEntry = gui.configure_product_id_entry(frames["product_id"])


value = [[1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5]]

# Execute tkinter mainloop
app.mainloop()