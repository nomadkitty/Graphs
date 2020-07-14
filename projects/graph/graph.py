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
        # make a queue
        q = Queue()
        # enqueue our starting node
        q.enqueue(starting_vertex)
        # make a set to track if we've been here before
        visited = set()
        # while our queue isn't empty
        while q.size() > 0:
            # dequeue whatever's at the front of our line, this is our current_node
            current_node = q.dequeue()
        # if we haven't visited this node yet,
            if current_node not in visited:
                # mark as visited
                visited.add(current_node)
                print(current_node)
        # get its neighbors
                neighbors = self.get_neighbors(current_node)
        # for each of the neighbors,
                for neighbor in neighbors:
                    # add to queue
                    q.enqueue(neighbor)
    # ------>
    # q = Queue(1)
    # visited = set(1)

    # current_node = 1
    # neighbor = []

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack
        s = Stack()
        # push on our starting node
        s.push(starting_vertex)
        # make a set to track if we've been here before
        visited = set()
        # while our stack isn't empty
        while s.size() > 0:
            # pop off whatever's on the top, this is current_node
            current_node = s.pop()
        # if we haven't visited this vertex before
            if current_node not in visited:
                # mark as visited
                visited.add(current_node)
                print(current_node)
        # get its neighbors
                neighbors = self.get_neighbors(current_node)
        # for each of the neighbors
                for neighbor in neighbors:
                    # add to our stack
                    s.push(neighbor)

        # s = Stack()
        # visited = set(1, 2, 4,7, 6, 3, 5)
        # current_node = 2
        # neighbors = []

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # if start node is not in the visited:
        if starting_vertex not in visited:
            # add start node to the visited
            visited.add(starting_vertex)
            # print the start node
            print(starting_vertex)
            # get neighbors of the node
            neighbors = self.get_neighbors(starting_vertex)
            # loop through neighbors
            for neighbor in neighbors:
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # make a queue
        q = Queue()
        # push the 1st path to the queue
        q.enqueue([starting_vertex])
        # make a set of visited
        visited = set()
        # make a list of the paths
        paths = []
        # shortest path
        min_path = min_steps = None
        # while our queue isn't empty
        while q.size() > 0:
            # dequeue whatever 1st path on the queue
            path = q.dequeue()
            # find the last node from the path
            last_node = path[-1]
            # check if it's the destination node, path found
            if last_node == destination_vertex:
                # return path
                paths.append(path)
                continue
        # if last node is not is the visited yet
            if last_node not in visited:
                # add the last node to the path
                visited.add(last_node)
        # get neighbors of the last node
                neighbors = self.get_neighbors(last_node)
        # check each neighbor of the last node
                for neighbor in neighbors:
                    # append the neighbor to the path
                    new_path = path + [neighbor]
                    q.enqueue(new_path)
        # find the shortest length path as min_path
        for path in paths:
            steps = len(path)
            if min_steps is None or steps < min_steps:
                min_path = path
                min_steps = steps
        return min_path

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # make a stack
        s = Stack()
        # push 1st path to the stack
        s.push([starting_vertex])
        # make a list of paths
        paths = []
        # make a set of visited
        visited = set()
        # while the stack isn't empty:
        while s.size() > 0:
            # pop off the last path of the stack
            path = s.pop()
            # grab the last node of the path
            last_node = path[-1]
            # check if it's the dest node
            if last_node == destination_vertex:
                # return found fath
                paths.append(path)
                continue
            # if the last node is not in visited
            if last_node not in visited:
                # add last node to visited
                visited.add(last_node)
            # get neighbor of the last node
                neighbors = self.get_neighbors(last_node)
            # loop through neighbor
                for neighbor in neighbors:
                    # construct a new path
                    new_path = path + [neighbor]
            # push the new path up
                    s.push(new_path)
        return paths

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        paths = []
        visited = set()


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
