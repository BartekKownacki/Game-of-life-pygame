"""
Mouse position helpers module.
"""

def is_mouse_on_button(mouse_pos_x, mouse_pos_y, button):
    """
    Is mouse on button function.
    """
    if (button["dimensions_x"]
        <= mouse_pos_x
        <= button["dimensions_x"] + button["dimensions_width"]):
        if (button["dimensions_y"]
            <= mouse_pos_y
            <= button["dimensions_y"] + button["dimensions_height"]):
            return True
    return False
