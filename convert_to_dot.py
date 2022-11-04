"""
Converts dict to dot format
and writes it in file
"""
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
