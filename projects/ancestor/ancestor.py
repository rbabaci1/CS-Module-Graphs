from collections import deque


def earliest_ancestor(ancestors, starting_node):
    stack = deque()
    stack.append([starting_node])
    graph = create_graph(ancestors)
    paths = []

    while len(stack):
        current_path = stack.pop()
        current_vertex = current_path[-1]

        if current_vertex in graph:
            for neighbor in graph[current_vertex]:
                new_path = list(current_path)
                new_path.append(neighbor)
                stack.append(new_path)
        elif current_vertex != starting_node:
            paths.append(current_path)

    return get_longest(paths) if len(paths) else -1


def get_longest(paths):
    result = paths[-1][-1]
    for path in paths:
        if len(path) == len(paths[-1]):
            if result > path[-1]:
                result = path[-1]
    return result


def create_graph(ancestors):
    graph = {}
    for pair in ancestors:
        if pair[1] in graph:
            graph[pair[1]].add(pair[0])
        else:
            graph[pair[1]] = set()
            graph[pair[1]].add(pair[0])
    return graph

