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


def count_live_neighbors(grid: List[List[int]], row: int, col: int) -> int:
    """
    Calculate the number of live neighbours around a given cell.

    Args:
        grid (List[List[int]]): The grid representing the current state.
        row (int): The row index of the cell.
        col (int): The column index of the cell.

    Returns:
        int: The number of live neighbours.
    """
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")

    rows, cols = len(grid), len(grid[0])
    live_neighbors = 0 
    for rr in range((max(0, row-1)), min(rows, row+2)):
        for cc in range((max(0, col-1)), min(cols, col+2)):
            if (rr, cc) != (row, col) and grid[rr][cc] == 1:
                live_neighbors += 1
    return live_neighbors


def next_cell_state(cell: int, live_neighbors: int) -> int:
    """
    Determine the next state of a cell based on Conway's Game of Life rules.

    Args:
        cell (int): The current state of the cell (1 for alive, 0 for dead).
        live_neighbors (int): The count of live neighbours.

    Returns:
        int: The next state of the cell (1 for alive, 0 for dead).
    """
    # Apply the Game of Life rules
    if cell == 1 and live_neighbors < 2:
        return 0    # Die of underpopulation
    if cell == 1 and live_neighbors in [2, 3]:
        return 1    # Survive
    if cell == 1 and live_neighbors > 3:
        return 0    # Die of overpopulation
    if cell == 0 and live_neighbors == 3:
        return 1    # Become alive through reproduction

    return cell     # Remain in the current state


def update_grid(grid: List[List[int]]) -> List[List[int]]:
    """
    Update all cells in the grid to their next state according to the Game of Life rules.

    Args:
        grid (List[List[int]]): The grid representing the current generation.

    Returns:
        List[List[int]]: A new grid representing the next generation.
    """
    rows, cols = len(grid), len(grid[0])
    next_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            live_neighbors = count_live_neighbors(grid, row, col)
            next_grid[row][col] = next_cell_state(grid[row][col], 
                                                  live_neighbors)
    return next_grid


def main() -> None:
    rows, cols = 10, 10  # Example grid size
    grid = create_grid(rows, cols)
    populate_grid(grid)
    # Example of printing the grid state to console
    for row in grid:
        print(' '.join(str(cell) for cell in row))


if __name__ == "__main__":
    main()
