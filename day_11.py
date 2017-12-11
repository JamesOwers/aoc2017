from __future__ import division, print_function
import os
from my_utils.tests import test_function
from collections import Counter


def sign(n):
    if n < 0:
        return -1
    else:
        return 1


def part_1(steps):
    """Function which calculates the solution to part 1
    Remap the hex grid to square grid

      \    /    \    /    \    /
       +--+      +--+ 0, 3 +--+
      /    \    /    \    /    \
    -+      +--+ 0, 2 +--+ 1, 4 +-
      \    /    \    /    \    /
       +--+ 0, 1 +--+ 1, 3 +--+
      /    \    /    \    /    \
    -+ 0, 0 +--+ 1, 2 +--+ 2, 4 +-
      \    /    \    /    \    /
       +--+ 1, 1 +--+ 2, 3 +--+
      /    \    /    \    /    \
    -+ 1, 0 +--+ 2, 2 +--+ 3, 4 +-
      \    /    \    /    \    /
       +--+ 2, 1 +--+ 3, 3 +--+
      /    \    /    \    /    \

    Arguments
    ---------

    Returns
    -------
    """
    step_freq = Counter(steps)
    # define ne sw as staying on same level
    vert = step_freq['s'] + step_freq['se'] \
        - step_freq['n'] - step_freq['nw']
    horiz = step_freq['ne'] + step_freq['se'] \
        - step_freq['sw'] - step_freq['nw']
    if sign(horiz) == sign(vert):
        diag_steps = min(abs(vert), abs(horiz))
        if vert < 0:
            vert += diag_steps
        else:
            vert -= diag_steps    
    return abs(horiz) + abs(vert)


def part_2(steps):
    """Function which calculates the solution to part 2

    Arguments
    ---------

    Returns
    -------
    """
    max_dist = 0
    for ii in range(len(steps)):
        dist = part_1(steps[:ii])
        if dist > max_dist:
            max_dist = dist
    return max_dist


def main(test_datas, functions, puzzle_input=None):
    for ii, (test_data, fun) in enumerate(zip(test_datas, functions)):
        nr_errors = test_function(fun, test_data)
        if nr_errors == 0:
            print('Pt. {} Tests Passed'.format(ii+1))

    if puzzle_input is not None:
        fn = os.path.basename(__file__)
        for ii, fun in enumerate(functions):
            ans = fun(puzzle_input)
            print('{} Pt. {} Solution: {}'.format(fn, ii+1, ans))


if __name__ == "__main__":
    # Testing data:
    #    - each element of input list will be passed to function
    #    - the relative element in output list is the expected output
    test_data1 = {
        'inputs': [['ne', 'ne', 'ne'],
                   ['ne', 'ne', 'sw', 'sw'],
                   ['ne', 'ne', 's', 's'],
                   ['se', 'sw', 'se', 'sw', 'sw'],
                   ['se', 'sw', 'se', 'sw', 'sw', 'nw'],
                   ['n', 'sw', 'n', 'sw', 'sw']],
        'outputs': [3, 0, 2, 3, 3, 3]
    }
    test_data2 = {
        'inputs': [],
        'outputs': []
    }

    # Code to import the actual puzzle input
    with open('./inputs/day_11.txt') as f:
        puzzle_input = f.read().strip()
        puzzle_input = puzzle_input.split(',')
#        puzzle_input = f.read().strip()
#        puzzle_input = [line.rstrip('\n') for line in f]

    # Main call: performs testing and calculates puzzle outputs
    main(test_datas=[test_data1],
         functions=[part_1, part_2],
         puzzle_input=puzzle_input)

    # main(test_datas=[test_data1, test_data2],
    #      functions=[part_1, part_2],
    #      puzzle_input=puzzle_input)
