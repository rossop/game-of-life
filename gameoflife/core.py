from typing import List
import random

def create_grid(rows: int, cols: int) -> List[List[int]]:
    """
    Creates a grid for the Game of Life.

    Args:
        rows (int): Number of rows in the grid.
        cols (int): Number of columns in the grid.

    Returns:
        List[List[int]]: A 2D list representing the grid, initialized with all
            cells dead (0).

    Raises:
        ValueError: If `rows` or `cols` are non-positive.
    """
    if rows <= 0 or cols <= 0:
        raise ValueError("rows and cols must be positive integers")
    return [[0 for _ in range(cols)] for _ in range(rows)]

def populate_grid(grid: List[List[int]]) -> None:
    """
    Populates Grid with alive cells at randomly generated positions.

    Args:
        grid (List[List[int]]): A 2D list representing the grid, initialized 
            with all cells dead (0).

    Raises:
        ValueError: If `grid` is empty or not a 2D list.
    """
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")
    rows = len(grid)
    cols = len(grid[0])
    for rr in range(rows):
        for cc in range(cols):
            grid[rr][cc] = random.randint(0, 1)


def main() -> None:    
    rows, cols = 10, 10  # Example grid size
    grid = create_grid(rows, cols)
    populate_grid(grid)
    # Example of printing the grid state to console
    for row in grid:
        print(' '.join(str(cell) for cell in row))


if __name__ == "__main__":
    main()