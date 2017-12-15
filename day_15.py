from __future__ import division, print_function
import os
from my_utils.tests import test_function


def parse_input(string):
    return [int(ll.split(' ')[-1]) for ll in string.split('\n')]


def part_1(starts, factors=[16807, 48271], divider=2147483647, 
           nr_tests=40000000):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    values = parse_input(starts)
    judge_count = 0
    for ii in range(nr_tests):
        for jj, vv in enumerate(values):
            values[jj] = vv * factors[jj] % divider
        bin_vals = [bin(vv)[2:].zfill(16)[-16:] for vv in values]
        if len(set(bin_vals)) == 1:
            judge_count += 1
    return judge_count


def part_2(starts, factors=[16807, 48271], divider=2147483647, 
           nr_tests=5000000, gen_dividers=[4, 8]):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    values = parse_input(starts)
    judge_count = 0
    for ii in range(nr_tests):
        for jj, vv in enumerate(values):
            vv = vv * factors[jj] % divider
            while vv % gen_dividers[jj] != 0:
                vv = vv * factors[jj] % divider
            values[jj] = vv
        bin_vals = [bin(vv)[2:].zfill(16)[-16:] for vv in values]
        if len(set(bin_vals)) == 1:
            judge_count += 1
    return judge_count


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
    test1_data = """Generator A starts with 65
Generator B starts with 8921"""
    
    test_data1 = {
        'inputs': [test1_data],
        'outputs': [588]
    }
    test_data2 = {
        'inputs': [test1_data],
        'outputs': [309]
    }
    
    # Code to import the actual puzzle input
    with open('./inputs/day_15.txt') as f:
        puzzle_input = f.read().strip()
#        puzzle_input = [line.rstrip('\n') for line in f]

    # Main call: performs testing and calculates puzzle outputs
    main(test_datas=[test_data2],
         functions=[part_2],
         puzzle_input=puzzle_input,
         test_functions=None)

    # main(test_datas=[test_data1, test_data2],
    #      functions=[part_1, part_2],
    #      puzzle_input=puzzle_input)
