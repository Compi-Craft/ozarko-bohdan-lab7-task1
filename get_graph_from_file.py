"""
Gets files from file
"""
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
