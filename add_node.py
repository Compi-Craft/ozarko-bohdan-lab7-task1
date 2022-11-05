"""
Adds node to graph
"""
def add_node(graph: dict, node: int) -> dict:
    """
    (dict, int) -> (dict)
    Add a new node to the graph and return a new graph.
    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    if node not in graph.keys():
        graph.update({node: []})
    return graph
