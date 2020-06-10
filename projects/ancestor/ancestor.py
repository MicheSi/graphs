import sys
sys.path.append('../graph')
from graph import Graph
from util import Queue

# data is list of (parent, child) pairs
# returns earliest ancestor
# if more than one at "earliest", return lowest numeric ID
# if input has no parents, return -1

# create path of nodes (to get back to parent)
# keep track of neighbors (to keep track of children)

def earliest_ancestor(ancestors, starting_node):
    # create empty Graph
    g = Graph()

    # for each tuple
    for pair in ancestors:
        # add verts to graph
        g.add_vertex(pair[0]) # parent
        g.add_vertex(pair[1]) # child
    for pair in ancestors:
        # make directed by pointing child to parent
        g.add_edge(pair[1], pair[0])


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

            # loop through parents (neighbors) of vert
            for parent in g.get_neighbors(vert):
                # copy the path
                new_path = list(path)
                # append parent to back of path copy
                new_path.append(parent)
                # add copy of path to end of queue
                q.enqueue(new_path)
        # return vert which should be earliest ancestor (last index in path)
        return vert


    # max_path_len = 1
    # earliest_ancestor = -1

    # while q.size() > 0:
    #     path = q.dequeue()
    #     vert = path[-1]
    #     # if path is longer or equal and value is smaller, or if path is longer
    #     if (len(path) >= max_path_len and vert < earliest_ancestor) or (len(path) > max_path_len):
    #         earliest_ancestor = vert
    #         max_path_len = len(path)
    #     for parent in g.vertices[vert]:
    #         new_path = list(path)
    #         new_path.append(parent)
    #         q.enqueue(new_path)
    # return earliest_ancestor


if __name__ == '__main__':
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors, 3))
    print(earliest_ancestor(test_ancestors, 8))
    print(earliest_ancestor(test_ancestors, 9))
