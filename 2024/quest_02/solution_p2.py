#!/usr/bin/env python3
"""
This code holds the solution for part 2 of quest 2 of the Everone Codes tournament 2024.
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
                positions = set()

                for word in words:
                    offset = 0
                    while offset < len(line):
                        pos = line.find(word, offset)
                        if pos == -1:
                            break

                        for x in range(pos, pos+len(word)):
                            positions.add(x)

                        offset = pos + 1

                    # Now check the same word in reverse...
                    offset = 0
                    word = word[::-1]
                    while offset < len(line):
                        pos = line.find(word, offset)
                        if pos == -1:
                            break
                        
                        for x in range(pos, pos+len(word)):
                            positions.add(x)

                        offset = pos + 1

                result += len(positions)

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
WORDS:THE,OWE,MES,ROD,HER,QAQ

AWAKEN THE POWE ADORNED WITH THE FLAMES BRIGHT IRE
THE FLAME SHIELDED THE HEART OF THE KINGS
POWE PO WER P OWE R
THERE IS THE END
QAQAQ
"""
result = run_test(test_list, 42)

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
