#!/usr/bin/env python3
"""
This code holds the solution for part 1 of quest 9 of the Everone Codes tournament 2024.
"""
import sys


def calculate_solution(sparkballs):
    result = 0

    stamps = [10, 5, 3, 1]

    for sparkball in [int(x) for x in sparkballs]:
        beetles = 0

        for stamp in stamps:
            while sparkball >= stamp:
                sparkball -= stamp
                beetles += 1

        result += beetles
    
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

test_list = """2
4
7
16"""
result = run_test(test_list, 10)

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
