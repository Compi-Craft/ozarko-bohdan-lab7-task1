def del_node(graph: dict, node: int) -> dict:
    """
    (dict, int) -> (dict)
    Delete a node and all incident edges from the graph.
    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    if node in graph.keys():
        graph.pop(node)
        for i in graph:
            if node in graph[i]:
                graph[i].remove(node)
    return graph
print(del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4))