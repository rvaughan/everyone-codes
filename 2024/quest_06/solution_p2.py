#!/usr/bin/env python3
"""
This code holds the solution for part 2 of quest 6 of the Everone Codes tournament 2024.
"""
from collections import defaultdict, deque
import sys


def to_dict(lines):
    return {
        line[0]: line[1].split(",")
        for line in [line.strip().split(":") for line in lines]
    }


def calculate_solution(lines):
    data = to_dict(lines)

    q, paths = deque([["RR"]]), defaultdict(list)
    while q:
        path = q.popleft()
        key = path[-1]
        if key == "@":
            paths[len(path)].append(path)

        children = data[key]
        for c in children:
            q.append(path + [c])
    
    return "".join(next(filter(lambda p: len(p) == 1, paths.values())).pop())


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

test_list = """RR:A,B,C
A:D,E
B:F,@
C:G,H
D:@
E:@
F:@
G:@
H:@"""
result = run_test(test_list, 'RRB@')

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
