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
# configure frames
gui.configure_frame(app)

insert_product_id_label = CTkLabel(app, text = "Insert product ID:")
product_id_entry = CTkEntry(app)
def button_event():
    print("button pressed")
add_product_btn = CTkButton(app, text = "Add to cart", command = button_event)

value = [[1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5]]

# Execute tkinter mainloop
app.mainloop()