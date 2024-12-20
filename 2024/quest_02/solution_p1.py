#!/usr/bin/env python3
"""
This code holds the solution for part 1 of quest 2 of the Everone Codes tournament 2024.
"""
import sys


def calculate_solution(lines):
    result = 0

    words = None
    for line in lines:
        if line.strip() != '':
            if words is None:
                words = line.split(':')[1].split(',')
            else:
                for word in words:
                    result += line.count(word)

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
WORDS:THE,OWE,MES,ROD,HER

AWAKEN THE POWER ADORNED WITH THE FLAMES BRIGHT IRE
"""
result = run_test(test_list, 4)

test_list = """
WORDS:THE,OWE,MES,ROD,HER

THE FLAME SHIELDED THE HEART OF THE KINGS
"""
result = run_test(test_list, 3)

test_list = """
WORDS:THE,OWE,MES,ROD,HER

POWE PO WER P OWE R
"""
result = run_test(test_list, 2)

test_list = """
WORDS:THE,OWE,MES,ROD,HER

THERE IS THE END
"""
result = run_test(test_list, 3)

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
