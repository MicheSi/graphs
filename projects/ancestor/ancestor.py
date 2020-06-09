# data is list of (parent, child) pairs
# returns earliest ancestor
# if more than one at "earliest", return lowest numeric ID
# if input has no parents, return -1

# create path of nodes (to get back to parent)
# keep track of neighbors (to keep track of children)
import sys
sys.path.append('../graph')
from graph import Graph
from util import Queue


# def get_neighbors(arr, node):
#     # create empty list for neighbors
#     neighbors = []

#     # data = list(node)

#     for n in range(len(arr)):
#         if arr[n][1] == node:
#             neighbors.append(arr[n][0])

#     return neighbors

def earliest_ancestor(ancestors, starting_node):
    # create empty Graph
    g = Graph()

    # for each tuple
    for parent, child in ancestors:
        # add verts to graph
        g.add_vertex(parent)
        g.add_vertex(child)
        # make directed by pointed child to parent
        g.add_edge(child, parent)

    # create empty Queue
    q = Queue()
    # add starting node to queue
    q.enqueue([starting_node])

    # if no parents to node, return -1
    if len(g.get_neighbors(starting_node)) == 0:
        return -1
    else:
        # while queue is not empty
        while q.size() > 0:
            # dequeue the 1st path
            path = q.dequeue()
            # grab vert from last index in path
            vert = path[-1]

            # loop through parents
            for parent in g.get_neighbors(vert):
                # copy the path
                new_path = list(path)
                # append parent to back
                new_path.append(parent)
                # add copy of path
                q.enqueue(new_path)
    return vert

