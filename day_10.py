from __future__ import division, print_function
import os
from my_utils.tests import test_function


def create_hash(lengths, hash_length=256, preproc='list', rounds=1):
#    [chr(ii) for ii in [17, 31, 73, 47, 23]]
#    Out[43]: ['\x11', '\x1f', 'I', '/', '\x17']
#    \021  17  DC1  \x11  ^Q    (Device control 1) (XON) (Default UNIX START char.)
#    \037  31  US   \x1F  ^_    (Unit separator, Information separator one)
#    \027  23  ETB  \x17  ^W    (End of transmission block)
    if preproc == 'list':
        lengths = [int(ll) for ll in lengths.split(',')]
    if preproc == 'ascii':
        end_block = [17, 31, 73, 47, 23]
        if len(lengths) > 0:
            lengths = [ord(ll) for ll in lengths]
        else:
            lengths = []
        lengths += end_block
    hash_map = range(hash_length)
    skip_size = 0
    start_pos = 0
    for rr in range(rounds):
        for ll in lengths:
            end_pos = (start_pos + ll) % hash_length
#            print(ll, start_pos, end_pos)
            if ll > 1:
                for ii in range(ll // 2):
                    idx_end = end_pos - ii - 1
                    idx_start = (start_pos + ii) % hash_length
                    end_val = hash_map[idx_end]
                    start_val = hash_map[idx_start]
                    hash_map[idx_end] = start_val
                    hash_map[idx_start] = end_val
            start_pos = end_pos + skip_size % hash_length
            skip_size += 1
    return hash_map


def make_dense(hash_map):
    nr_blocks = len(hash_map) // 16  # f padding (always 256)
    dense = []
    for bb in range(nr_blocks):
        idx_start = bb * 16
        idx_end = (bb + 1) * 16
        block = hash_map[idx_start:idx_end]
        block_xor = reduce(lambda i, j: i ^ j, block)
        dense.append(block_xor)
    return dense


def to_hex(hash_map):
#    hex_map = [hex(ii).split('x')[1] for ii in hash_map]
#    hex_map = ['0{}'.format(ii) if len(ii)==1 else ii for ii in hex_map]
    hex_map = ['{:02x}'.format(ii) for ii in hash_map]
    return ''.join(hex_map)


def part_1(lengths, hash_length=256):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    hash_map = create_hash(lengths, hash_length)
    return hash_map[0] * hash_map[1]


def part_2(lengths):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    hash_map = create_hash(lengths, hash_length=256, preproc='ascii', rounds=64)
    dense_map = make_dense(hash_map)
    hex_str = to_hex(dense_map)
    return hex_str


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
        'inputs': ['3,4,1,5'],
        'outputs': [12]
    }
    test_data2 = {
        'inputs': ['', 'AoC 2017', '1,2,3', '1,2,4'],
        'outputs': ['a2582a3a0e66e6e86e3812dcb672a272',
                    '33efeb34ea91902bb2f59c9920caa6cd',
                    '3efbe78a8d82f29979031a4aa0b16a9d',
                    '63960835bcdc130f0b66d7ff4f6a5a8e']
    }
    
    # Code to import the actual puzzle input
    with open('./inputs/day_10.txt') as f:
        puzzle_input = f.read().strip()
#        puzzle_input = [line.rstrip('\n') for line in f]
      
    part_1_test = lambda lengths: part_1(lengths, hash_length=5)
    # Main call: performs testing and calculates puzzle outputs
    main(test_datas=[test_data1, test_data2],
         test_functions=[part_1_test, part_2],
         functions=[part_1, part_2],
         puzzle_input=puzzle_input)

    # main(test_datas=[test_data1, test_data2],
    #      functions=[part_1, part_2],
    #      puzzle_input=puzzle_input)
