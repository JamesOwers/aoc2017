from __future__ import division, print_function
import os
from my_utils.tests import test_function
from collections import defaultdict


def part_1(lines):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    var_dict = defaultdict(int)
    for line in lines:
        line = line.replace('inc', '+').replace('dec', '-')
        inst_expr, cond_expr = line.split(' if ', 1)
        edit_var, edit_op = inst_expr.split(' ', 1)
        cond_var, cond = cond_expr.split(' ', 1)
        if eval('{} {}'.format(var_dict[cond_var], cond)):
            var_dict[edit_var] = \
                eval('{} {}'.format(var_dict[edit_var], edit_op))
#    max(var_dict.iterkeys(), key=(lambda key: var_dict[key]))
    return max(var_dict.values())


def part_2(lines):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    max_value = None
    var_dict = defaultdict(int)
    for line in lines:
        line = line.replace('inc', '+').replace('dec', '-')
        inst_expr, cond_expr = line.split(' if ', 1)
        edit_var, edit_op = inst_expr.split(' ', 1)
        cond_var, cond = cond_expr.split(' ', 1)
        if eval('{} {}'.format(var_dict[cond_var], cond)):
            var_dict[edit_var] = \
                eval('{} {}'.format(var_dict[edit_var], edit_op))
            if var_dict[edit_var] > max_value:
                max_value = var_dict[edit_var]
#    max(var_dict.iterkeys(), key=(lambda key: var_dict[key]))
    return max_value


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
    test1 = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10""".split('\n')
    
    
    test_data1 = {
        'inputs': [test1],
        'outputs': [1]
    }
    test_data2 = {
        'inputs': [test1],
        'outputs': [10]
    }
    
    # Code to import the actual puzzle input
    with open('./inputs/day_8.txt') as f:
        puzzle_input = [line.rstrip('\n') for line in f]

    # Main call: performs testing and calculates puzzle outputs
    main(test_datas=[test_data1, test_data2],
         functions=[part_1, part_2],
         puzzle_input=puzzle_input)

    # main(test_datas=[test_data1, test_data2],
    #      functions=[part_1, part_2],
    #      puzzle_input=puzzle_input)
