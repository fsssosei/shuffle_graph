'''
shuffle_graph - This is a graph shuffling package.
Copyright (C) 2020  sosei

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

from typing import TypeVar, Optional
from networkx.classes.graph import Graph
from networkx.classes.digraph import DiGraph
from networkx.classes.multigraph import MultiGraph
from networkx.classes.multidigraph import MultiDiGraph
from complete_shuffle_package import *

__all__ = ['shuffle_graph', 'prng_type_tuple', 'default_prng_type']

NetworkXGraphObject = TypeVar('NetworkXGraphObject', Graph, DiGraph, MultiGraph, MultiDiGraph)

def shuffle_graph(data_graph: NetworkXGraphObject, seed: Optional[int] = None, prng_type: str = default_prng_type) -> NetworkXGraphObject:
    '''
        Returns a new graph, shuffling the order of the nodes in the input data_graph, but the relationship between the nodes remains the same. The data_graph doesn't change.
        
        Parameters
        ----------
        data_graph: NetworkXGraphObject
            A NetworkX graph object.
        
        seed: int, default None
            The seed of a pseudo-random number generator.
        
        prng_type: str, default default_prng_type
            Specifies the pseudo-random number generator algorithm to use.
        
        Returns
        -------
        new_order_data_graph: NetworkXGraphObject
            Returns a new graph that shuffles the order of nodes but keeps the relationships between them the same.
        
        Examples
        --------
        >>> from networkx.classes.graph import Graph
        >>> G = Graph({0: {1: {}}, 1: {0: {}, 2: {}}, 2: {1: {}, 3: {}}, 3: {2: {}, 4: {}}, 4: {3: {}}})
        >>> seed = 170141183460469231731687303715884105727
        >>> shuffle_graph(G, seed).adj  #Set seed to make the results repeatable.
        AdjacencyView({1: {0: {}, 2: {}}, 2: {1: {}, 3: {}}, 3: {2: {}, 4: {}}, 4: {3: {}}, 0: {1: {}}})
    '''
    assert isinstance(data_graph, (Graph, DiGraph, MultiGraph, MultiDiGraph)), f'data_graph must be an NetworkXGraphObject, got type {type(data_graph).__name__}'
    assert isinstance(seed, (int, type(None))), f'seed must be an int or None, got type {type(seed).__name__}'
    assert isinstance(prng_type, str), f'prng_type must be an str, got type {type(prng_type).__name__}'
    if isinstance(seed, int) and (seed < 0): raise ValueError('seed must be >= 0')
    if prng_type not in prng_type_tuple: raise ValueError('The string for prng_type is not in the list of implemented algorithms.')
    
    from networkx.convert import from_dict_of_dicts
    
    list_of_nodes = list(data_graph.nodes)
    pr_complete_shuffle(list_of_nodes, seed, prng_type)
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
