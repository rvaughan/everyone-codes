#!/usr/bin/env python3
"""
This code holds the solution for part 3 of quest 7 of the Everone Codes tournament 2024.
"""
import sys


def calculate_solution(items, track_plan):
    plans = {}

    track_pieces = track_plan.split('\n')

    track = track_pieces[0]

    left_side = ''
    right_side = ''

    for piece in track_pieces[1:-1]:
        left_side += piece[0]
        right_side += piece[-1]

    track += right_side + track_pieces[-1][::-1] + left_side[::-1]

    track = track[1:] + 'S'

    for plan in items:
        name, steps = plan.split(':')
        steps = steps.split(',')

        plans[name] = 10

        scores = []

        loop = 0
        knight_segment = 0
        while loop < 10:
            for track_segment in range(0, len(track)):                        
                if track[track_segment] == '+':
                    plans[name] += 1
                elif track[track_segment] == '-':
                    plans[name] -= 1 if plans[name] > 0 else 0
                elif track[track_segment] == '=' or track[track_segment] == 'S':
                    # Just do whatever the knight wants to
                    if steps[knight_segment % len(steps)] == '+':
                        plans[name] += 1
                    elif steps[knight_segment % len(steps)] == '-':
                        plans[name] -= 1 if plans[name] > 0 else 0
                    elif steps[knight_segment % len(steps)] == '=':
                        plans[name] += 0

                # print(track[track_segment], knight_segment, knight_segment % len(steps), steps[knight_segment % len(steps)], plans[name])

                knight_segment += 1

                scores.append(plans[name])

            # print(name, scores, sum(scores))

            loop += 1

        plans[name] = sum(scores)

    sorted_plans = dict(sorted(plans.items(), key=lambda item: item[1]))

    # print(sorted_plans)

    result = ''
    for key, _ in sorted_plans.items():
        result += key

    result = result[::-1]

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

track="""S+= +=-== +=++=     =+=+=--=    =-= ++=     +=-  =+=++=-+==+ =++=-=-=--
- + +   + =   =     =      =   == = - -     - =  =         =-=        -
= + + +-- =-= ==-==-= --++ +  == == = +     - =  =    ==++=    =++=-=++
+ + + =     +         =  + + == == ++ =     = =  ==   =   = =++=
= = + + +== +==     =++ == =+=  =  +  +==-=++ =   =++ --= + =
+ ==- = + =   = =+= =   =       ++--          +     =   = = =--= ==++==
=     ==- ==+-- = = = ++= +=--      ==+ ==--= +--+=-= ==- ==   =+=    =
-               = = = =   +  +  ==+ = = +   =        ++    =          -
-               = + + =   +  -  = + = = +   =        +     =          -
--==++++==+=+++-= =-= =-+-=  =+-= =-= =--   +=++=+++==     -=+=++==+++-"""

with open('input_p2.txt', 'r') as f:
    input_data = [line.strip() for line in f]
    answer = calculate_solution(input_data, track)

    print(f'Solution is {answer}')
