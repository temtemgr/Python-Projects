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

# sets all frames
def configure_frames(window: CTk):
    product_table_frame = CTkFrame(window, width = 450, height = 480, corner_radius = 0, fg_color= "#242424")
    shopping_cart_frame = CTkFrame(window, width = 350, height = 550, border_width = 3, border_color = "#1e1e1e", corner_radius = 0, fg_color= "#242424")
    product_id_frame = CTkFrame(window, width = 450, height = 70, corner_radius = 0)
    # sticky makes it stick to a side: north, east, south, west
    product_table_frame.grid(column = 0, row = 0, sticky = "NSEW")
    shopping_cart_frame.grid(column = 1, row = 0, sticky = "NSEW", rowspan = 2)
    product_id_frame.grid(column = 0, row = 1, sticky = "NSEW")
    # weight = 1 gives a specific column/row the maximum width/height of the frame
    product_id_frame.rowconfigure(0, weight = 1)
    product_table_frame.columnconfigure(0, weight = 1)
    product_table_frame.rowconfigure(0, weight = 1)
    shopping_cart_frame.rowconfigure(2, weight = 1)
    
    window.columnconfigure((0,1), weight = 1)
    window.rowconfigure((0,1), weight = 1)
    return {"table": product_table_frame, "cart": shopping_cart_frame, "product_id": product_id_frame}

# FRAME product_id - widgets

# sets add_product button
def configure_add_product_button(frame: CTkFrame):
    btn = CTkButton(frame, text = "Add", width = 60, corner_radius = 50, fg_color = "#383838", border_color = "grey", border_width = 1)
    btn.grid(column = 2, row = 0, padx = 20)
    return btn

# sets product_id label
def configure_product_id_label(frame: CTkFrame):
    label = CTkLabel(frame, text = "Article Number:")
    label.grid(column = 0, row  = 0, sticky = "EW", padx = (30, 10), pady = 10)
    return label

# sets product_id entry
def configure_product_id_entry(frame: CTkFrame):
    entry = CTkEntry(frame, width = 160)
    entry.grid(column = 1, row = 0, sticky = "W")
    return entry

# FRAME table - widgets

# sets table tabview
def configure_tab_view(frame: CTkFrame):
    tab_view: CTkTabview = CTkTabview(frame, width = 550, height = 460, segmented_button_selected_color = "#696969", segmented_button_selected_hover_color = "#696969")
    tab_view.grid(column = 0, row = 0, padx = 15, pady = 5)
    return tab_view

# sets table rows in tab
def configure_table_row(table, text, column, row):
    label = CTkLabel(table, text = text)
    label.grid(column = column, row  = row, sticky = "W", padx = 20, pady = 10)

# sets all tabs
def configure_tabs(tab_view: CTkTabview):
    all_products = tab_view.add("All Products")
    all_products.grid_columnconfigure((0,1,2,3), weight = 1)

    # sets as default tab
    tab_view.set("All Products")

    return {
        "all_products": all_products, 
        "fruits": tab_view.add("Fruits"), 
        "vegetables": tab_view.add("Vegetables"), 
        "bakery": tab_view.add("Bakery"), 
        "other": tab_view.add("Other")
    }

# FRAME cart - widgets

# sets cart label
def configure_cart_label(frame: CTkFrame):
    label = CTkLabel(frame, text = "Shopping Cart")
    label.grid(column = 0, row  = 0, sticky = "W", padx = 20, pady = (15, 10), columnspan = 3)
    return label

# sets cart frame
def configure_cart_frame(frame: CTkFrame):
    cart_frame = CTkFrame(frame, width = 300, height = 421)
    cart_frame.grid_configure(padx = 32),
    cart_frame.grid(column = 0, row = 1, sticky = "NSEW", columnspan = 3)
    return cart_frame

# sets cart total label
def configure_cart_total_label(frame: CTkFrame):
    label = CTkLabel(frame, text = "Total:")
    label.grid(column = 0, row  = 2, sticky = "SW", padx = (30,0), pady = 20,)
    return label

# sets cart sum label
def configure_cart_sum_label(frame: CTkFrame):
    label = CTkLabel(frame, text = "0  CHF")
    label.grid(column = 1, row  = 2, sticky = "SW", padx = 10, pady = 20,)
    return label

# sets buy button
def configure_buy_button(frame: CTkFrame):
    btn = CTkButton(frame, text = "Buy", width = 60, corner_radius = 50, text_color = "Black")
    btn.grid(column = 2, row = 2, padx = 40, pady = 20, sticky = "SE")
    return btn