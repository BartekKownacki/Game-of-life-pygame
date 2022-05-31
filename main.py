"""
Pygame version of Conway's Game of Life.
author: Bartosz Kownacki
"""
import pygame
import static.colors as c

from static import init_data as init
from controllers.grid_controller import GridController
from controllers.menu_controller import MenuController

dimensions = width, height = init.WIDTH, init.HEIGHT

pygame.init()


PIXEL_WIDTH = (init.CELL_SIZE + init.GAP_SIZE)*width + init.GAP_SIZE
PIXEL_GRID_HEIGHT = (init.CELL_SIZE + init.GAP_SIZE)*height
size = PIXEL_WIDTH, PIXEL_GRID_HEIGHT + init.MENU_HEIGHT

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

pygame.display.set_caption("Game of Life - Bartosz Kownacki ")

grid_controller = GridController(screen,
                                width,
                                height,
                                {
                                    "cell_size": init.CELL_SIZE,
                                    "gap_size": init.GAP_SIZE,
                                    "cell_color": c.LIGHT_GRAY,
                                })
menu_controller = MenuController(screen,
                                PIXEL_GRID_HEIGHT,
                                grid_controller,
                                {"statuses": init.STATUSES,
                                "buttons": init.BUTTONS,
                                "menu_height": init.MENU_HEIGHT,
                                "menu_width": PIXEL_WIDTH,})

RUN = True
while RUN:
    screen.fill(c.BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if event.pos[1] > PIXEL_GRID_HEIGHT:
                    menu_controller.handle_click(event.pos[0], event.pos[1])
                else:
                    grid_controller.handle_click(event.pos[0], event.pos[1], True)

    grid_controller.draw_grid()
    menu_controller.draw_menu()
    if grid_controller.is_simulation_running:
        grid_controller.one_step()
    pygame.display.flip()
    clock.tick(15)
