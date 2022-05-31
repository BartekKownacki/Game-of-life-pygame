"""
View file for the menu.
"""
import pygame
from static import colors as c
from static import init_data as init


class MenuView:
    """
    Menu view class
    """
    def __init__(self, screen, buttons, dimensions, statuses):
        """
        Initialize the menu view.
        """
        self.screen = screen
        self.buttons = buttons
        self.menu_start_y = dimensions["menu_start_y"]
        self.screen_width = dimensions["screen_width"]
        self.menu_height = dimensions["menu_height"]
        self.statuses = statuses

    def draw_menu(self):
        """
        Draw the menu.
        """
        self.draw_divider()
        for button in self.buttons:
            self.draw_button(button)

        for status in self.statuses:
            self.draw_status(status)

    def draw_divider(self):
        """
        Draw divider
        """
        divider_y = init.GAP_SIZE + self.menu_start_y
        pygame.draw.line(self.screen,
                        c.WHITE,
                        (init.GAP_SIZE, divider_y),
                        (self.screen_width-init.GAP_SIZE, divider_y),
                        init.DIVIDER_SIZE)

    def draw_button(self, button):
        """
        Draw button
        """
        if button["is_visible"]:
            button_width = init.BUTTON_DIMENSIONS_X
            button_height = init.BUTTON_DIMENSIONS_Y
            button_x = init.BTN_GAP_SIZE + (init.BTN_GAP_SIZE + button_width) * button["index"]
            button_y = self.menu_start_y + (self.menu_height - button_height)/2
            pygame.draw.rect(self.screen,
                            c.WHITE,
                            (button_x, button_y, button_width, button_height))
            pygame.draw.rect(self.screen,
                            c.BLACK,
                            (button_x, button_y, button_width, button_height),
                            init.DIVIDER_SIZE)
            button_image = pygame.image.load(button["image_path"])
            button_image = pygame.transform.scale(button_image, (button_width, button_height))
            self.screen.blit(button_image, (button_x, button_y))

    def draw_status(self, status):
        """
        Draw status
        """
        if status["is_visible"]:
            status_width = init.STATUS_DIMENSIONS_X
            status_height = init.STATUS_DIMENSIONS_Y
            status_x = self.screen_width - init.BTN_GAP_SIZE - status_width
            status_y = self.menu_start_y + (self.menu_height - status_height)/2
            if status["index"] == 0:
                status_y = self.menu_start_y + (self.menu_height - status_height*2)/2
            else:
                status_y = (self.menu_start_y
                            + self.menu_height
                            - (self.menu_height - status_height*2)/2
                            - status_height)
            pygame.draw.rect(self.screen,
                            c.WHITE,
                            (status_x, status_y, status_width, status_height))
            pygame.draw.rect(self.screen,
                            c.BLACK,
                            (status_x, status_y, status_width, status_height), init.DIVIDER_SIZE)
            status_image = pygame.image.load(status["image_path"])
            status_image = pygame.transform.scale(status_image, (status_width, status_height))
            self.screen.blit(status_image, (status_x, status_y))
