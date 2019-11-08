'''
shuffle_graph - This is a graph shuffling package.
Copyright (C) 2019  sosei

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

from networkx.classes.graph import Graph
from networkx.classes.digraph import DiGraph
from networkx.classes.multigraph import MultiGraph
from networkx.classes.multidigraph import MultiDiGraph

__all__: list = ['version', 'calculate_number_of_shuffles_required_under_default_random_function', 'shuffle_graph']

version = '1.0.1'

def calculate_number_of_shuffles_required_under_default_random_function(node_number: int) -> int:
    '''
        Python's random number function USES the Mersenne Twister algorithm, which has a period of 2**19937-1.If the total permutation of graph nodes is larger than the random function period, the card cannot be shuffled only once.
        The total permutation of a graph node is "factorial of the number of nodes".The number of binary digits of the total number of permutations can be calculated by Stirling's formula.

        >>> calculate_number_of_shuffles_required_under_default_random_function(1000)
        1
        >>> calculate_number_of_shuffles_required_under_default_random_function(10000)
        6
    '''
    import math
    if node_number > 0:
        bit_length_of_permutation_number = math.ceil(math.log2(2*math.pi*node_number)/2 + math.log2(node_number/math.e)*node_number)
        shuffle_number = math.ceil(bit_length_of_permutation_number/19937)
    else:
        shuffle_number = 0
    return shuffle_number

def shuffle_graph(data_graph: 'graph', shuffle_number: int, seed: int = None) -> 'graph':
    '''
        >>> G = Graph({0: {1: {}}, 1: {0: {}, 2: {}}, 2: {1: {}, 3: {}}, 3: {2: {}, 4: {}}, 4: {3: {}}})
        >>> shuffle_graph(G, 1, 65535).adj  #Set seed to make the results repeatable.
        AdjacencyView({3: {2: {}, 4: {}}, 4: {3: {}}, 1: {0: {}, 2: {}}, 2: {3: {}, 1: {}}, 0: {1: {}}})
    '''
    import random
    from networkx.convert import from_dict_of_dicts
    
    random.seed(seed)
    
    list_of_nodes = list(data_graph.nodes)
    for _i in range(shuffle_number):
        random.shuffle(list_of_nodes)
    new_order_data_graph = dict()
    for node in list_of_nodes:
        new_order_data_graph.update({node: data_graph[node]})
    if data_graph.is_directed():
        if data_graph.is_multigraph():
            new_order_data_graph = from_dict_of_dicts(new_order_data_graph, create_using = MultiDiGraph, multigraph_input = True)
        else:
            new_order_data_graph = from_dict_of_dicts(new_order_data_graph, create_using = DiGraph)
    else:
        if data_graph.is_multigraph():
            new_order_data_graph = from_dict_of_dicts(new_order_data_graph, create_using = MultiGraph, multigraph_input = True)
        else:
            new_order_data_graph = from_dict_of_dicts(new_order_data_graph, create_using = Graph)
    return new_order_data_graph
