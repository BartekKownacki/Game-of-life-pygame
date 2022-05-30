from models.Grid import Grid
from static import colors as c
from static import init_data as init
import sys,pygame

class GridView:
    def __init__(self, screen, cell_size, gap_size):
        self.screen = screen
        self.cell_size = cell_size
        self.gap_size = gap_size

    def draw_grid(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                x, y = self.convert_to_pixel_coordinates(i, j)
                pygame.draw.rect(self.screen, c.light_gray, (x, y, init.cell_size, init.cell_size))
                if grid[i][j] == 1:
                    pygame.draw.circle(self.screen, c.dark_green, (x + (self.cell_size/2), y + (init.cell_size/2)), init.radius)


    def convert_to_pixel_coordinates(self, index_x, index_y):
        x = self.gap_size + index_x * (self.cell_size + self.gap_size)
        y = self.gap_size + index_y * (self.cell_size + self.gap_size)
        return x, y 