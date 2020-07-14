"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # use Queue to enqueue starting vertex
        # track visited vertices with a set
        # while queue is not empty
        # current vertex is what dequeue from the queue
        # if the current vertex is not in the visited
        # add to the visited and print it out
        # get neighbors of this current vertex
        # loop through neighbors, enqueue each neighbor
        queue = Queue()
        visited = set()
        queue.enqueue(starting_vertex)
        while queue.size() > 0:
            current_vertex = queue.dequeue()
            if current_vertex not in visited:
                visited.add(current_vertex)
                print(current_vertex)
                neighbors = self.get_neighbors(current_vertex)
                for neighbor in neighbors:
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # same logic above but using stack instead
        stack = Stack()
        visited = set()
        stack.push(starting_vertex)
        while stack.size() > 0:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                visited.add(current_vertex)
                print(current_vertex)
                neighbors = self.get_neighbors(current_vertex)
                for neighbor in neighbors:
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # recursion: everytime set each neighbor as the starting vertex
        # also brings in the visited set
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
            neighbors = self.get_neighbors(starting_vertex)
            for neighbor in neighbors:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # use a Queue and enqueue the 1st path with starting vertex as the only item in the list
        # track visited vertices with set
        # track current path and shortest path
        # while Queue is not empty
        # dequeue the current path
        # grab last vertex from the current path list
        # if the last vertex is the destination vertex, path found
        # else: if last vertex is not in visited path list
        # add to visited
        # get neighbors of the last vertex
        # construct the new path by adding each neighbor to the path and enqueue the new path
        queue = Queue()
        visited = set()
        queue.enqueue([starting_vertex])
        while queue.size() > 0:
            current_path = queue.dequeue()
            last_vertex = current_path[-1]
            if last_vertex == destination_vertex:
                return current_path
            if last_vertex not in visited:
                visited.add(last_vertex)
                for neighbor in self.get_neighbors(last_vertex):
                    new_path = current_path + [neighbor]
                    queue.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # similar logic but using a stack
        stack = Stack()
        visited = set()
        stack.push([starting_vertex])
        while stack.size() > 0:
            current_path = stack.pop()
            last_vertex = current_path[-1]
            if last_vertex == destination_vertex:
                return current_path
            if last_vertex not in visited:
                visited.add(last_vertex)
                for neighbor in self.get_neighbors(last_vertex):
                    new_path = current_path + [neighbor]
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, path=[], visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # mark our node as visited
        visited.add(starting_vertex)

        # check if it's our target node, if so return
        if starting_vertex == destination_vertex:
            return path

        if len(path) == 0:
            path.append(starting_vertex)
        # iterate over neighbores
        neighbors = self.get_neighbors(starting_vertex)
        # check if visited
        for neighbor in neighbors:
            # if not, recurse with a path
            if neighbor not in visited:
                # if this recursion return a path,
                new_path = path + [neighbor]
                result = self.dfs_recursive(
                    neighbor, destination_vertex, new_path, visited)
        # if recoursion returns a path,
                if result is not None:
                    # return from here
                    return result


if __name__ == '__main__':
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

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
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
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
