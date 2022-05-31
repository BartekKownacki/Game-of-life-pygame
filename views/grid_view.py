"""
View file for the grid.
"""
import pygame
from static import colors as c
from static import init_data as init


class GridView:
    """
    Grid view class
    """
    def __init__(self, screen, cell_size, gap_size):
        """
        Initialize the grid view.
        """
        self.screen = screen
        self.cell_size = cell_size
        self.gap_size = gap_size

    def draw_grid(self, grid):
        """
        Draw the grid.
        """
        for i, element in enumerate(grid):
            for j, item in enumerate(grid[i]):
                x_coordinate, y_coordinate = self.convert_to_pixel_coordinates(i, j)
                pygame.draw.rect(self.screen,
                                c.LIGHT_GRAY,
                                (x_coordinate, y_coordinate, self.cell_size, self.cell_size))
                if grid[i][j] == 1:
                    pygame.draw.circle(self.screen, c.DARK_GREEN,
                                        (x_coordinate + (self.cell_size/2),
                                            y_coordinate + (self.cell_size/2)), init.RADIUS)


    def convert_to_pixel_coordinates(self, index_x, index_y):
        """
        Convert grid coordinates to pixel coordinates.
        """
        x_coordinate = self.gap_size + index_x * (self.cell_size + self.gap_size)
        y_coordinate = self.gap_size + index_y * (self.cell_size + self.gap_size)
        return x_coordinate, y_coordinate
