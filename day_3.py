from __future__ import division, print_function
import os
from utils.tests import test_function
import math

def part_1(memory_loc):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    if memory_loc == 1:
        return 0
    else:
        layer_nr = 1
        while (2*layer_nr-1) ** 2 < memory_loc:  
            layer_nr += 1
        layer_nr -= 1  # 0-indexed layer number
        square_nr = (2 * (layer_nr+1) - 1) ** 2
        square_nr_prev = (2 * (layer_nr) - 1) ** 2
        perim_loc = memory_loc - square_nr_prev
        perim_len = square_nr - square_nr_prev
        side_len = perim_len / 4
        assert side_len == int(side_len)
        side_len = int(side_len)
        side_loc = perim_loc % side_len
#        print(memory_loc, layer_nr, perim_loc, perim_len, side_len, side_loc,
#              side_loc - math.floor(side_len / 2))
        nr_steps = layer_nr + abs(side_loc - math.floor(side_len / 2))
        return int(nr_steps)


def memory_loc_to_coords(memory_loc):
    if memory_loc == 1:
        layer_nr, side_nr, side_loc = 0, 0, 0
    else:
        layer_nr = 1
        while (2*layer_nr-1) ** 2 < memory_loc:  
            layer_nr += 1
        layer_nr -= 1  # 0-indexed layer number
        square_nr = (2 * (layer_nr+1) - 1) ** 2
        square_nr_prev = (2 * (layer_nr) - 1) ** 2
        perim_loc = memory_loc - square_nr_prev
        perim_len = square_nr - square_nr_prev
        side_len = perim_len / 4
        assert side_len == int(side_len)
        side_len = int(side_len)
        side_loc = perim_loc % side_len
        side_nr = int(math.floor(perim_loc / side_len)) % 4
    return layer_nr, side_nr, side_loc


def construct_matrix(stop_value):
    """Constructs a dictionary of memory_loc co-ordinates to values
    """
    memory_loc = 1
    value = 1
    matrix = {memory_loc: value}
    coord_matrix = {memory_loc_to_coords(memory_loc): value}
    while value < stop_value:
        memory_loc += 1
        layer_nr, side_nr, side_loc = memory_loc_to_coords(memory_loc)
        
    return matrix
    

def part_2(idx):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    return None


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
        'inputs': [1, 12, 23, 1024, 21, 10, 25, 4, 9],
        'outputs': [0, 3, 2, 31, 4, 3, 4, 1, 2]
    }
    test_data2 = {
        'inputs': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'outputs': [1, 1, 2, 4, 5, 10, 11, 23, 25]
    }
    
    # Code to import the actual puzzle input
    puzzle_input = 347991

    # Main call: performs testing and calculates puzzle outputs
    main(test_datas=[test_data1],
         functions=[part_1],
         puzzle_input=puzzle_input)

    # main(test_datas=[test_data1, test_data2],
    #      functions=[part_1, part_2],
    #      puzzle_input=puzzle_input)
