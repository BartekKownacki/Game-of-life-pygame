"""
Grid model file.
"""
class Grid:
    """
    Grid class
    """
    def __init__(self, dimensions, grid, cell_props):
        """
        Initialize the grid.
        """
        self._width = dimensions["width"]
        self._height = dimensions["height"]
        self.grid = grid
        self.cell_size = cell_props["cell_size"]
        self.gap_size = cell_props["gap_size"]
        self.cell_color = cell_props["cell_color"]
        # self.cell_live_color = cell_props["cell_live_color"]
        # self.cell_live_radius = cell_props["cell_live_radius"]

    @property
    def width(self):
        """
        Public width property
        """
        return self._width

    @property
    def height(self):
        """
        Public height property
        """
        return self._height
