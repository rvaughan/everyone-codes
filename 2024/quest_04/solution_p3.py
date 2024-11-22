#!/usr/bin/env python3
"""
This code holds the solution for part 2 of quest 4 of the Everone Codes tournament 2024.
"""
import sys


def calculate_solution(nails_list):
    nails = [int(n) for n in nails_list]
    
    # This time, sort the list, and then work our way through the list, when the
    # number of strikes goes up then we know the previous attempt was the correct 
    # answer.

    nails.sort()

    starting_point = 0
    best_strikes = 999999999

    while True:
        min_height = nails[starting_point]

        num_strikes = 0
        for nail in nails:
            num_strikes += abs(min_height - nail)

        print(starting_point, min_height, num_strikes)

        if num_strikes > best_strikes:
            break

        best_strikes = num_strikes
        starting_point += 1

    return best_strikes


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
5
6
8"""
result = run_test(test_list, 8)

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
