#  A cash register with GUI

from customtkinter import *

import cashregister.CashRegisterGUI as gui
import cashregister.CashRegisterLogic as core

screen_width = 700
screen_height = 500


# header for the product list
header =["ID:", "Name:", "Price:", "Currency:"]

# create root window
app = CTk()
app.title("Coop Online Supermatket App")

# set window dimensions
gui.set_window(app, screen_width, screen_height, app._get_window_scaling())


# Execute tkinter mainloop
app.mainloop()