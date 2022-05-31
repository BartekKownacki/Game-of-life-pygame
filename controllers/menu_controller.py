"""
Menu controller
"""
from models.menu import Menu
from views.menu_view import MenuView
from static import init_data as init
from helpers.mouse_pos_helpers import is_mouse_on_button
class MenuController:
    """
    Menu controller class
    """
    def __init__(self, screen, menu_start_y, grid_controller, props):
        """
        Initialize the menu controller.
        """
        self.screen = screen
        self.menu_start_y = menu_start_y
        self.menu_height = props["menu_height"]
        self.menu = Menu(self.merge_buttons_with_dimensions(props["buttons"]),
                        self.menu_height,
                        props["menu_width"],
                        props["statuses"])
        self.view = MenuView(self.screen, self.menu.buttons,
                            {"screen_width": self.menu.menu_width,
                            "menu_height": self.menu.menu_height,
                            "menu_start_y": self.menu_start_y},
                            self.menu.statuses)
        self._grid_controller = grid_controller

    def draw_menu(self):
        """
        Draw the menu function.
        """
        self.view.draw_menu()

    def merge_buttons_with_dimensions(self, buttons):
        """
        Merge buttons with dimensions.
        """
        for button in buttons:
            button_width = init.BUTTON_DIMENSIONS_X
            button_height = init.BUTTON_DIMENSIONS_Y
            button_x = init.BTN_GAP_SIZE + (init.BTN_GAP_SIZE + button_width) * button["index"]
            button_y = self.menu_start_y + (self.menu_height - button_height)/2
            button["dimensions_x"] = button_x
            button["dimensions_y"] = button_y
            button["dimensions_width"] = button_width
            button["dimensions_height"] = button_height
        return buttons

    def handle_button_action(self, action):
        """
        Button action handler.
        """
        if action == "play":
            self._grid_controller.is_simulation_running = True
            self.menu.buttons[2]["is_visible"] = False
            self.menu.buttons[3]["is_visible"] = False
            self.menu.buttons[4]["is_visible"] = False
            self.menu.statuses[1]["is_visible"] = True
            self.menu.statuses[2]["is_visible"] = False
        elif action == "stop":
            self._grid_controller.is_simulation_running = False
            self.menu.buttons[2]["is_visible"] = True
            self.menu.buttons[3]["is_visible"] = True
            self.menu.buttons[4]["is_visible"] = True
            self.menu.statuses[1]["is_visible"] = False
            self.menu.statuses[2]["is_visible"] = True
        elif action == "randomize":
            self._grid_controller.is_simulation_running = False
            self._grid_controller.randomize_grid()
        elif action == "step":
            self._grid_controller.one_step()
        elif action == "clear":
            self._grid_controller.is_simulation_running = False
            self._grid_controller.clear_grid()

    def handle_click(self, mouse_pos_x, mouse_pos_y):
        """
        Handle click function.
        """
        for button in self.menu.buttons:
            if is_mouse_on_button(mouse_pos_x, mouse_pos_y, button):
                if button["is_visible"]:
                    self.handle_button_action(button["action"])
