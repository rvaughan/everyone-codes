#!/usr/bin/env python3
"""
This code holds the solution for part 1 of quest 1 of the Everone Codes tournament 2024.
"""
import sys


def calculate_solution(genetics):
    termites = {}

    for genes in genetics:
        genes = genes.split(':')
        termites[genes[0]] = genes[1].split(',')

    population = ['A']

    for day in range(4):
        new_population = []

        for termite in population:
            for gene in termites[termite]:
                new_population.append(gene)

        population = new_population

    result = len(population)

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

test_list = """A:B,C
B:C,A
C:A"""
result = run_test(test_list, 8)

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
