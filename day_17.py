from __future__ import division, print_function
import os
from my_utils.tests import test_function


def create_buff(step_size, buff_max=2017):
    buff = [0]
    curr_pos = 0
    for buff_len in range(1, buff_max+1):
        curr_pos = (curr_pos + step_size) % buff_len
        curr_pos += 1
        buff.insert(curr_pos, buff_len)
    return buff


def simulate_buff(step_size, buff_max=2017):
    zero_pos = 0
    curr_pos = 0
    val_after_zero = None
    for buff_len in range(1, buff_max+1):
        curr_pos = (curr_pos + step_size) % buff_len
        curr_pos += 1
        if curr_pos == zero_pos + 1:
            val_after_zero = buff_len
        if curr_pos <= zero_pos:  # i.e. insert before if index same
            zero_pos += 1
    return val_after_zero


def part_1(step_size, buff_max=2017):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    buff = create_buff(step_size, buff_max=buff_max)
    idx = buff.index(buff_max)
    return buff[idx + 1 % len(buff)]


def part_2(step_size):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    return simulate_buff(step_size, int(50*1e6))


def main(test_datas, functions, puzzle_input=None, test_functions=None):
    if test_functions is None:
        test_functions = functions
    for ii, (test_data, fun) in enumerate(zip(test_datas, test_functions)):
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
        'inputs': [3],
        'outputs': [638]
    }
    test_data2 = {
        'inputs': [],
        'outputs': []
    }
    
    # Code to import the actual puzzle input
    with open('./inputs/day_17.txt') as f:
        puzzle_input = f.read().strip()
        puzzle_input = int(puzzle_input)
#        puzzle_input = [line.rstrip('\n') for line in f]

    # Main call: performs testing and calculates puzzle outputs
    main(test_datas=[],
         functions=[part_2],
         puzzle_input=puzzle_input,
         test_functions=None)

    # main(test_datas=[test_data1, test_data2],
    #      functions=[part_1, part_2],
    #      puzzle_input=puzzle_input)
