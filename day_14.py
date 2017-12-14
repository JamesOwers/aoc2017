from __future__ import division, print_function
import os
from my_utils.tests import test_function
import day_10
import numpy as np
from skimage import measure


def hash_to_disk(hash_str):
    hashes = [day_10.part_2(hash_str + '-{}'.format(ii))
              for ii in range(128)]
    bin_hashes = [bin(int(hh, 16))[2:].zfill(len(hh)*4) for hh in hashes]
    disk = np.array([list(bb) for bb in bin_hashes], dtype=int)
    return disk


def part_1(hash_str):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    disk = hash_to_disk(hash_str)
    return np.sum(disk)


def part_2(hash_str):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    disk = hash_to_disk(hash_str)
    disk_labelled, nr_labs = measure.label(disk, neighbors=4, background=0,
                                           return_num=True)
    return nr_labs


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
        'inputs': ['flqrgnkx'],
        'outputs': [8108]
    }
    test_data2 = {
        'inputs': ['flqrgnkx'],
        'outputs': [1242]
    }
    
    # Code to import the actual puzzle input
    with open('./inputs/day_14.txt') as f:
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
