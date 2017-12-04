from __future__ import division, print_function
import os
from utils.tests import test_function
import math
import numpy as np


def part_1(memory_loc):
    """Get the manhattan distance from a location to the centre of a
    (1-indexed) spiral array

    Arguments
    ---------
    memory_loc : int, the location of the starting point. Locations are
        numbered anticlockwise from the centre, and head right first, e.g.
        5 4 3
        6 1 2
        7 8 9

    Returns
    -------
    nr_steps : int, The manhattan distance from memory_loc to '1'
        i.e. the centre
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
        nr_steps = layer_nr + abs(side_loc - math.floor(side_len / 2))
        return int(nr_steps)


def rehouse_matrix(matrix):
    """Convenience function to create a zero pad border around matrix
    """
    old_shape = matrix.shape
    new_shape = (old_shape[0] + 2, old_shape[1] + 2)
    old_matrix = matrix
    matrix = np.zeros(new_shape, dtype=int)
    matrix[1:-1, 1:-1] = old_matrix
    return matrix


def to_spiral(A):
    """Converts a matrix with normal indexing, to spiral indexing
    """
    A = np.array(A)
    B = np.empty_like(A)
    B.flat[base_spiral(*A.shape)] = A.flat
    return B


def from_spiral(A):
    """Converts a matrix with spiral indexing back to normal indexing
    """
    A = np.array(A)
    return A.flat[base_spiral(*A.shape)].reshape(A.shape)


def spiral_cw(A):
    """Creates a list of values in the order of a spiral index by
    slicing off the bottom row and rotating the remaining matrix
    anticlockwise repeatedly. Row values are recorded in reverse order
    such that, when read back, you read the bottom right matrix entry
    first, and spiral clockwise and inwards
    """
    A = np.array(A)
    out = []
    while A.size:
        out.append(A[-1][::-1])  # last row reversed
        A = A[:-1].T[::-1]       # cut last and rotate anticlock
    return np.concatenate(out)


def base_spiral(nrow, ncol):
    """Creates a spiral of size nrow, ncol"""
    return spiral_cw(np.arange(nrow*ncol).reshape(nrow, ncol))[::-1]


def memory_loc_to_coord(memory_loc, shape):
    """Gets the matrix coordinates of a location in a spiral array
    """
    nr_elems = shape**2
    shape = (shape, shape)
    matrix = to_spiral(np.arange(1, nr_elems+1).reshape(shape))
    coords = np.argwhere(matrix == memory_loc)[0]
    return coords


def construct_matrix(stop_value):
    """Builds numpy array sequentially from centre outwards
    """
    memory_loc = 1
    patch_sum = 1
    matrix = np.array([[patch_sum]])
    layer_nr = 1
    square_nr = (2 * (layer_nr) - 1) ** 2
    side_len = 1
    while patch_sum < stop_value:
        memory_loc += 1
        if memory_loc - 1 == square_nr:
            matrix = rehouse_matrix(matrix)
            layer_nr += 1
            square_nr = (2 * (layer_nr) - 1) ** 2
            side_len += 2
        coords = memory_loc_to_coord(memory_loc, side_len)
        idx0 = coords[0]
        min0 = idx0 - 1 if idx0 > 0 else 0                  # inclusive
        max0 = idx0 + 2 if idx0 < side_len else side_len+1  # exclusive
        idx1 = coords[1]
        min1 = idx1 - 1 if idx1 > 0 else 0
        max1 = idx1 + 2 if idx1 < side_len else side_len+1
        patch_sum = np.sum(matrix[min0:max0, min1:max1])
        matrix[idx0, idx1] = patch_sum
    return matrix


def part_2(stop_value):
    """Function which calculates the solution to part 2

    Arguments
    ---------
    stop_value : int, value at which to stop building the spiral array

    Returns
    -------
    max value in the constructed array
    """
    return np.max(construct_matrix(stop_value))


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
        'inputs': [1, 1, 2, 4, 5, 10, 11, 23, 25],
        'outputs': [1, 1, 2, 4, 5, 10, 11, 23, 25]
    }

    # Code to import the actual puzzle input
    puzzle_input = 347991

    # Main call: performs testing and calculates puzzle outputs
    main(test_datas=[test_data1, test_data2],
         functions=[part_1, part_2],
         puzzle_input=puzzle_input)
