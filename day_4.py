from __future__ import division, print_function
import os
from my_utils.tests import test_function


def part_1(passphrases):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    valid = []
    for pp in passphrases:
        pp_list = pp.split()
        pp_set = set(pp_list)
        if len(pp_list) != len(pp_set):
            valid += [0]
        else:
            valid += [1]
    return sum(valid)


def part_2(passphrases):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    pp_list = [pp.split() for pp in passphrases]
    pp_sorted_words = [[''.join(sorted(word)) for word in pp] 
                       for pp in pp_list]
    pp_sorted_words = [' '.join(pp) for pp in pp_sorted_words]
    return part_1(pp_sorted_words)


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
        'inputs': [['aa bb cc dd ee'], 
                   ['aa bb cc dd aa'], 
                   ['aa bb cc dd aaa']],
        'outputs': [1, 0, 1]
    }
    test_data2 = {
        'inputs': [['abcde fghij'], 
                   ['abcde xyz ecdab'], 
                   ['a ab abc abd abf abj'],
                   ['iiii oiii ooii oooi oooo'],
                   ['oiii ioii iioi iiio'],
                   ['oiii ioii iioi iiio iiii iiiii'],
                   ['abcde fghij', 'abcde fghkj']],
        'outputs': [1, 0, 1, 1, 0, 0, 2]
    }
    
    # Code to import the actual puzzle input
    with open('./inputs/day_4.txt') as f:
        puzzle_input = [line.rstrip('\n') for line in f]

    # Main call: performs testing and calculates puzzle outputs
    main(test_datas=[test_data1, test_data2],
         functions=[part_1, part_2],
         puzzle_input=puzzle_input)
