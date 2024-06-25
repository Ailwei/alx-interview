#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all four possible neighbors
                if i == 0 or grid[i - 1][j] == 0:  # check above
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:  # check below
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # check left
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:  # check right
                    perimeter += 1

    return perimeter
