#!/usr/bin/env python3
"""
This code holds the solution for part 2 of quest 9 of the Everone Codes tournament 2024.
"""
from functools import cache
import sys


@cache
def num_beetles(brightness):
    stamps = [30, 25, 24, 20, 16, 15, 10, 5, 3, 1]

    if brightness == 0:
        return 0
    
    if brightness < 0:
        return 10**100
    
    best = 10**100
    
    for stamp in stamps:
        sub = num_beetles(brightness - stamp)
        best = min(best, 1 + sub)
    
    return best


def calculate_solution(sparkballs):
    sparkballs = [int(x) for x in sparkballs]
    result = 0

    for sparkball in sparkballs:
        result += num_beetles(sparkball)

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

test_list = """156488
352486
546212"""
result = run_test(test_list, 10449)

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
