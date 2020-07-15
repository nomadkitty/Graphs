class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


def earliest_ancestor(ancestors, starting_node):
    graph = {}
    queue = Queue()
    visited = set()
    queue.enqueue([starting_node])
    longest_path_len = 1
    earliest_ancestor = -1
# loop through the given ancestors list
# create my graph dict {child: {parents}}
    for pairs in ancestors:
        graph[pairs[1]] = set()
    for pairs in ancestors:
        graph[pairs[1]].add(pairs[0])
    # print(graph)

# if the starting node is a not a key of graph, means no parent, return -1
    if starting_node not in graph:
        return -1

# while the queue is not empty
    while queue.size() > 0:
        current_path = queue.dequeue()
        current_node = current_path[-1]
    # if it's not in visited, mark as visited
    # get the neighbors
    # loop through neighbors,
    # construct new path by adding each neighbor to the end if neighbor is not none
    # last node is current node,
    # check if the length of current path is bigger than the longest path,
    # or (equal and current node is smaller than earliest ancestor)
    # assign current node to earliest ancestor
        if current_node not in visited:
            visited.add(current_node)
            neighbors = graph.get(current_node)
            if neighbors is not None:
                for neighbor in neighbors:
                    new_path = current_path + [neighbor]
                    queue.enqueue(new_path)
            # at the end of the path when there's no neighbors
            else:
                if len(current_path) > longest_path_len or (len(current_path) == longest_path_len and current_node < earliest_ancestor):
                    longest_path_len = len(current_path)
                    earliest_ancestor = current_node
    return earliest_ancestor


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
             (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(ancestors, 6)

# Brianna's recursion solution
# def earliest_ancestor(ancestors, starting_node):
#     for parent, child in ancestors:
#         if child is starting_node:
#             earliest_parent = earliest_ancestor(ancestors, parent)
#             if earliest_parent is not -1:
#                 return earliest_parent
#             return parent
#     return -1
