"""
View file for the grid.
"""
import pygame

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
        for i, _ in enumerate(grid.grid):
            for j, _ in enumerate(grid.grid[i]):
                x_coordinate, y_coordinate = self.convert_to_pixel_coordinates(i, j)
                pygame.draw.rect(self.screen,
                                grid.cell_color,
                                (x_coordinate, y_coordinate, self.cell_size, self.cell_size))
                if grid.grid[i][j] == 1:
                    pygame.draw.circle(self.screen, grid.cell_live["color"],
                                        (x_coordinate + (self.cell_size/2),
                                            y_coordinate + (self.cell_size/2)),
                                        grid.cell_live["radius"])


    def convert_to_pixel_coordinates(self, index_x, index_y):
        """
        Convert grid coordinates to pixel coordinates.
        """
        x_coordinate = self.gap_size + index_x * (self.cell_size + self.gap_size)
        y_coordinate = self.gap_size + index_y * (self.cell_size + self.gap_size)
        return x_coordinate, y_coordinate
