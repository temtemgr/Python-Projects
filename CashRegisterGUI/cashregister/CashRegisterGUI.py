# a file for gui logic

from customtkinter import *

# theme
set_default_color_theme("green")
set_appearance_mode("dark")

# grid
def configure_grid(window):
    window.grid_columnconfigure(0.25, weight = 1)

# sets windeow with centering it and setting dimensions
def set_window(window: CTk, window_width: int, window_height: int, scale: float):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width - window_width) // 2 * scale)
    y = int((screen_height - window_height) // 2.5 * scale)
# x and y are the coordinates where the window will spawn
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")