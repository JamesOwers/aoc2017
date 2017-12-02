from __future__ import division, print_function
import os
from utils.tests import test_function
import numpy as np
from itertools import combinations
from fractions import gcd


def part_1(X):
    return np.sum(X.max(axis=1) - X.min(axis=1))


def part_2(X):
    ans = []
    for row in X:
        combs = combinations(row, 2)
        comb = [ii for ii in combs if (gcd(*ii) in ii)]
        assert len(comb) == 1
        comb = comb[0]
        ans += [max(comb) / min(comb)]
    return np.sum(ans)


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
        'inputs': [np.array([[5, 1, 9, 5]]), np.array([[7, 5, 3]]),
                   np.array([[2, 4, 6, 8]])],
        'outputs': [np.array(8), np.array(4), np.array(6)]
    }
    test_data2 = {
        'inputs': [np.array([[5, 9, 2, 8]]), np.array([[9, 4, 7, 3]]),
                   np.array([[3, 8, 6, 5]])],
        'outputs': [np.array(4), np.array(3), np.array(2)]
    }

    puzzle_input = np.genfromtxt('./inputs/day_2.txt', dtype=int)

    main(test_datas=[test_data1, test_data2],
         functions=[part_1, part_2],
         puzzle_input=puzzle_input)

    # main(test_datas=[test_data1, test_data2],
    #      functions=[part_1, part_2],
    #      puzzle_input=puzzle_input)
