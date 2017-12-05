from __future__ import division, print_function
import os
from my_utils.tests import test_function
import copy

def part_1(jumps_orig):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    jumps = copy.copy(jumps_orig)
    nr_steps = 0
    loc = 0
    jumps_len = len(jumps)
    while loc < jumps_len and loc >= 0:
        jump_dist = jumps[loc]
        jumps[loc] += 1
        loc += jump_dist
        nr_steps += 1
    return nr_steps


def part_2(jumps_orig, show_exit_state=False):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    jumps = copy.copy(jumps_orig)
    nr_steps = 0
    loc = 0
    jumps_len = len(jumps)
    while loc < jumps_len and loc >= 0:
        jump_dist = jumps[loc]
        if jump_dist >= 3:
            jumps[loc] -= 1
        else:
            jumps[loc] += 1
        loc += jump_dist
        nr_steps += 1
    if show_exit_state:
        nr_steps = (nr_steps, jumps)
    return nr_steps


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
        'inputs': [[0, 3, 0, 1, -3]],
        'outputs': [5]
    }
    test_data2 = {
        'inputs': [[0, 3, 0, 1, -3]],
        'outputs': [10]
    }
    
    # Code to import the actual puzzle input
    with open('./inputs/day_5.txt') as f:
        puzzle_input = [int(line.rstrip('\n')) for line in f]

    # Main call: performs testing and calculates puzzle outputs
    main(test_datas=[test_data1, test_data2],
         functions=[part_1, part_2],
         puzzle_input=puzzle_input)
