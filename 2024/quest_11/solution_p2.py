#!/usr/bin/env python3
"""
This code holds the solution for part 2 of quest 11 of the Everone Codes tournament 2024.
"""
import sys


def calculate_solution(genetics):
    termites = {}

    for genes in genetics:
        genes = genes.split(':')
        termites[genes[0]] = genes[1].split(',')

    population = ['Z']

    for day in range(10):
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

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('input_p2.txt', 'r') as f:
    input_data = [line.strip() for line in f]
    answer = calculate_solution(input_data)

    print(f'Solution is {answer}')
