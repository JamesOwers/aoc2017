from __future__ import division, print_function
import os
from my_utils.tests import test_function


def make_graph(graph_str):
    graph_list = graph_str.strip().split('\n')
    graph_list = [gg.split(' <-> ') for gg in graph_list]
    graph = dict([(int(k), v.split(', ')) for k, v in graph_list])
    for node in graph:
        graph[node] = [int(v) for v in graph[node]]
    return graph


def get_conns(idx, graph, conns=[]):
    for conn in graph[idx]:
        if conn not in conns:
            conns = get_conns(conn, graph, conns=conns + [conn])
    return conns
            

def part_1(graph_str):
    """Function which calculates the solution to part 1
    
    Arguments
    ---------
    
    Returns
    -------
    """
    graph = make_graph(graph_str)
    conn_to_zero = get_conns(0, graph)
    return len(conn_to_zero)


def part_2(graph_str):
    """Function which calculates the solution to part 2
    
    Arguments
    ---------
    
    Returns
    -------
    """
    graph = make_graph(graph_str)
    groups = []
    for node in graph:
        if len(groups) == 0:
            groups = [get_conns(node, graph)]
        else:
            seen = 0
            for group in groups:
                if node in group:
                    seen = 1
            if seen:
                continue
            else:
                groups.append(get_conns(node, graph))
    return len(groups)


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
    graph_str1 = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""

    test_data1 = {
        'inputs': [graph_str1],
        'outputs': [6]
    }
    test_data2 = {
        'inputs': [graph_str1],
        'outputs': [2]
    }
    
    # Code to import the actual puzzle input
    with open('./inputs/day_12.txt') as f:
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
