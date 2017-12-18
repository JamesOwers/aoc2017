from __future__ import division, print_function
import os
from my_utils.tests import test_function
from collections import defaultdict, deque


def get_val(this_str, registers):
    try:
        val = int(this_str)
    except:
        val = registers[this_str]
    return val


def sound_reg(in_str, curr_idx=None, registers=None, sounds=None, read_idx=None, curr_prog=None):
    freq = get_val(in_str, registers)
    sounds.append(freq)
    curr_idx += 1
    return curr_idx, registers, sounds


def set_reg(in_str, curr_idx=None, registers=None, sounds=None, read_idx=None, curr_prog=None):
    reg_name, val_str = in_str.split(' ')
    val = get_val(val_str, registers)
    registers[reg_name] = val
    curr_idx += 1
    return curr_idx, registers, sounds


def add_reg(in_str, curr_idx=None, registers=None, sounds=None, read_idx=None, curr_prog=None):
    reg_name, val_str = in_str.split(' ')
    val = get_val(val_str, registers)
    registers[reg_name] += val
    curr_idx += 1
    return curr_idx, registers, sounds


def mul_reg(in_str, curr_idx=None, registers=None, sounds=None, read_idx=None, curr_prog=None):
    reg_name, val_str = in_str.split(' ')
    val = get_val(val_str, registers)
    registers[reg_name] *= val
    curr_idx += 1
    return curr_idx, registers, sounds


def mod_reg(in_str, curr_idx=None, registers=None, sounds=None, read_idx=None, curr_prog=None):
    reg_name, val_str = in_str.split(' ')
    val = get_val(val_str, registers)
    registers[reg_name] %= val
    curr_idx += 1
    return curr_idx, registers, sounds


def recover_reg(in_str, curr_idx=None, registers=None, sounds=None, read_idx=None, curr_prog=None):
    val = get_val(in_str, registers)
    if val != 0:
        curr_idx = None
    else:
        curr_idx += 1
    return curr_idx, registers, sounds


def jump_reg(in_str, curr_idx=None, registers=None, sounds=None, read_idx=None, curr_prog=None):
    check_val, jump_val = [get_val(ss, registers) for ss in in_str.split(' ')]
    if check_val > 0:
        curr_idx += jump_val
    else:
        curr_idx += 1
    return curr_idx, registers, sounds


SOUND_FUNS = {
    'snd': sound_reg,
    'set': set_reg,
    'add': add_reg,
    'mul': mul_reg,
    'mod': mod_reg,
    'rcv': recover_reg,
    'jgz': jump_reg
    }


def receive_reg(in_str, curr_idx=None, registers=None, sends=None, read_idx=None, curr_prog=None):
    """
    Assumes the global var CURR_PROG is available
    """
    read_queue = sends[curr_prog - 1]  # the other program's send list
#    # Too expensive to access specific idx, popping instead
#    # LOL turned out it would probably have been fine to access with read_idx
#    # had implemented jump_reg incorrectly (condition != 0 should've been > 0)
#    this_read_idx = read_idx[curr_prog]
    try:
        val = read_queue.popleft()  # read_queue is appended with new sends
#        val = read_queue[this_read_idx]  # will raise IndexError if nothing received
        registers[in_str] = val
        read_idx[curr_prog] += 1  # changes globally (because it's a list obj)
        curr_idx += 1
    except:
        pass
#        print('Prog {} can\'t read id {} from queue: {}. Waiting...'.format(
#              curr_prog, this_read_idx, read_queue))
    return curr_idx, registers, sends


def send_reg(in_str, curr_idx=None, registers=None, sends=None, read_idx=None, 
             curr_prog=None):
    send_queue = sends[curr_prog]
    freq = get_val(in_str, registers)
    send_queue.append(freq)
    curr_idx += 1
    return curr_idx, registers, sends


COMM_FUNS = {
    'snd': send_reg,
    'set': set_reg,
    'add': add_reg,
    'mul': mul_reg,
    'mod': mod_reg,
    'rcv': receive_reg,
    'jgz': jump_reg
    }


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
    sounds = []
    while curr_idx < len(inst_list):
        fun_str, in_str = inst_list[curr_idx].split(' ', 1)
        fun = SOUND_FUNS[fun_str]
        curr_idx, registers, sounds = fun(in_str, curr_idx, registers, sounds)
        if curr_idx is None:
            print('First recoverey triggered')
            print('Sounds: {}'.format(sounds))
            return sounds[-1]
    print('Nothing recovered')
    return None


def part_2(instruction_str):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    SENT_COUNT = 0
    inst_list = instruction_str.split('\n')
    idx_list = [0, 0]
    registers = [defaultdict(int), defaultdict(int)]
    registers[0]['p'] = 0
    registers[1]['p'] = 1
    sends = [deque(), deque()]
    CURR_PROG = 0
    READ_IDX = [0, 0]  # Read inside functions (naughty)
                       # UPDATE: UNUSED NOW AS LIST TOO LARGE AND ACCESS TOO
                       # EXPENSIVE (using deques and popping instead)
    curr_idx = idx_list[CURR_PROG]
    waiting = False
    while True:
#        print(idx_list, registers, sends, CURR_PROG, READ_IDX, waiting)
        curr_idx = idx_list[CURR_PROG]
        if curr_idx < len(inst_list):
            fun_str, in_str = inst_list[curr_idx].split(' ', 1)
            if fun_str == 'snd' and CURR_PROG == 1:
                SENT_COUNT += 1
            fun = COMM_FUNS[fun_str]
            next_idx, registers[CURR_PROG], sends = fun(in_str, curr_idx, 
                               registers[CURR_PROG], sends, READ_IDX, CURR_PROG)
        else:
            next_idx == curr_idx
        if next_idx == curr_idx:  # this only happens if cant read or have
                                  # finished instructions
            if waiting:
#                print('Both programs waiting, terminating')
                # Both programs are waiting...terminate
                return SENT_COUNT
#                return registers
            else:
                # Signal this program is waiting and change program)
                waiting = True
                CURR_PROG = [0, 1][CURR_PROG - 1]
        else:
            waiting = False  # this program may have sent a value so other
                             # program should check again if it can go
            idx_list[CURR_PROG] = next_idx
    print('Something went wrong...')
    return None


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
    test_str1 = """set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2"""
    
    test_str2 = """snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d"""
    
    test_data1 = {
        'inputs': [test_str1],
        'outputs': [4]
    }
    test_data2 = {
        'inputs': [test_str2],
        'outputs': [3]
    }
    
    # Code to import the actual puzzle input
    with open('./inputs/day_18.txt') as f:
        puzzle_input = f.read().strip()
#        puzzle_input = [line.rstrip('\n') for line in f]

    # Main call: performs testing and calculates puzzle outputs
    main(test_datas=[test_data1, test_data2],
         functions=[part_1, part_2],
         puzzle_input=puzzle_input,
         test_functions=None)

    # main(test_datas=[test_data1, test_data2],
    #      functions=[part_1, part_2],
    #      puzzle_input=puzzle_input)
