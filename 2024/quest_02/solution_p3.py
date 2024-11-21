#!/usr/bin/env python3
"""
This code holds the solution for part 2 of quest 2 of the Everone Codes tournament 2024.
"""
import sys


def find_words(words, lines):
    result = 0

    for line in lines:
        positions = set()

        for word in words:
            offset = 0
            while offset < len(line):
                # We'll double the length of the line to allow us to find line wraps.
                pos = (line*2).find(word, offset)
                if pos == -1:
                    break

                for x in range(pos, pos+len(word)):
                    # Because the doubled the line size, we need to use modulus here.
                    positions.add(x % len(line))

                offset = pos + 1

        result += len(positions)

    return result


def calculate_solution(lines):
    result = 0

    words = None
    lines_to_process = []
    for line in lines:
        if line.strip() != '':
            if words is None:
                words = line.split(':')[1].split(',')
                words.extend([w[::-1] for w in words])
            else:
                lines_to_process.append(line)

    result += find_words(words, lines_to_process)

    vertical_lines = list(map("".join,zip(*lines_to_process)))

    result += find_words(words, vertical_lines)

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
WORDS:THE,OWE,MES,ROD,RODEO

HELWORLT
ENIGWDXL
TRODEOAL
"""
# result = run_test(test_list, 10)

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