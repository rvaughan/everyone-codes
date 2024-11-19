#!/usr/bin/env python3
"""
This code holds the solution for part 1 of quest 1 of the Everone Codes tournament 2024.
"""
import sys


def calculate_solution(battles):
    result = 0

    for battle in battles:
        n = 3
        for pairs in [battle[i:i+n] for i in range(0, len(battle), n)]:
            count = 0
            score = 0
            for item in pairs:
                if item == 'A':
                    score += 0
                    count += 1
                elif item == 'B':
                    score += 1
                    count += 1
                elif item == 'C':
                    score += 3
                    count += 1
                elif item == 'D':
                    score += 5
                    count += 1

            if count == 3:
                score += 6
            elif count == 2:
                score += 2

            # print(pairs, count, score, result)

            result += score

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
xBxAAABCDxCC
"""
result = run_test(test_list, 30)

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
