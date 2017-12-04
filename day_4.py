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


def anagram_check(word_list):
    for jj, word in enumerate(word_list):  # anagram search
        word_letters = list(word)
        # only need to check forward
        for other_word in word_list[jj+1:]:
            is_anagram = 1
            other_word_letters = list(other_word)
            if len(other_word_letters) != len(word_letters):
                is_anagram = 0
            else:
                for letter in word_letters:
                    if letter not in other_word_letters:
                        is_anagram = 0
                        break
                    else:
                        other_word_letters.remove(letter) 
            # no need to continue with pp if anagram found
            if is_anagram:
                return 1
    return 0


def part_2(passphrases):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    valid = []    
    for pp in passphrases:
        pp_words = pp.split()
        pp_set = set(pp_words)
        if len(pp_words) == len(pp_set):  # no repeated words
            contains_anagram = anagram_check(pp_words)
            if contains_anagram == 1:
                vv = 0
            else:
                vv = 1
        else:  # there are repeated words
            vv = 0
        valid += [vv]
    return sum(valid)


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
