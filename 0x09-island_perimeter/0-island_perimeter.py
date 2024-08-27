#!/usr/bin/python3
""" Returns perimeter of island described in grid """


def island_perimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                if i == rows-1 or grid[i][j-1] == 0:
                    perimeter += 1

    return perimeter
