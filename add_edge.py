"""
Adds edge to graph
"""
def add_edge(graph: dict, edge: tuple) -> dict:
    """
    (dict, tuple) -> dict
    Add a new edge to the graph and return new graph.
    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    if edge[0] not in graph:
        graph.update({edge[0]: []})
    graph[edge[0]].append(edge[1])
    if edge[1] not in graph:
        graph.update({edge[1]: []})
    graph[edge[1]].append(edge[0])
    return graph
