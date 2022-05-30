import sys, pygame
from time import sleep
import static.colors as c

from static import init_data
from controllers.GridController import GridController
from controllers.MenuController import MenuController

dimensions = width, height = init_data.width, init_data.height
pygame.init()


pixel_width = (init_data.cell_size + init_data.gap_size)*width + init_data.gap_size
pixel_grid_height = (init_data.cell_size + init_data.gap_size)*height  
size = pixel_width, pixel_grid_height + init_data.menu_height

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

pygame.display.set_caption("Game of Life - Bartosz Kownacki ")

grid_controller = GridController(screen, width, height, init_data.cell_size, init_data.gap_size, c.light_gray)
menu_controller = MenuController(screen, pixel_width, init_data.menu_height, init_data.buttons, pixel_width, pixel_grid_height, grid_controller, init_data.statuses)

run = True
while run:
    screen.fill(c.black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[1] > pixel_grid_height:
                menu_controller.handle_click(event.pos[0], event.pos[1])
            else: 
                grid_controller.handle_click(event.pos[0], event.pos[1], True)

    grid_controller.draw_grid()
    menu_controller.draw_menu()
    if(grid_controller.is_simulation_running):
        grid_controller.one_step()
        # sleep(0.1)
    
    pygame.display.flip()
    clock.tick(15)