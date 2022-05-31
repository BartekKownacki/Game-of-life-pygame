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
        self._menu_height = menu_height
        self._menu_width = menu_width
        self.statuses= statuses

    @property
    def menu_height(self):
        """
        Public menu height property
        """
        return self._menu_height

    @property
    def menu_width(self):
        """
        Public menu width property
        """
        return self._menu_width
