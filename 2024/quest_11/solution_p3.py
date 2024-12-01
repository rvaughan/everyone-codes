#!/usr/bin/env python3
"""
This code holds the solution for part 3 of quest 11 of the Everone Codes tournament 2024.
"""
from collections import Counter
import sys


def calculate_population(termites, starting_population):
    population = starting_population

    cur = Counter({starting_population[0]: 1})

    for day in range(20):
        new_population = Counter()

        for termite, termite_count in cur.items():
            for gene, count in termites[termite].items():
                new_population[gene] += termite_count * count

        cur = new_population

    return sum(cur.values())


def calculate_solution(genetics):
    termites = {}

    for genes in genetics:
        genes = genes.split(':')
        termites[genes[0]] = Counter(genes[1].split(','))

    populations = []
    for key in termites.keys():
        populations.append(calculate_population(termites, [key]))

    populations.sort()

    result = populations[-1] - populations[0]

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
B:C,A,A
C:A"""
result = run_test(test_list, 268815)

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
