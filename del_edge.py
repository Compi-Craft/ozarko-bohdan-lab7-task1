"""
Deletes edge
"""
def del_edge(graph: dict, edge: tuple) -> dict:
    """
    (dict, tuple) -> (dict)
    Delete an edge from the graph and return a new graph.
    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    if edge[0] in list(graph.keys()) and edge[1] in list(graph.keys()):
        if edge[1] in graph[edge[0]]:
            graph[edge[0]].remove(edge[1])
        if edge[0] in graph[edge[1]]:
            graph[edge[1]].remove(edge[0])
    return graph
