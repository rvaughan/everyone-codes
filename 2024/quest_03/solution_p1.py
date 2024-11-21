#!/usr/bin/env python3
"""
This code holds the solution for part 1 of quest 3 of the Everone Codes tournament 2024.
"""
import sys


def calculate_solution(lines):
    result = 0

    grid = []
    for line in lines:
        if line.strip() == '':
            continue

        grid.append(list([0 if item == '.' else 1 for item in line]))

    changes = True
    while changes:
        changes = False
        
        # Create a copy of the grid variable
        new_grid = []
        for row in grid:
            new_grid.append(row.copy())
        
        
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == 0:
                    continue

                if y > 0 and grid[y - 1][x] == 0:
                    continue

                if grid[y - 1][x] <= (grid[y][x] - 1) or grid[y - 1][x] >= (grid[y][x] + 1):
                    continue

                if y < len(grid) and grid[y + 1][x] == 0:
                    continue

                if grid[y + 1][x] <= (grid[y][x] - 1) or grid[y + 1][x] >= (grid[y][x] + 1):
                    continue

                if x > 0 and grid[y][x - 1] == 0:
                    continue

                if grid[y][x - 1] <= (grid[y][x] - 1) or grid[y][x + 1] >= (grid[y][x] + 1):
                    continue

                if y < len(grid) and grid[y][x + 1] == 0:
                    continue

                if grid[y][x + 1] <= (grid[y][x] - 1) or grid[y][x + 1] >= (grid[y][x] + 1):
                    continue

                new_grid[y][x] += 1

                changes = True

        grid = new_grid

    result = sum([sum(row) for row in grid])

    return result


def run_test(test_input, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split('\n'))

    print()
    if result != expected_solution:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result


# Run any tests that we've defined to help validate our code prior to
# trying to solve the puzzle.

test_list = """
..........
..###.##..
...####...
..######..
..######..
...####...
..........
"""
result = run_test(test_list, 35)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input_p1.txt', 'r') as f:
    input_data = [line.strip() for line in f]
    answer = calculate_solution(input_data)

    print(f'Solution is {answer}')
