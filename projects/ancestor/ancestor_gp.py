# Understood

# Plan
# Graphs Problem Solving
# Translate the problem
#### Nodes: people
# Edges: when a child has a parent

# build our graph, or just define get_neighbors

# Choose algorithm
# Either BFS or DFS
# DFS
# How would we know if DFS happened to be faster?

# import deque from collections

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex):
        return self.vertices[vertex]

# Build a path like we did in search
# But we don't know when we stop until we've seen everyone


def build_graph(ancestors):
    graph = Graph()
    for parent, child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)
    return graph


def earliest_ancestor(ancestors, starting_node):
    graph = build_graph(ancestors)

    s = Stack()
    visited = set()
    s.push([starting_node])

    longest_path = []
    earliest_ancestor = -1

    while s.size() > 0:
        path = s.pop()
        current_node = path[-1]

        # if path is longer, or path is equal but the id is smaller
        if (len(path) > len(longest_path)) or (len(path) == len(longest_path) and current_node < earliest_ancestor):
            longest_path = path
            earliest_ancestor = longest_path[-1]

        if current_node not in visited:
            visited.add(current_node)
            parents = graph.get_neighbors(current_node)

            for parent in parents:
                new_path = path + [parent]
                s.push(new_path)
    return earliest_ancestor


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
             (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(ancestors, 2))

# this doesn't pass test, need to check edge cases
