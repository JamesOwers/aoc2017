from __future__ import division, print_function
import os
from utils.tests import test_function


def part_1():
    return None


def part_2():
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
    test_data1 = {
        'inputs': [],
        'outputs': []
    }
    test_data2 = {
        'inputs': [],
        'outputs': []
    }
    with open('./inputs/day_x.txt') as f:
        puzzle_input = f.read().strip()

    main(test_datas=[test_data1],
         functions=[part_1],
         puzzle_input=None)

    # main(test_datas=[test_data1, test_data2],
    #      functions=[part_1, part_2],
    #      puzzle_input=puzzle_input)
