#!/usr/bin/env python3
"""
This code holds the solution for part 3 of quest 7 of the Everone Codes tournament 2024.
"""
import itertools
import sys


# Keep a cache of actions and scores, so we don't have to keep calculating things
# over and over. Performance.
DP = {}


def map_track(grid):
    row, col, direction = 0, 0, 1

    # N E S W
    D = [(0,-1), (1,0), (0,1), (-1,0)]

    track_str = ''

    while True:
        # Check to see if we've finished one circuit of the map...
        if len(track_str) > 0 and grid[row][col] == 'S':
            break

        # Decide where to look next for the continuation of the track, will be
        # one of:
        #   1. in the same direction
        #   2. to our left (relative to the current direction)
        #   3. to our right (relative to the current direction)
        for new_direction in [direction, (direction+3) % 4, (direction+1) % 4]:
            rr = row + D[new_direction][1]
            cc = col + D[new_direction][0]

            # Check that we are still within bounds, and we've not found an empty cell.
            if 0 <= rr < len(grid) and 0 <= cc < len(grid[rr]) and grid[rr][cc] != ' ':
                track_str += grid[rr][cc]
                row, col = rr, cc
                direction = new_direction
                break

    return track_str


def score_lap(actions, track_str):
    key = tuple(actions)

    if key in DP:
        return DP[key]
    
    power = 0
    score = 0
    i = 0
    
    for cell in track_str:
        if cell == '=' or cell == 'S':
            cell = actions[i % len(actions)]

        if cell == '+':
            power += 1
        elif cell == '-':
            power -= 1
        else:
            assert cell == '=' or cell == 'S', cell
        
        score += power
        i += 1
    
    DP[key] = (score, power)
    
    return (score, power)


def score_knight(actions, track, laps):
    score = 0
    power = 10
    i = 0

    for round_ in range(laps):
        round_actions = actions[i:] + actions[:i]

        #print(f'{i=} {round_actions=} {actions=}')
        
        round_score, round_power = score_lap(round_actions, track)
        score += round_score + power * len(track)
        power += round_power
        i = (i + len(track)) % len(actions)

    return score


def calculate_solution(lines, track_plan):
    track = map_track(track_plan)

    actions_by_id = {}
    for line in lines:
        id_, actions = line.split(':')
        actions = actions.split(',')
        actions_by_id[id_] = actions

    ROUNDS = 2024
    enemy_score = score_knight(actions_by_id['A'], track, ROUNDS)

    result = 0
    opts = set(itertools.permutations('+++++---==='))
    # print(len(opts))
    
    for i, opt in enumerate(opts):
        opt_score = score_knight(opt, track, ROUNDS)

        # if i % 100 == 0:
        #     print(i, opt_score, enemy_score)

        if opt_score > enemy_score:
            result += 1

    return result


def run_test(test_input, test_track, expected_solution):
    """
    Helper method for running some unit tests whilst minimising repetative code.
    """
    result = calculate_solution(test_input.split('\n'), test_track)

    print()
    if result != expected_solution:
        print(f'Test for {test_input} FAILED. Got a result of {result}, not {expected_solution}')
        sys.exit(-1)

    print(f'Test for {test_input} passed.')

    return result

# Ok, so if we reach here, then we can be reasonably sure that the code
# above is working correctly. Let's use the actual captcha now.

with open('track_p3.txt', 'r') as f:
    track = [line.strip() for line in f]

with open('input_p3.txt', 'r') as f:
    input_data = [line.strip() for line in f]
    answer = calculate_solution(input_data, track)

    print(f'Solution is {answer}')
