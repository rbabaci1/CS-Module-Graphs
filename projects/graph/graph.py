"""
Simple graph implementation
"""
from collections import deque


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def __str__(self):
        return str(self.vertices)

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            if v2 not in self.vertices[v1]:
                self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]

    def get_shortest_path(self, paths, destination_vertex):
        matches = []
        for path in paths:
            if path[-1] == destination_vertex:
                matches.append(path)
        return min(matches, key=lambda p: len(p)) if matches else None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = deque()
        queue.append(starting_vertex)
        visited = set()

        while len(queue):
            current_vertex = queue.popleft()
            if current_vertex not in visited:
                visited.add(current_vertex)
                print(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    queue.append(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = deque()
        stack.append(starting_vertex)
        visited = set()

        while len(stack):
            current_vertex = stack.pop()
            if current_vertex not in visited:
                visited.add(current_vertex)
                print(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    stack.append(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()

        def r_helper(self, starting_vertex):
            if starting_vertex not in visited:
                visited.add(starting_vertex)
                print(starting_vertex)
                for neighbor in self.get_neighbors(starting_vertex):
                    r_helper(self, neighbor)

        r_helper(self, starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = deque()
        visited = set()
        queue.append([starting_vertex])

        while len(queue):
            current_path = queue.popleft()
            current_vertex = current_path[-1]

            if current_vertex == destination_vertex:
                return current_path

            if current_vertex not in visited:
                visited.add(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    new_path = list(current_path)
                    new_path.append(neighbor)
                    queue.append(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = deque()
        visited = set()
        stack.append([starting_vertex])

        while len(stack):
            print("iterative +1")
            current_path = stack.pop()
            current_vertex = current_path[-1]

            if current_vertex == destination_vertex:
                return self.get_shortest_path(list(stack), destination_vertex)

            if current_vertex not in visited:
                visited.add(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    new_path = list(current_path)
                    new_path.append(neighbor)
                    stack.append(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        stack = deque()
        stack.append([starting_vertex])
        visited = set()

        def r_helper(self, destination_vertex):
            print("recursive +1")
            current_path = stack.pop()
            current_vertex = current_path[-1]

            if current_vertex == destination_vertex:
                return self.get_shortest_path(list(stack), destination_vertex)

            if current_vertex not in visited:
                visited.add(current_vertex)
                for n in self.get_neighbors(current_vertex):
                    new_path = list(current_path)
                    new_path.append(n)
                    stack.append(new_path)
                return r_helper(self, destination_vertex)

        return r_helper(self, destination_vertex)


if __name__ == "__main__":
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    """
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    """
    # print(graph.vertices)

    """
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    """
    # graph.bft(1)

    """
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    """
    # graph.dft(1)
    # graph.dft_recursive(1)

    """
    Valid BFS path:
        [1, 2, 4, 6]
    """
    # print(graph.bfs(1, 6))

    """
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    """
    print(graph.dfs(1, 7))
    print(graph.dfs_recursive(1, 6))
