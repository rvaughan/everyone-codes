#!/usr/bin/env python3
"""
This code holds the solution for part 3 of quest 5 of the Everone Codes tournament 2024.
"""
from collections import defaultdict
import functools
import sys


def calculate_solution(input):
    result = 0
    shouted = defaultdict(int)

    num_rows = len(input[0].split(' '))

    lines = [[]] * num_rows
    for line in input:
        data = line.split(' ')
        for row, x in enumerate(data):
            lines[row] = lines[row] + [int(x)]

    highest = 0
    cur_row = 0
    clap_round = 1
    while True:
        clapper = lines[cur_row].pop(0)
        
        next_row = cur_row + 1 if cur_row < num_rows - 1 else 0

        position = (clapper - 1) % (2*len(lines[next_row]))
        if position >= len(lines[next_row]):
            # We would be coming "back up" the row, on the right hand side...
            position = 2*len(lines[next_row]) - position
        lines[next_row].insert(position,clapper)

        # print(clap_round, "".join([str(x[0]) for x in lines]))

        result = int("".join([str(x[0]) for x in lines]))

        shouted[result] += 1

        # print(clap_round, "".join([str(x[0]) for x in lines]), max(shouted))

        if result > highest:
            highest = result
            print(result)

        # Assume that we've found it by this point...
        if clap_round == 10000:
            break

        clap_round += 1
        cur_row = next_row

    return highest


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

test_list = """2 3 4 5
6 7 8 9"""
result = run_test(test_list, 6584)

print('')
print('-----------------')
print('All Tests PASSED.')
print('-----------------')
print('')

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input_p3.txt', 'r') as f:
    input_data = [line.strip() for line in f]
    answer = calculate_solution(input_data)

    print(f'Solution is {answer}')
