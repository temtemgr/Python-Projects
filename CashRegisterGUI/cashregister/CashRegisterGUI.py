# a file for gui logic

from customtkinter import *

# theme
set_default_color_theme("green")
set_appearance_mode("dark")

# sets windeow with centering it and setting dimensions
def set_window(window: CTk, window_width: int, window_height: int, scale: float):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width - window_width) // 2 * scale)
    y = int((screen_height - window_height) // 2.5 * scale)
# x and y are the coordinates where the window will spawn
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# sets Frame and grid
def configure_frame(window: CTk):
    product_table_frame = CTkFrame(window, width = 550, height = 450, border_width = 2)
    shopping_cart_frame = CTkFrame(window, width = 350, height = 550,border_width = 2)
    product_id_frame = CTkFrame(window, width = 550, height = 100, border_width = 2)
    # sticky makes it stick to a side: north, east, south, west
    product_table_frame.grid(column = 0, row = 0, sticky = "NSEW")
    shopping_cart_frame.grid(column = 1, row = 0, sticky = "NSEW", rowspan = 2)
    product_id_frame.grid(column = 0, row = 1, sticky = "NSEW")

    window.columnconfigure((0,1), weight = 1)
    window.rowconfigure((0,1), weight = 1)