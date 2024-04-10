import pytest
from gameoflife import create_grid, populate_grid

@pytest.mark.parametrize("rows, cols", [
    (5, 5),
    (10, 10),
    (1, 1)
])
def test_create_grid_positive_dimensions(rows: int, cols: int):
    """
    Test that create_grid creates a grid with the correct dimensions and initializes all cells to dead (0).

    Args:
        rows (int): Number of rows in the grid.
        cols (int): Number of columns in the grid.
    """
    grid = create_grid(rows, cols)
    assert len(grid) == rows, "Grid has the correct number of rows"
    assert all(len(row) == cols for row in grid), "All rows have the correct number of columns"
    assert all(cell == 0 for row in grid for cell in row), "All cells are initialized to dead (0)"

@pytest.mark.parametrize("rows, cols", [
    (-1, 5),
    (5, -1),
    (0, 0)
])
def test_create_grid_negative_dimensions(rows: int, cols: int):
    """
    Test that create_grid raises a ValueError for non-positive dimensions.

    Args:
        rows (int): Number of rows in the grid.
        cols (int): Number of columns in the grid.
    """
    with pytest.raises(ValueError):
        create_grid(rows, cols)

@pytest.mark.parametrize("rows, cols", [
    (5, 5),
    (10, 10),
    (3, 3)
])
def test_populate_grid_non_empty(rows: int, cols: int):
    """
    Test that populate_grid correctly populates a grid, ensuring at least one cell is alive.

    Args:
        rows (int): Number of rows in the grid to be created and populated.
        cols (int): Number of columns in the grid to be created and populated.
    """
    grid = create_grid(rows, cols)
    populate_grid(grid)
    assert len(grid) == rows, "Grid has the correct number of rows after population"
    assert all(len(row) == cols for row in grid), "All rows have the correct number of columns after population"
    assert any(cell == 1 for row in grid for cell in row), "At least one cell is alive after population"

def test_populate_grid_empty():
    """
    Test that populate_grid raises a ValueError when attempting to populate an empty grid.
    """
    with pytest.raises(ValueError):
        populate_grid([])