"""
Menu model
"""
class Menu:
    """
    Menu model class
    """
    def __init__(self, buttons_list, menu_height, menu_width, statuses):
        """
        initialize menu model
        """
        self.buttons = buttons_list
        self.menu_height = menu_height
        self.menu_width = menu_width
        self.statuses= statuses
