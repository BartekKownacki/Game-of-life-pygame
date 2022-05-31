"""
Grid controller
"""
from math import floor
import random as r
from models.grid import Grid
from views.grid_view import GridView

class GridController:
    """
    Grid controller methods
    """
    def __init__(self, screen, width, height, props):
        """
        Initialize grid controller
        """
        self.is_simulation_running = False
        self.width = width
        self.height = height
        self.grid = Grid({"width": width, "height": height},
                        self.create_random_grid(),
                        {"cell_size": props["cell_size"],
                            "gap_size": props["gap_size"],
                            "cell_color": props["cell_color"],
                            "cell_live_color": props["cell_live_color"],
                            "cell_live_radius": props["cell_live_radius"],
                        })
        self.view = GridView(screen, props["cell_size"], props["gap_size"])

    def create_grid(self):
        """
        create and return empty grid
        """
        grid = [[0 for i in range(self.height)] for j in range(self.width)]
        return grid

    def create_random_grid(self):
        """
        create and return grid with random living cells
        """
        grid = self.create_grid()
        random_x = r.randint(0, self.width-1)
        random_y = r.randint(0, self.height-1)
        random_fields_to_fill = floor(self.width * self.height * 2/3)
        for _ in range(random_fields_to_fill):
            random_x = r.randint(0, self.width-1)
            random_y = r.randint(0, self.height-1)
            grid[random_x][random_y] = 1
        return grid

    def clear_grid(self):
        """
        set grid empty
        """
        self.grid.grid = self.create_grid()

    def randomize_grid(self):
        """
        set grid to random state
        """
        grid = self.create_grid()
        random_x = r.randint(0, self.grid.width-1)
        random_y = r.randint(0, self.grid.height-1)
        random_fields_to_fill = floor(self.grid.width * self.grid.height * 2/3)
        for _ in range(random_fields_to_fill):
            random_x = r.randint(0, self.grid.width-1)
            random_y = r.randint(0, self.grid.height-1)
            grid[random_x][random_y] = 1
        self.grid.grid = grid

    def handle_click(self, x_dimension, y_dimension, is_mouse_coordinates):
        """
        handle grid click
        """
        if is_mouse_coordinates:
            x_dimension, y_dimension = self.convert_to_grid_coordinates(x_dimension, y_dimension)
        self.toggle_cell(x_dimension, y_dimension)

    def toggle_cell(self, x_dimension, y_dimension):
        """
        toggle cell state
        """
        try:
            if self.grid.grid[x_dimension][y_dimension] == 1:
                self.grid.grid[x_dimension][y_dimension] = 0
            else:
                self.grid.grid[x_dimension][y_dimension] = 1
        except IndexError:
            print("Out of bounds")

    def convert_to_grid_coordinates(self, x_dimension, y_dimension):
        """
        convert mouse coordinates to grid coordinates
        """
        divider = self.grid.cell_size + self.grid.gap_size
        x_dimension = floor(x_dimension/divider)
        y_dimension = floor(y_dimension/divider)
        return x_dimension, y_dimension

    def draw_grid(self):
        """
        draw grid on screen
        """
        self.view.draw_grid(self.grid)

    def one_step(self):
        """
        move one step forward
        """
        next_step_grid = self.create_grid()
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

    def count_live_neighbours(self, x_dimension, y_dimension):
        """
        count live neighbours
        """
        cells_to_test = [(x_dimension-1, y_dimension-1),
                        (x_dimension-1, y_dimension),
                        (x_dimension-1, y_dimension+1),
                        (x_dimension, y_dimension-1),
                        (x_dimension, y_dimension+1),
                        (x_dimension+1, y_dimension-1),
                        (x_dimension+1, y_dimension),
                        (x_dimension+1, y_dimension+1)]
        live_cell_count = 0
        for element in cells_to_test:
            if (element[0] < 0 or element[1] < 0
                or element[0] >= self.grid.width
                or element[1] >= self.grid.height):
                pass
            else:
                if self.grid.grid[element[0]][element[1]] == 1:
                    live_cell_count += 1
        return live_cell_count
