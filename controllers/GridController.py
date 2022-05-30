from models.Grid import Grid
from views.GridView import GridView
from math import floor

import random as r
class GridController:
    def __init__(self, screen, width, height, cell_size, gap_size, cell_color):
        self.screen = screen
        self.is_simulation_running = False
        self.width = width
        self.height = height
       
        self.grid = Grid(width, height, self.create_random_grid(), cell_size, gap_size, cell_color)
        self.view = GridView(screen, cell_size, gap_size)

    def create_grid(self, width, height):
        grid = [[0 for i in range(height)] for j in range(width)]
        return grid

    def create_random_grid(self):
        grid = self.create_grid(self.width, self.height)
        
        random_x = r.randint(0, self.width-1)
        random_y = r.randint(0, self.height-1)
        
        for i in range(1000):
            random_x = r.randint(0, self.width-1)
            random_y = r.randint(0, self.height-1)
            grid[random_x][random_y] = 1
        return grid

    def randomize_grid(self):
        grid = self.create_grid(self.width, self.height)
        
        random_x = r.randint(0, self.width-1)
        random_y = r.randint(0, self.height-1)
        
        for i in range(1000):
            random_x = r.randint(0, self.width-1)
            random_y = r.randint(0, self.height-1)
            grid[random_x][random_y] = 1
            
        self.grid.grid = grid

    def handle_click(self, x, y, is_mouse_coordinates):
        if is_mouse_coordinates:
            x, y = self.convert_to_grid_coordinates(x, y)
        self.toggle_cell(x, y)

    def toggle_cell(self, x, y):
        try:
            self.grid.grid[x][y] = 0 if self.grid.grid[x][y] == 1 else 1
        except:
            print("Out of bounds")
            pass
        
    def convert_to_grid_coordinates(self, x, y):
        divider = self.grid.cell_size + self.grid.gap_size
        x = floor(x/divider)
        y = floor(y/divider)
        return x, y 

    def draw_grid(self):
        self.view.draw_grid(self.grid.grid)

    def one_step(self):
        next_step_grid = self.create_grid(self.grid.width, self.grid.height)
        for i in range(self.grid.width):
            for j in range(self.grid.height):
                live_cell_count = self.count_live_neighbours(i, j)
                if self.grid.grid[i][j] == 1:
                    if live_cell_count < 2 or live_cell_count > 3:
                        next_step_grid[i][j] = 0
                    else:
                        next_step_grid[i][j] = 1
                else:
                    if live_cell_count == 3:
                        next_step_grid[i][j] = 1
                    else:
                        next_step_grid[i][j] = 0
        self.grid.grid = next_step_grid

    
    def count_live_neighbours(self, x, y):
        cells_to_test = [(x-1, y-1), 
                        (x-1, y), 
                        (x-1, y+1), 
                        (x, y-1), 
                        (x, y+1), 
                        (x+1, y-1), 
                        (x+1, y), 
                        (x+1, y+1)]
        live_cell_count = 0
        for element in cells_to_test:
            if element[0] < 0 or element[1] < 0 or element[0] >= self.grid.width or element[1] >= self.grid.height:
                continue
            else:
                if self.grid.grid[element[0]][element[1]] == 1:
                    live_cell_count += 1
        return live_cell_count

    
