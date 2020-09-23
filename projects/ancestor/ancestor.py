from collections import deque, defaultdict


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
            elif len(current_path) > len(paths[0]) or (
                len(current_path) == len(paths[0]) and current_path[-1] < paths[0][-1]
            ):
                paths = [current_path]

    return paths[0][-1] if len(paths) else -1

    # graph = create_graph(ancestors)
    # stack = deque()
    # stack.append((starting_node, 0))
    # visited = set()
    # earliest_ancestor = (starting_node, 0)

    # while len(stack) > 0:
    #     current = stack.pop()
    #     currentNode, distance = current[0], current[1]
    #     visited.add(current)

    #     if currentNode not in graph:
    #         if distance > earliest_ancestor[1]:
    #             earliest_ancestor = current
    #         elif (
    #             distance == earliest_ancestor[1] and currentNode < earliest_ancestor[0]
    #         ):
    #             earliest_ancestor = current
    #     else:
    #         for ancestor in graph[currentNode]:
    #             if ancestor not in visited:
    #                 stack.append((ancestor, distance + 1))
    # return earliest_ancestor[0] if earliest_ancestor[0] != starting_node else -1


def create_graph(edges):
    graph = defaultdict(set)
    for edge in edges:
        ancestor, child = edge[0], edge[1]
        graph[child].add(ancestor)
    return graph
