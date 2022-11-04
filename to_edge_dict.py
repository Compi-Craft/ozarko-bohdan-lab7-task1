"""
Converts a graph
"""
from copy import deepcopy
def to_edge_dict(edge_list: list[list]) -> dict:
    """
    (list) -> (dict)
    Convert a graph from list of edges to dictionary of vertices.
    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
    graph_dict = dict()
    for i in edge_list:
        for j in i:
            temporary = deepcopy(i)
            temporary.remove(j)
            if j not in graph_dict:
                graph_dict.update({j: temporary})
            else:
                for element in temporary:
                    graph_dict[j].append(element)
                    graph_dict[j].sort()
    return graph_dict
