# cash register with GUI

from tkinter import *
from tkinter import messagebox 
from tktable import Table 
from CashRegisterModules.GUI import *

screen_width = "700"
screen_height = "500"

# create root window
root_window = Tk()
root_window.title("Coop Online Supermatket App")

# set window dimensions -> what the fn parameters do ("widthxheight+x+y") 
root_window.geometry(f"{screen_width}x{screen_height}")
center_window(root_window, screen_width, screen_height)

def btn_click():
    messagebox.showinfo("Hii")


Label(root_window, text = "Insert Product ID:").grid(row = 0, column = 0)
product_id = Entry(root_window).grid(row = 0, column = 1)
Button(root_window, text = "Add to cart", command = btn_click).grid(row = 0, column = 2)

product_table = Table(root_window, ("Hi", "Hi")).grid(row = 1, column = 0)

# Execute Tkinter mainloop
root_window.mainloop()