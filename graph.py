"""
Allows to do different operations with graphs
"""
from copy import deepcopy
def get_graph_from_file(file_name: str) -> list[list]:
    """
    (str) -> (list)
    Read graph from file and return a list of edges.
    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """
    big_lst = []
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip("\n")
            small_lst = []
            for i in line:
                if i.isnumeric():
                    small_lst.append(int(i))
            big_lst.append(small_lst)
    return big_lst
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
def add_edge(graph: dict, edge: tuple) -> dict:
    """
    (dict, tuple) -> dict
    Add a new edge to the graph and return new graph.
    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
    return graph
def del_edge(graph: dict, edge: tuple) -> dict:
    """
    (dict, tuple) -> (dict)
    Delete an edge from the graph and return a new graph.
    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    graph[edge[0]].remove(edge[1])
    graph[edge[1]].remove(edge[0])
    return graph
def add_node(graph: dict, node: int) -> dict:
    """
    (dict, int) -> (dict)
    Add a new node to the graph and return a new graph.
    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    graph.update({node: []})
    return graph
def del_node(graph: dict, node: int) -> dict:
    """
    (dict, int) -> (dict)
    Delete a node and all incident edges from the graph.
    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    graph.pop(node)
    for i in graph:
        if node in graph[i]:
            graph[i].remove(node)
    return graph
def convert_to_dot(graph: dict) -> None:
    """
    (dict) -> (None)
    Save the graph to a file in a DOT format.
    """
    with open("graph.dot", "w", encoding="utf-8") as file:
        file.write("graph {\n")
        for i in graph:
            for j in graph[i]:
                file.write(f"{i} -- {j}\n")
        file.write("}")
