from __future__ import division, print_function
import os
from my_utils.tests import test_function


def parse_tree(tower_str):
    tower_dict = {}
    tower_list = tower_str.strip().split('\n')
    for ll in tower_list:
        name, rest = ll.split(' ', 1)
        rest = rest.split(' -> ')
        if len(rest) == 2:
            weight, children = rest
            children = children.split(', ')
        else:
            weight = rest[0]
            children = None
        weight = int(weight[1:-1])
        tower_dict[name] = {'weight': weight, 'children': children}
    return tower_dict


def make_parents(tower_dict):
    for name in tower_dict:
        if tower_dict[name]['children'] is not None:
            children = tower_dict[name]['children']
            for child in children:
                try:
                    tower_dict[child]['parents'].append(name)
                except:
                    tower_dict[child]['parents'] = [name]
    return tower_dict
    

def weigh_children(name, tower_dict):
    cumulative_weight = tower_dict[name]['weight']
    children = tower_dict[name]['children']
    if children is not None:  # you're not a leaf
        child_weights = []
        for child in children:
            child_weights += [weigh_children(child, tower_dict)]
        cumulative_weight += sum(child_weights)
        tower_dict[name]['cumulative_weight'] = cumulative_weight
        return cumulative_weight
    else:  # you're a leaf
        tower_dict[name]['cumulative_weight'] = cumulative_weight
        return cumulative_weight


def find_fattie(name, tower_dict):
    children = tower_dict[name]['children']
    if children is not None:  # you're not a leaf
        child_weights = []
        for child in children:
            child_weights += [tower_dict[child]['cumulative_weight']]
        if len(set(child_weights)) != 1:
            print('{} has unbalanced children {} {}'.format(
                    name, children, child_weights))
            for ii, weight in enumerate(child_weights):
                other_weights = [x for jj, x in enumerate(child_weights) 
                                 if jj != ii]
                if weight not in other_weights:
                    odd_weight = weight
                    odd_child = children[ii]
                    odd_child_weight = tower_dict[odd_child]['weight']
                    real_weight = other_weights[0]
                    break
            weight_diff = odd_weight - real_weight
            adj_odd_child_weight = odd_child_weight - weight_diff
            print('The odd child is {} ({}), whose cumulative weight is {}, but '
                  'should be {} => its weight should be {} - {} = {}'.format(
                          odd_child, odd_child_weight, odd_weight, 
                          real_weight, odd_child_weight, 
                          weight_diff, adj_odd_child_weight))
            find_fattie(odd_child, tower_dict)
        else: 
            return name
        

def part_1(tower_str):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    tower_dict = make_parents(parse_tree(tower_str))
    for name in tower_dict:
        try:
            parents = tower_dict[name]['parents']
        except:
            parents = None
        if parents is None:
            break
    return name


def part_2(tower_str):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    tower_dict = make_parents(parse_tree(tower_str))
    root = part_1(tower_str)
    weigh_children(part_1(tower_str), tower_dict)
    return find_fattie(root, tower_dict)


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
    test1 = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
    """
    
    test_data1 = {
        'inputs': [test1],
        'outputs': ['tknk']
    }
    test_data2 = {
        'inputs': [test1],
        'outputs': ['tknk']
    }
    
    # Code to import the actual puzzle input
    with open('./inputs/day_7.txt') as f:
        puzzle_input = f.read().strip()

    # Main call: performs testing and calculates puzzle outputs
    main(test_datas=[test_data1, test_data2],
         functions=[part_1, part_2],
         puzzle_input=puzzle_input)

    # main(test_datas=[test_data1, test_data2],
    #      functions=[part_1, part_2],
    #      puzzle_input=puzzle_input)
