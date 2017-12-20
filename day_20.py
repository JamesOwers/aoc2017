from __future__ import division, print_function
import os
from my_utils.tests import test_function
#from collections import defaultdict
import re


def parse_string(update_str):
    updates = [re.findall("<([ ,0-9\-]+)>", inst) for 
               inst in update_str.split('\n')]
    updates = [[coord.strip().split(',') for coord in ll] for ll in updates]
    updates = [[[int(coord) for coord in coord_list] 
                for coord_list in ll] 
                for ll in updates]
    updates = [{'p':p, 'v':v, 'a':a} for p, v, a in updates]
    return updates


def update_state(updates, destruction=False):
    for ii, coords in enumerate(updates):
        if coords != 'kaput':
            new_v = [sum(xx) for xx in zip(coords['v'], coords['a'])]
            new_p = [sum(xx) for xx in zip(coords['p'], new_v)]
            updates[ii]['v'] = new_v
            updates[ii]['p'] = new_p
    if destruction:  # check for collisions
        for ii, particle in enumerate(updates):
            if particle != 'kaput':
                this_p = particle['p']
                for jj in range(ii + 1, len(updates)):
                    other_particle = updates[jj]
                    if other_particle != 'kaput':
                        that_p = other_particle['p']
                    if this_p == that_p:
                        updates[ii] = 'kaput'
                        updates[jj] = 'kaput'
    return updates


def part_1(update_str):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    initial_state = parse_string(update_str)
    new_state = update_state(initial_state)
#    print('prev: {}, new: {}'.format(update_str, new_state))
#    distances = [sum([abs(coord) for coord in ss['p']]) for ss in new_state]
#    min_idx = distances.index(min(distances))
    # particle with smallest abs accelleration will be closest to 0 in long term
    accels = [sum([abs(coord) for coord in ss['a']]) for ss in new_state]
    min_idx = accels.index(min(accels))
    return min_idx


def part_2(update_str, max_iters=1000, visualize=False):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    states = parse_string(update_str)
    for ii in range(max_iters):
        states = update_state(states, destruction=True)
    nr_surviving = len(states) - sum([particle == 'kaput' for particle in states])
    return nr_surviving


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
    tst1_list = """p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>

p=< 4,0,0>, v=< 1,0,0>, a=<-1,0,0>
p=< 2,0,0>, v=<-2,0,0>, a=<-2,0,0>

p=< 4,0,0>, v=< 0,0,0>, a=<-1,0,0>
p=<-2,0,0>, v=<-4,0,0>, a=<-2,0,0>

p=< 3,0,0>, v=<-1,0,0>, a=<-1,0,0>
p=<-8,0,0>, v=<-6,0,0>, a=<-2,0,0>""".split('\n\n')
    tst2_list = """p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
p=< 6,0,0>, v=< 0,0,0>, a=<-2,0,0>

p=< 4,0,0>, v=< 1,0,0>, a=<-1,0,0>
p=< 2,0,0>, v=<-2,0,0>, a=<-2,0,0>

p=< 4,0,0>, v=< 0,0,0>, a=<-1,0,0>
p=<-2,0,0>, v=<-4,0,0>, a=<-2,0,0>

p=< 3,0,0>, v=<-1,0,0>, a=<-1,0,0>
p=<-8,0,0>, v=<-6,0,0>, a=<-2,0,0>""".split('\n\n')
    test_data1 = {
        'inputs': tst1_list,
#        'outputs': [[4, 2], [4, 2], [3, 8], [1, 16]]
        'outputs': [0, 0, 0, 0]
    }
    test_data2 = {
        'inputs': tst2_list,
        'outputs': [0, 2, 2, 2]
    }
    
    # Code to import the actual puzzle input
    with open('./inputs/day_20.txt') as f:
        puzzle_input = f.read().strip()
#        puzzle_input = [line.rstrip('\n') for line in f]

    # Main call: performs testing and calculates puzzle outputs
    main(test_datas=[test_data2],
         functions=[part_2],
         puzzle_input=puzzle_input,
         test_functions=None)

    # main(test_datas=[test_data1, test_data2],
    #      functions=[part_1, part_2],
    #      puzzle_input=puzzle_input)


#    ## Noodling
#    import matplotlib.pyplot as plt
#    max_x = 10000
#    for ii in range(100):
    ## They don't start on top of each other
#    ps = [tuple(pp['p']) for pp in parse_string(puzzle_input)]
#    len(ps)
#    len(set(ps))
    