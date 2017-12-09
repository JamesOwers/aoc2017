from __future__ import division, print_function
import os
from my_utils.tests import test_function


def clear_garbage(stream, return_count=False):
    count = 0
    in_garbage = False
    ignore_next = False
    out = []
    for char in stream:
        if not in_garbage:
            if char == '<':
                in_garbage = True
            else:
                out.append(char)
        else:  # in garbage
            if not ignore_next:
                if char == '!':
                    ignore_next = True
                elif char == '>':
                    in_garbage = False
                else:
                    count += 1
            else:
                ignore_next = False
    s = ''.join(out)
    if return_count:
        s = (s, count)        
    return s


def part_1(stream):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    stream = clear_garbage(stream)
    depth = 0
    total = 0
    for char in stream:
        if char == '{':
            depth += 1
        elif char == '}':
            total += depth
            depth -= 1
    return total


def part_2(stream):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    stream, count = clear_garbage(stream, return_count=True)
    return count


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
        'inputs': ['{}', '{{{}}}', '{{},{}}', '{{{},{},{{}}}}', 
                   '{<a>,<a>,<a>,<a>}', '{{<ab>},{<ab>},{<ab>},{<ab>}}',
                   '{{<!!>},{<!!>},{<!!>},{<!!>}}', 
                   '{{<a!>},{<a!>},{<a!>},{<ab>}}'],
        'outputs': [1, 6, 5, 16, 1, 9, 9, 3]
    }
    test_data2 = {
        'inputs': ['<>', '<random characters>', '<<<<>', 
                   '<{!>}>', '<!!>', '<!!!>>', '<{o"i!a,<{i<a>'],
        'outputs': [0, 17, 3, 2, 0, 0, 10]
    }
    
    # Code to import the actual puzzle input
    with open('./inputs/day_9.txt') as f:
        puzzle_input = f.read().strip()

    # Main call: performs testing and calculates puzzle outputs
    main(test_datas=[test_data1, test_data2],
         functions=[part_1, part_2],
         puzzle_input=puzzle_input)
