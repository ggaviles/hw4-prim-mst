import numpy as np
import heapq as hq
from typing import Union

class Graph:

    def __init__(self, adjacency_mat: Union[np.ndarray, str]):
        """
    
        Unlike the BFS assignment, this Graph class takes an adjacency matrix as input. `adjacency_mat` 
        can either be a 2D numpy array of floats or a path to a CSV file containing a 2D numpy array of floats.

        In this project, we will assume `adjacency_mat` corresponds to the adjacency matrix of an undirected graph.
    
        """
        if type(adjacency_mat) == str:
            self.adj_mat = self._load_adjacency_matrix_from_csv(adjacency_mat)
        elif type(adjacency_mat) == np.ndarray:
            self.adj_mat = adjacency_mat
        else: 
            raise TypeError('Input must be a valid path or an adjacency matrix')
        self.mst = None

    def _load_adjacency_matrix_from_csv(self, path: str) -> np.ndarray:
        with open(path) as f:
            return np.loadtxt(f, delimiter=',')

    def construct_mst(self):
        """
    
        TODO: Given `self.adj_mat`, the adjacency matrix of a connected undirected graph, implement Prim's 
        algorithm to construct an adjacency matrix encoding the minimum spanning tree of `self.adj_mat`. 
            
        `self.adj_mat` is a 2D numpy array of floats. Note that because we assume our input graph is
        undirected, `self.adj_mat` is symmetric. Row i and column j represents the edge weight between
        vertex i and vertex j. An edge weight of zero indicates that no edge exists. 
        
        This function does not return anything. Instead, store the adjacency matrix representation
        of the minimum spanning tree of `self.adj_mat` in `self.mst`. We highly encourage the
        use of priority queues in your implementation. Refer to the heapq module, particularly the 
        `heapify`, `heappop`, and `heappush` functions.

        """

        """self.mst = [] # Initialize mst

        visited = set()  # Initialize a set to keep track of visited nodes

        outgoing_edges = []  # Initialize outgoing_edges as a priority queue
        hq.heapify(outgoing_edges)

        self.mst.append(self.adj_mat[0])
        


        while v not in visited:
            # Pop lowest weight edge from priority queue
            hq.heappop(outgoing_edges)

            if next_v not in visited:
                hq.heappush(self.mst, next_v)  # Add edge to mst
                visited.add(next_v)"""

        # Initialize mst
        self.mst = []

        # Generate a random starting index in order to randomly choose a node from which to build the mst
        random_starting_index = np.random.randint(0, len(self.adj_mat))

        visited = set()  # Initialize set of visited nodes
        visited.add(random_starting_index)  # Add starting nodes

        # Starting node's smallest edge
        next_edge = min([x for x in self.adj_mat[random_starting_index] if x > 0])

        # Add edge to mst
        self.mst.append(next_edge)

        # Next node in mst (finds index for which distance is least)
        next_node, = np.where(self.adj_mat[random_starting_index] == next_edge)

        # Add node to visited set
        visited.add(next_node)


        for i,j in enumerate(self.adj_mat):



        while len(visited) != len(self.adj_mat):








