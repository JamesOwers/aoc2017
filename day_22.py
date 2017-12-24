from __future__ import division, print_function
import os
from my_utils.tests import test_function
from collections import defaultdict


DIRECTIONS = ['n', 'e', 's', 'w']
MOVEMENTS = dict(zip(DIRECTIONS, [(-1, 0), (0, 1), (1, 0), (0, -1)]))
PROCESS1 = {
    '.': '#',
    '#': '.'
}
PROCESS2 = {
    '.': 'W',  # Clean nodes become weakened.
    'W': '#',  # Weakened nodes become infected.
    '#': 'F',  # Infected nodes become flagged.
    'F': '.'  #Flagged nodes become clean.
}




class Worm(object):
    def __init__(self, loc=(0, 0), direction='n'):
        self.loc = loc
        self.direction = direction
        self.nr_infections = 0
        
    def get_location(self):
        return self.loc
    
    def turn_left(self):
        dir_idx = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[dir_idx - 1]
    
    def turn_right(self):
        dir_idx = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(dir_idx + 1) % len(DIRECTIONS)]

    def move(self):
        self.loc = tuple(ii + jj for ii, jj in 
                    zip(self.loc, MOVEMENTS[self.direction]))
        
    def burst(self, node_state):
        if node_state == '#':  # infected
            self.turn_right()
            node_state = '.'
        elif node_state == '.': # not infected
            self.turn_left()
            node_state = '#'
            self.nr_infections += 1
        else:
            raise ValueError('{} is an invalid node state'.format(node_state))
        self.move()
        return node_state



class Worm2(Worm):
    def __init__(self, loc=(0, 0), direction='n'):
        super(Worm2, self).__init__(loc, direction)
    
    def burst(self, node_state):
        if node_state == '.':  # clean
            self.turn_left()
            node_state = 'W'
        elif node_state == 'W':  # weakened 
            node_state = '#'
            self.nr_infections += 1
        elif node_state == '#':  # infected
            self.turn_right()
            node_state = 'F'
        elif node_state == 'F':  # flagged
            self.turn_right()
            self.turn_right()
            node_state = '.'
        else:
            raise ValueError('{} is an invalid node state'.format(node_state))
        self.move()
        return node_state



def initialise_grid(in_str):
    """Assumes in_str given in matrix format (i.e. location of character 
    corresponds to desired location in grid)"""
    grid_dict = defaultdict(lambda: '.')
    for ii, row_str in enumerate(in_str.split('\n')):
        row_str = row_str.strip()
        for jj, char in enumerate(row_str):
            grid_dict[(ii, jj)] = char
    centre_idx = (ii//2, jj//2)  # assumes all lines same length
    return grid_dict, centre_idx



def grid_dict_to_str(grid_dict, worm_loc=None, row_spacing=2):
    x0_coords, x1_coords = zip(*grid_dict.keys())
    x0_min, x0_max = min(x0_coords), max(x0_coords)
    x1_min, x1_max = min(x1_coords), max(x1_coords)
    grid_list = []
    spacer = [' ' for ii in range(row_spacing - 1)]
    for ii in range(x0_min, x0_max+1):
        grid_row_list = [' ']
        for jj in range(x1_min, x1_max+1):
            grid_row_list += [grid_dict[(ii, jj)]] + spacer
        grid_list += [grid_row_list]
    if worm_loc is not None:
#        row_len = row_spacing*(x1_max - x1_min)+1
#        worm_char = worm_loc[0]*row_len + worm_loc[1]*row_spacing
        grid_list[worm_loc[0]][worm_loc[1]*row_spacing] = '['
        grid_list[worm_loc[0]][worm_loc[1]*row_spacing + 2] = ']'
    grid_str = '\n'.join([''.join(row) for row in grid_list])
    return grid_str
    


def part_1(in_str):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    grid_dict, centre_idx = initialise_grid(in_str)
    worm = Worm(loc=centre_idx, direction='n')
    nr_bursts = 10000
    for bb in range(nr_bursts):
        worm_loc = worm.get_location()
        node_state = grid_dict[worm_loc]
#        print(worm_loc, worm.direction)
#        print(grid_dict_to_str(grid_dict, worm_loc))
        grid_dict[worm_loc] = worm.burst(node_state)
    return worm.nr_infections


def part_2(in_str):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    grid_dict, centre_idx = initialise_grid(in_str)
    worm = Worm2(loc=centre_idx, direction='n')
    nr_bursts = 10000000
#    nr_bursts = 100
    for bb in range(nr_bursts):
        worm_loc = worm.get_location()
        node_state = grid_dict[worm_loc]
#        print(worm_loc, worm.direction)
#        print(grid_dict_to_str(grid_dict, worm_loc))
        grid_dict[worm_loc] = worm.burst(node_state)
    return worm.nr_infections


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
    tst1_in = """..#
#..
..."""
    
    test_data1 = {
        'inputs': [tst1_in],
        'outputs': [5587]
    }
    test_data2 = {
        'inputs': [tst1_in],
        'outputs': [2511944]
    }
    
    # Code to import the actual puzzle input
    with open('./inputs/day_22.txt') as f:
        puzzle_input = f.read().strip()
#        puzzle_input = [line.rstrip('\n') for line in f]

    # Main call: performs testing and calculates puzzle outputs
    main(test_datas=[],
         functions=[part_2],
         puzzle_input=puzzle_input,
         test_functions=None)

    # main(test_datas=[test_data1, test_data2],
    #      functions=[part_1, part_2],
    #      puzzle_input=puzzle_input)
