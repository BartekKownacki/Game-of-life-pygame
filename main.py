from ast import PyCF_ALLOW_TOP_LEVEL_AWAIT
from math import floor
import sys, pygame
import colors as c


pygame.init()


cell_size = 16
radius = 6
gap_size = 4
grid_size_x = 32
grid_size_y = 24 
menu_height = 100
button_dimensions = 80, 42
grid_dimensions = (cell_size + gap_size)*grid_size_x, (cell_size + gap_size)*grid_size_y
size = width, height = (grid_dimensions[0], grid_dimensions[1] + menu_height) 
listOfCircles = []

def create_grid(x, y):
    grid = [[0 for i in range(y)] for j in range(x)]
    return grid

def draw_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(screen, c.light_gray, (i * (cell_size + gap_size), j * (cell_size + gap_size), cell_size, cell_size))
            if grid[i][j] == 1:
                pygame.draw.circle(screen, c.black, (i * (cell_size + gap_size) + (cell_size/2), j * (cell_size + gap_size) + (cell_size/2)), radius)

screen = pygame.display.set_mode(size)
grid = create_grid(grid_size_x, grid_size_y)
run = True
while run:
    screen.fill(c.black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x = floor(x/(cell_size+gap_size))
            y = floor(y/(cell_size+gap_size))
            value = grid[x][y]
            grid[x][y] = 1 if value == 0 else 0
            

    
    draw_grid(grid)
    for circle in listOfCircles:
        pygame.draw.circle(screen, c.red, circle, radius)
    pygame.display.update()