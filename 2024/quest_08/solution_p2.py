#!/usr/bin/env python3
"""
This code holds the solution for part 2 of quest 8 of the Everone Codes tournament 2024.
"""
import sys


def calculate_solution(num_blocks):
    result = 0

    num_blocks = int(num_blocks[0])

    cur_width = 1
    num_blocks -= cur_width
    while num_blocks > 0:
        cur_width += 2

        if cur_width > num_blocks:
            missing = cur_width - num_blocks
            result = missing * cur_width
            break            
        else:
            num_blocks -= cur_width

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

test_list = """3"""
result = run_test(test_list, 27)

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
