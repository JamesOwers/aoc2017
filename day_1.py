from __future__ import division, print_function
import os
from utils.tests import test_function


def solve_capcha(capcha_str):
    capcha = [int(cc) for cc in list(capcha_str)]
    total = 0
    for ii in range(len(capcha)):
         if capcha[ii] == capcha[ii - 1]:
             total += capcha[ii]
    return total


def solve_capcha2(capcha_str):
    capcha = [int(cc) for cc in list(capcha_str)]
    total = 0
    capcha_len = len(capcha)
    for ii in range(capcha_len):
         if capcha[ii] == capcha[ii - capcha_len//2]:
             total += capcha[ii]
    return total


part_1 = solve_capcha
part_2 = solve_capcha2


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
        'inputs': ['1122', '1111', '1234', '91212129'],
        'outputs': [3, 4, 0, 9]
    }
    test_data2 = {
        'inputs': ['1212', '1221', '123425', '123123', '12131415'],
        'outputs': [6, 0, 4, 12, 4]
    }
    with open('./inputs/day_1.txt') as f:
        puzzle_input = f.read().strip()

    main(test_datas=[test_data1, test_data2],
         functions=[part_1, part_2],
         puzzle_input=puzzle_input)
