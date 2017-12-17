from __future__ import division, print_function
import os
from my_utils.tests import test_function
import string

def spin(inst_string, programs):
    nr = int(inst_string)
    if nr == 0:
        return programs
    old_programs = programs[:]
    programs[0:nr] = old_programs[-nr:]
    programs[nr:] = old_programs[0:-nr]
    return programs


def exchange(inst_string, programs):
    pid1, pid2 = [int(ii) for ii in inst_string.split('/')]
    val1 = programs[pid1]
    val2 = programs[pid2]
    programs[pid1] = val2
    programs[pid2] = val1
    return programs


def partner(inst_string, programs):
    pname1, pname2 = inst_string.split('/')
    pid1 = programs.index(pname1)
    pid2 = programs.index(pname2)
    programs[pid1] = pname2
    programs[pid2] = pname1
    return programs


MOVE_FUN = {
    's': spin,
    'x': exchange,
    'p': partner
}


def part_1(inst_string, programs=list(string.ascii_lowercase[:16])):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    instruction_list = inst_string.split(',')
    for instr in instruction_list:
        programs = MOVE_FUN[instr[0]](instr[1:], programs)
    return ''.join(programs)


def part_2(inst_string, nr_dances=int(1e9), 
           programs=list(string.ascii_lowercase[:16])):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    configs = {''.join(programs): 0}
    cycle_detected = 0
    for ii in range(1, nr_dances+1):
        this_programs = part_1(inst_string, programs=programs)
#        print('iter {}: {}'.format(ii, this_programs))
        if this_programs in configs:
            cycle_detected = 1
            break
        else:
            configs[this_programs] = ii
            programs = list(this_programs)
    if cycle_detected:
        programs = list(this_programs)
        first_occurence = configs[this_programs]
        cycle_len = ii - first_occurence
        remaining_iters = (nr_dances - ii) % cycle_len
#        print('cycle detected @{}, focc {}, cyclen {}, remain {} from {}'.\
#              format(ii, first_occurence, cycle_len, remaining_iters, nr_dances))
        for jj in range(remaining_iters):
            programs = list(part_1(inst_string, programs=programs))
    return ''.join(programs)


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
        'inputs': ['s1,x3/4,pe/b'],
        'outputs': ['baedc']
    }
    test_data2 = {
        'inputs': ['s1,x3/4,pe/b'],
        'outputs': ['ceadb']  # contains a cycle of length 4
                              # this answer at iter 2 % 4
    }
    
    # Code to import the actual puzzle input
    with open('./inputs/day_16.txt') as f:
        puzzle_input = f.read().strip()
#        puzzle_input = [line.rstrip('\n') for line in f]

    
    part_1_test = lambda x: part_1(x, programs=list(string.ascii_lowercase[:5]))
    part_2_test = lambda x: part_2(x, nr_dances=18, programs=list(string.ascii_lowercase[:5]))
    
    # Main call: performs testing and calculates puzzle outputs
    main(test_datas=[test_data2],
         functions=[part_2],
         puzzle_input=puzzle_input,
         test_functions=[part_2_test])

    # main(test_datas=[test_data1, test_data2],
    #      functions=[part_1, part_2],
    #      puzzle_input=puzzle_input)
