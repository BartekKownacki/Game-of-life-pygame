from models.Grid import Grid
from static import colors as c
from static import init_data as init
import sys,pygame

class MenuView:
    def __init__(self, screen, buttons, screen_width, menu_start_y, menu_height, statuses):
        self.screen = screen
        self.buttons = buttons
        self.menu_start_y = menu_start_y
        self.screen_width = screen_width
        self.menu_height = menu_height
        self.statuses = statuses

    def draw_menu(self):
        self.draw_divider()
        for button in self.buttons:
            self.draw_button(button)

        for status in self.statuses:
            self.draw_status(status)

    def draw_divider(self):
        divider_y = init.gap_size + self.menu_start_y
        pygame.draw.line(self.screen, c.white, (init.gap_size, divider_y), (self.screen_width-init.gap_size, divider_y), init.divider_size)

    def draw_button(self, button):
        if(button["is_visible"]):
            button_width = init.button_dimensions_x
            button_height = init.button_dimensions_y
            button_x = init.btn_gap_size + (init.btn_gap_size + button_width) * button["index"]
            button_y = self.menu_start_y + (self.menu_height - button_height)/2
            pygame.draw.rect(self.screen, c.white, (button_x, button_y, button_width, button_height))
            pygame.draw.rect(self.screen, c.black, (button_x, button_y, button_width, button_height), init.divider_size)
            button_image = pygame.image.load(button["image_path"])
            button_image = pygame.transform.scale(button_image, (button_width, button_height))
            self.screen.blit(button_image, (button_x, button_y))

    def draw_status(self, status):
        if(status["is_visible"]):
            status_width = init.status_dimensions_x
            status_height = init.status_dimensions_y
            status_x = self.screen_width - init.btn_gap_size - status_width
            status_y = self.menu_start_y + (self.menu_height - status_height)/2
            if(status["index"] == 0):
                status_y = self.menu_start_y + (self.menu_height - status_height*2)/2
            else:
                status_y = self.menu_start_y + self.menu_height - (self.menu_height - status_height*2)/2 - status_height
                 
            pygame.draw.rect(self.screen, c.white, (status_x, status_y, status_width, status_height))
            pygame.draw.rect(self.screen, c.black, (status_x, status_y, status_width, status_height), init.divider_size)
            status_image = pygame.image.load(status["image_path"])
            status_image = pygame.transform.scale(status_image, (status_width, status_height))
            self.screen.blit(status_image, (status_x, status_y))