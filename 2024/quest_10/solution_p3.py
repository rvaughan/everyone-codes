#!/usr/bin/env python3
"""
This code holds the solution for part 3 of quest 10 of the Everone Codes tournament 2024.
"""
import sys


def calc_rune_board(grid):
    col, row = 2, 2
    for row in range(2, 6):
        for col in range(2, 6):
            row_data = grid[row]
            col_data = [grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col], grid[5][col], grid[6][col], grid[7][col]]

            rune = '*'
            for r in row_data:
                for c in col_data:
                    if r != '.' and r == c:
                        rune = r

            grid[row][col] = rune

    runic_word = ''
    for row in range(2, 6):
        for col in range(2, 6):
            runic_word += grid[row][col]

    result = 0
    for pos, rune in enumerate(runic_word):
        result += ((pos + 1) * (ord(rune) - 64))

    return result


def calculate_solution(items):
    all_grid = []
    for item in items:
        all_grid.append(list(item))

    boards = []
    row = 0
    while row < len(all_grid) - 2:
        col = 0
        while col < len(all_grid[row]) - 2:
            grid = []
            for r in range(row, row + 8):
                grid.append(all_grid[r][col:col + 8])

            boards.append(grid)
            
            col += 6

        row += 6

    result = 0
    for grid in boards:
        result += calc_rune_board(grid)

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

test_list = """**XFZB**DCST**
**LWQK**GQJH**
?G....WL....DQ
BS....H?....CN
P?....KJ....TV
NM....Z?....SG
**NSHM**VKWZ**
**PJGV**XFNL**
WQ....?L....YS
FX....DJ....HV
?Y....WM....?J
TJ....YK....LP
**XRTK**BMSP**
**DWZN**GCJV**"""
result = run_test(test_list, 3889)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input_p2.txt', 'r') as f:
    input_data = [line.strip() for line in f]
    answer = calculate_solution(input_data)

    print(f'Solution is {answer}')
