from collections import deque


def earliest_ancestor(ancestors, starting_node):
    graph, stack, paths = create_graph(ancestors), deque(), []
    stack.append([starting_node])

    while len(stack):
        current_path = stack.pop()
        current_vertex = current_path[-1]

        if current_vertex in graph:
            for neighbor in graph[current_vertex]:
                new_path = list(current_path)
                new_path.append(neighbor)
                stack.append(new_path)
        elif current_vertex != starting_node:
            if not len(paths):
                paths.append(current_path)
            elif len(current_path) > len(paths[0]) or current_path[-1] < paths[0][-1]:
                paths = [current_path]

    return paths[0][-1] if len(paths) else -1


def create_graph(ancestors):
    graph = {}
    for pair in ancestors:
        edge, vertex = pair[0], pair[1]
        if vertex not in graph:
            graph[vertex] = set()
        graph[vertex].add(edge)
    return graph
