from __future__ import division, print_function
import os
from my_utils.tests import test_function
from collections import defaultdict
import string


def get_val(this_str, registers):
    try:
        val = int(this_str)
    except:
        val = registers[this_str]
    return val


def part_1(instruction_str):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    inst_list = instruction_str.split('\n')
    curr_idx = 0
    registers = defaultdict(int)
    nr_muls = 0
    while curr_idx < len(inst_list) and curr_idx >= 0:
        fun_str, in_str = inst_list[curr_idx].split(' ', 1)
        if fun_str == 'set':
            reg_name, val_str = in_str.split(' ')
            val = get_val(val_str, registers)
            registers[reg_name] = val
            curr_idx += 1
        elif fun_str == 'sub':
            reg_name, val_str = in_str.split(' ')
            val = get_val(val_str, registers)
            registers[reg_name] -= val
            curr_idx += 1
        elif fun_str == 'mul':
            nr_muls += 1
            reg_name, val_str = in_str.split(' ')
            val = get_val(val_str, registers)
            registers[reg_name] *= val
            curr_idx += 1
        elif fun_str == 'jnz':
            check_val, jump_val = [get_val(ss, registers) for ss in in_str.split(' ')]
            if check_val != 0:
                curr_idx += jump_val
            else:
                curr_idx += 1
        else:
            print("Don't recognise {} as an operation".format(fun_str))
            raise ValueError()
    return nr_muls



def part_2(instruction_str):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    inst_list = instruction_str.split('\n')
    curr_idx = 0
    registers = defaultdict(int)
#    registers['a'] = 1
    registers['a'] = 1
#    for letter in string.lowercase[:8]:
#        print('\t{}: {}'.format(letter, registers[letter]))
    idx_list = []
#    for ii in range(10000):
    ii = -1
    while True:
        ii += 1
#        if ii == 1:   
#            registers['b'] = 10
#        if ii == 2:
#            registers['c'] = 10 - -10 * 17
#        if ii == 8:
#            print('hacking the process: setting b to c (iterates till then)')
#            registers['b'] = registers['c']
#            print('b set to c = {}'.format(registers['c']))
        if ii == 8:
            registers['b'] = 3
            registers['c'] = 3 + 6*17
            # answer registers['h'] should be nr non-primes in:
            #     [3, 20, 37, 54, 71, 88, 105]
            # i.e. 4
        idx_list.append(curr_idx)
        if curr_idx >= len(inst_list) or curr_idx < 0:
            print('prog end')
            break
#        print('INSTR {}, {}:'.format(curr_idx, inst_list[curr_idx]))
#        _ = raw_input('>')
        fun_str, in_str = inst_list[curr_idx].split(' ', 1)
        if fun_str == 'set':
            reg_name, val_str = in_str.split(' ')
            val = get_val(val_str, registers)
            registers[reg_name] = val
            curr_idx += 1
        elif fun_str == 'sub':
            reg_name, val_str = in_str.split(' ')
            val = get_val(val_str, registers)
            registers[reg_name] -= val
            curr_idx += 1
        elif fun_str == 'mul':
            reg_name, val_str = in_str.split(' ')
            val = get_val(val_str, registers)
            registers[reg_name] *= val
            curr_idx += 1
        elif fun_str == 'jnz':
            check_val, jump_val = [get_val(ss, registers) for ss in in_str.split(' ')]
            if check_val != 0:
                curr_idx += jump_val
            else:
                curr_idx += 1
        else:
            print("Don't recognise {} as an operation".format(fun_str))
            raise ValueError()
#        for letter in string.lowercase[:8]:
#            print('\t{}: {}'.format(letter, registers[letter]))
    return registers


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
        'inputs': [],
        'outputs': []
    }
    test_data2 = {
        'inputs': [],
        'outputs': []
    }
    
    # Code to import the actual puzzle input
    with open('./inputs/day_23.txt') as f:
        puzzle_input = f.read().strip()
#        puzzle_input = [line.rstrip('\n') for line in f]

    # Main call: performs testing and calculates puzzle outputs
    main(test_datas=[test_data1],
         functions=[part_2],
         puzzle_input=puzzle_input,
         test_functions=None)

    # main(test_datas=[test_data1, test_data2],
    #      functions=[part_1, part_2],
    #      puzzle_input=puzzle_input)

## After 10 setup iterations
#        a: 1
#        b: 106700
#        c: 123700
#        d: 2
#        e: 5
#        f: 1
#        g: -106695
#        h: 0
    
# Then cycle is [11, 12, 13, 14, 16, 17, 18, 19]
#[(11, 'set g d'),
# (12, 'mul g e'),
# (13, 'sub g b'),
# (14, 'jnz g 2'),
# (16, 'sub e -1'),
# (17, 'set g e'),
# (18, 'sub g b'),
# (19, 'jnz g -8')]
    
# process will change when d * e = b
# command 15: set f 0
# i.e. if b has ANY factor then set f = 0
# this then adds one to the total stored in h
# the next value checked is b + 17

# Therefore the total stored in h is the number of non-primes in set
# [106700 + ii*17 for ii in range(1001)]


#def is_prime(a):
#    return all(a % i for i in xrange(2, a))
#
#len([106700 + ii*17 for ii in range(1001) if not is_prime(106700 + ii*17)])
