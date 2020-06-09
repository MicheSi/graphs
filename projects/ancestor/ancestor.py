# data is list of (parent, child) pairs
# returns earliest ancestor
# if more than one at "earliest", return lowest numeric ID
# if input has no parents, return -1

# create path of nodes (to get back to parent)
# keep track of neighbors (to keep track of children)
from util import Queue

def get_neighbors(arr, node):
    # create empty list for neighbors
    neighbors = []

    # data = list(node)

    for n in range(len(arr)):
        if arr[n][1] == node:
            neighbors.append(arr[n][0])

    return neighbors

def earliest_ancestor(ancestors, starting_node):
    