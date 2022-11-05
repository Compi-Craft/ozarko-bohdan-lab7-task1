"""
Chekcs whether edge is in graph
"""
def is_edge_in_graph(graph: dict, edge: tuple) -> bool:
    """
    (dict, tuple) -> bool
    Return True if graph contains a given edge and False otherwise.
    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """
    if edge[0] in graph and edge[1] in graph[edge[0]] or \
edge[1] in graph and edge[0] in graph[edge[1]]:
        return True
    return False
