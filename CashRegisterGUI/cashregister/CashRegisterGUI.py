# a file for gui related functions

# centers window
def center_window(window, window_width, window_height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - int(window_width)) // 2
    y = (screen_height - int(window_height)) // 2
    window.geometry(f"+{x}+{y}")