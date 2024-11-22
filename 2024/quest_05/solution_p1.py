#!/usr/bin/env python3
"""
This code holds the solution for part 1 of quest 5 of the Everone Codes tournament 2024.
"""
import sys


def calculate_solution(input):
    result = 0

    num_rows = len(input[0].split(' '))

    lines = [[]] * num_rows
    for line in input:
        data = line.split(' ')
        for row, x in enumerate(data):
            lines[row] = lines[row] + [int(x)]

    cur_row = 0
    clap_round = 1
    while clap_round < 11:
        clapper = lines[cur_row].pop(0)
        
        next_row = cur_row + 1 if cur_row < num_rows - 1 else 0

        pos = 0
        cc = clapper - 1
        direction = 1
        while cc > 0:
            cc -= 1
            pos += direction
            if direction == 1 and pos == len(lines[next_row]):
                direction = -1

        new_row = lines[next_row][:pos] + [clapper] + lines[next_row][pos:]

        lines[next_row] = new_row

        # print(clap_round, "".join([str(x[0]) for x in lines]))

        clap_round += 1
        cur_row = next_row

    result = int("".join([str(x[0]) for x in lines]))

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

test_list = """2 3 4 5
3 4 5 2
4 5 2 3
5 2 3 4"""
result = run_test(test_list, 2323)

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
