from __future__ import division, print_function
import os
from my_utils.tests import test_function
import copy
import numpy as np


def part_1(memory, max_cycles=1000000, show_configs=False):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    N = len(memory)
    this_memory = memory
    configs = [copy.copy(this_memory)]
    nr_iters = 0
    for jj in range(max_cycles):
        # np.argmax returns only the first max when there is a tie
        max_idx = np.argmax(this_memory)
        max_val = this_memory[max_idx]
        this_memory[max_idx] = 0
        for ii in range(max_val):
            idx = (max_idx + ii + 1) % (N)
            this_memory[idx] += 1
        nr_iters += 1
        if this_memory in configs:
            configs += [copy.copy(this_memory)]
            break
        else:
            configs += [copy.copy(this_memory)]
    if show_configs:
        nr_iters = (nr_iters, configs)
    return nr_iters


def part_2(memory):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    nr_iters, configs = part_1(memory, show_configs=True)
    final_config = configs[-1]
    nr_configs = len(configs)
    idx = np.argmax([cc == final_config for cc in configs])
    cycle_len = nr_configs - idx - 1
    return cycle_len


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
        'inputs': [[0, 2, 7, 0]],
        'outputs': [5]
    }
    test_data2 = {
        'inputs': [[0, 2, 7, 0]],
        'outputs': [4]
    }
    
    # Code to import the actual puzzle input
    with open('./inputs/day_6.txt') as f:
        puzzle_input = [int(s) for s in f.read().split()]

    # Main call: performs testing and calculates puzzle outputs
    main(test_datas=[test_data1, test_data2],
         functions=[part_1, part_2],
         puzzle_input=puzzle_input)

