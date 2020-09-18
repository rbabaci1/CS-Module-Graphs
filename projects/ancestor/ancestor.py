def earliest_ancestor(ancestors, starting_node):
    # 1- U
    # ancestors = [(1,3), (2, 3), (3,6), (5,6), (5,7), (4,5), (4,8), (8,9), (11,8), (10,1)]
    # To find the earliest ancestor, we might have to use a Depth first search strategy
    # Vertice = child
    # Edge = relation between parent and child, (parent)
    # Weights = None

    # 2- P
    # - first create the graph by having all the children as vertices and the parents as edges
    #

    pass


def create_graph(ancestors):
    graph = {}
    for pair in ancestors:
        if pair[1] in graph:
            graph[pair[1]].add(pair[0])
        else:
            graph[pair[1]] = set()
    return graph
