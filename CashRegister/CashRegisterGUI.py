# cash register with GUI

from tkinter import *
from CashRegisterModules.GUI import *

screen_width = "700"
screen_height = "500"

# create root window
root_window = Tk()
root_window.title("Coop Online Supermatket App")

# set window dimensions -> what the fn parameters do ("widthxheight+x+y") 
root_window.geometry(f"{screen_width}x{screen_height}")
center_window(root_window, screen_width, screen_height)

# Execute Tkinter mainloop
root_window.mainloop()