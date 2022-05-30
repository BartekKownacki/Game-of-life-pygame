from models.Menu import Menu
from views.MenuView import MenuView
from math import floor
from static import init_data as init
import random as r

class MenuController:
    def __init__(self, screen, menu_width, menu_height, buttons_list, screen_width, menu_start_y, grid_controller, statuses):
        self.screen = screen
        self.menu_start_y = menu_start_y
        self.menu_height = menu_height
        self.menu = Menu(self.merge_buttons_with_dimensions(buttons_list), menu_width, menu_height, statuses)
        self.view = MenuView(self.screen, self.menu.buttons, screen_width, menu_start_y, menu_height, self.menu.statuses)
        self._grid_controller = grid_controller
 
    def draw_menu(self):
        self.view.draw_menu()


    def merge_buttons_with_dimensions(self, buttons):
        for button in buttons:
            button_width = init.button_dimensions_x
            button_height = init.button_dimensions_y
            button_x = init.btn_gap_size + (init.btn_gap_size + button_width) * button["index"]
            button_y = self.menu_start_y + (self.menu_height - button_height)/2
            button["dimensions_x"] = button_x
            button["dimensions_y"] = button_y
            button["dimensions_width"] = button_width
            button["dimensions_height"] = button_height
        return buttons

    def handle_button_action(self, action):
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
        for button in self.menu.buttons:
            if self.is_mouse_on_button(mouse_pos_x, mouse_pos_y, button):
                if(button["is_visible"]):
                    self.handle_button_action(button["action"])

    def is_mouse_on_button(self, mouse_pos_x, mouse_pos_y, button):
        if mouse_pos_x >= button["dimensions_x"] and mouse_pos_x <= button["dimensions_x"] + button["dimensions_width"]:
            if mouse_pos_y >= button["dimensions_y"] and mouse_pos_y <= button["dimensions_y"] + button["dimensions_height"]:
                return True
        return False
