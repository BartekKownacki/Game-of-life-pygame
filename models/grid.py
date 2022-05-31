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
        self.width = dimensions["width"]
        self.height = dimensions["height"]
        self.grid = grid
        self.cell_size = cell_props["cell_size"]
        self.gap_size = cell_props["gap_size"]
        self.cell_color = cell_props["cell_color"]
        self.cell_live = {"color": cell_props["cell_live_color"],
                            "radius": cell_props["cell_live_radius"]}
