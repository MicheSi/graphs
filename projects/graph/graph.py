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
        self.vertices[vertex_id] = set() # assigns edges of vertex to a Set

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # if both vertices are in the graph
        if v1 in self.vertices and v2 in self.vertices:
            # add v2 as a neighbor to v1
            self.vertices[v1].add(v2)
        # v1 and v2 do not exist
        else:
            # give an error message
            raise IndexError('Vertex does not exist!')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # returns the neighbors of the specified vertex
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue
        q = Queue()
        # enqueue the starting vertex id
        q.enqueue(starting_vertex)
        # create a set() to store visited verts
        visited = set()
        # while queue is not empty
        while q.size() > 0:
            # dequeue the 1st vert
            vert = q.dequeue()
            # if vert has not been visited
            if vert not in visited:
                # visit it and print
                print(vert)
                # mark it as visited
                visited.add(vert)
            # add neighbors to back of queue
                for next_vert in self.get_neighbors(vert):
                    q.enqueue(next_vert)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create empty stack
        s = Stack()
        # add starting vertex to stack
        s.push(starting_vertex)
		# Create a Set to store visited vertices
        visited = set()
		# While the stack is not empty...
        while s.size() > 0:
			# Pop the first vert
            vert = s.pop()
			# If that vertex has not been visited...
            if vert not in visited:
                # visit and print
                print(vert)
				# Mark it as visited...
                visited.add(vert)
				# add neighbors to stack
                for next_vert in self.get_neighbors(vert):
                  s.push(next_vert)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # base case
        if visited is None:
            # create set to store visited verts
            visited = set()
        # create path from get_neighbors method
        path = self.get_neighbors(starting_vertex)
        # add starting vertex to visited
        visited.add(starting_vertex)
        # print starting vertex
        print(starting_vertex)
        # loop through next verts
        for next_vert in path - visited:
            self.dft_recursive(next_vert, visited)
        return visited


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
		# Create a Set to store visited vertices
        visited = set()
		# While the queue is not empty...
        while q.size() > 0:
			# Dequeue the first PATH
            path = q.dequeue()
			# Grab the last vertex from the PATH
            vert = path[-1]
			# If that vertex has not been visited...
            if vert not in visited:
				# CHECK IF IT'S THE TARGET
                if vert == destination_vertex:
				  # IF SO, RETURN PATH
                    return path
				    # Mark it as visited...
                    visited.add(vert)
				# Then add A PATH TO its neighbors to the back of the queue
                for neighbors in self.get_neighbors(vert):
				    # COPY THE PATH
                    new_path = list(path)
				    # APPEND THE NEIGHOR TO THE BACK
                    new_path.append(neighbors)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # initialize empty list
        path = []
        # create empty stack
        s = Stack()
        # add starting vertex to stack
        s.push(starting_vertex)
        # create set to store visited verts
        visited = set()
        # while stack not empty
        while s.size() > 0:
            # pop last vert
            vert = s.pop()
            # if vert has not been visited
            if vert not in visited:
                # visit and print
                # print(vert)
                # mark as visited
                visited.add(vert)
                # add to path list
                path.append(vert)
                # if vert is target
                if vert == destination_vertex:
                    # return the path
                    return path
                # add neighbors to top of stack
                for neighbors in self.get_neighbors(vert):
                    s.push(neighbors)


    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # base case
        if visited is None:
            visited = set()

        if path is None:
            path = []

        # track visited verts
        visited.add(starting_vertex)
        # make copy of the path
        path = path + [starting_vertex]
        # if starting vert is destination vert
        if starting_vertex == destination_vertex:
            # path is starting vert
            return path
        # loop through neighbors of vert
        for neighbor in self.vertices[starting_vertex]:
            # if neighbor vert has not been visited
            if neighbor not in visited:
                # recurse - add it to the new path
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                if new_path:
                    return new_path



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
