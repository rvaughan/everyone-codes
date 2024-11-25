#!/usr/bin/env python3
"""
This code holds the solution for part 1 of quest 10 of the Everone Codes tournament 2024.
"""
import sys


def calculate_solution(items):
    grid = []
    for item in items:
        grid.append(list(item))

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

    result = ''
    for row in range(2, 6):
        for col in range(2, 6):
            result += grid[row][col]

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

test_list = """**PCBS**
**RLNW**
BV....PT
CR....HZ
FL....JW
SG....MN
**FTZV**
**GMJH**"""
result = run_test(test_list, "PTBVRCZHFLJWGMNS")

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
