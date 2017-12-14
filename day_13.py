from __future__ import division, print_function
import os
from my_utils.tests import test_function


def list_to_dict(str_list):
    dict_list = [ss.split(': ') for ss in str_list]
    return {int(ii):int(jj) for ii, jj in dict_list}


def part_1(str_list):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    wall_dict = list_to_dict(str_list)
    trip_severity = 0
    for depth in wall_dict:
        rng = wall_dict[depth]
        if depth % ((rng - 2)*2 + 2) == 0:
            severity = depth * rng
            trip_severity += severity   
            print('Caught @ {}. Cost {}. Tot {}'.\
                  format(depth, severity, trip_severity))
    return trip_severity


def part_2(str_list, max_iters=10000000):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    wall_dict = list_to_dict(str_list)
    for ii in range(max_iters):
        caught = 0
        for depth in wall_dict:
            rng = wall_dict[depth]
            if (depth + ii) % ((rng - 2)*2 + 2) == 0:
                caught = 1
        if caught == 0:
            return ii


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
    test1_str = """0: 3
1: 2
4: 4
6: 4"""
    test1_str = test1_str.split('\n')
    test_data1 = {
        'inputs': [test1_str],
        'outputs': [24]
    }
    test_data2 = {
        'inputs': [test1_str],
        'outputs': [10]
    }
    
    # Code to import the actual puzzle input
    with open('./inputs/day_13.txt') as f:
#        puzzle_input = f.read().strip()
        puzzle_input = [line.rstrip('\n') for line in f]

    # Main call: performs testing and calculates puzzle outputs
#    main(test_datas=[test_data1],
#         functions=[part_1],
#         puzzle_input=puzzle_input,
#         test_functions=None)

    main(test_datas=[test_data1, test_data2],
         functions=[part_1, part_2],
         puzzle_input=puzzle_input)
