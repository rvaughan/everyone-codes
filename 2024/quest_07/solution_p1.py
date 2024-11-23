#!/usr/bin/env python3
"""
This code holds the solution for part 1 of quest 7 of the Everone Codes tournament 2024.
"""
import sys


def calculate_solution(items):
    plans = {}

    for plan in items:
        name, steps = plan.split(':')
        steps = steps.split(',')

        plans[name] = 10

        scores = []

        segment = 0
        while segment < 10:
            if steps[segment % len(steps)] == '+':
                plans[name] += 1
            elif steps[segment % len(steps)] == '-':
                plans[name] -= 1 if plans[name] > 0 else 0
            elif steps[segment % len(steps)] == '=':
                plans[name] += 0

            scores.append(plans[name])

            # print(name, segment, segment % len(steps), steps[segment % len(steps)], plans[name])

            segment += 1

        plans[name] = sum(scores)

    sorted_plans = dict(sorted(plans.items(), key=lambda item: item[1]))

    # print(sorted_plans)

    result = ''
    for key, _ in sorted_plans.items():
        result += key

    result = result[::-1]

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

test_list = """A:+,-,=,=
B:+,=,-,+
C:=,-,+,+
D:=,=,=,+"""
result = run_test(test_list, "BDCA")

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
