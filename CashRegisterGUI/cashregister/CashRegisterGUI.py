# a file for gui logic

from customtkinter import *
import cashregister.CashRegisterLogic as core

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
def configure_frames(window: CTk):
    product_table_frame = CTkFrame(window, width = 500, height = 480, corner_radius = 0, fg_color= "#242424")
    shopping_cart_frame = CTkFrame(window, width = 300, height = 550,border_width = 3, border_color = "#1e1e1e",corner_radius = 0,fg_color= "#242424")
    product_id_frame = CTkFrame(window, width = 500, height = 70, corner_radius = 0)
    # sticky makes it stick to a side: north, east, south, west
    product_table_frame.grid(column = 0, row = 0, sticky = "NSEW")
    shopping_cart_frame.grid(column = 1, row = 0, sticky = "NSEW", rowspan = 2)
    product_id_frame.grid(column = 0, row = 1, sticky = "NSEW")

    product_id_frame.rowconfigure(0, weight = 1)
    
    window.columnconfigure((0,1), weight = 1)
    window.rowconfigure((0,1), weight = 1)
    return {"table": product_table_frame, "cart": shopping_cart_frame, "product_id": product_id_frame}

# FRAME product_id - widgets

# sets add_product button
def configure_add_product_button(frame: CTkFrame):
    btn = CTkButton(frame, text = "Add", command = core.add_product, width = 60, corner_radius = 50, text_color = "Black")
    return btn.grid(column = 3, row = 0, padx = 20)

# sets product_id label
def configure_product_id_label(frame: CTkFrame):
    label = CTkLabel(frame, text = "Article Number:")
    return label.grid(column = 0, row  = 0, sticky = "EW", padx = (30, 10), pady = 10)

# sets product_id entry
def configure_product_id_entry(frame: CTkFrame):
    return CTkEntry(frame, width = 160).grid(column = 1, row = 0, sticky = "W")
