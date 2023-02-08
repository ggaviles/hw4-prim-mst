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
        self.mst = []

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

        # Initialize self.mst as empty list
        self.mst = []

        # Initialize visited as an empty set
        visited = set()

        # Choose a random starting node within the domain of the adjacency matrix size
        random_starting_node = np.random.randint(0, len(self.adj_mat))
        self.adj_mat[self.adj_mat == 0] = np.inf  # Replace all zeros with infinity
        heap = [_ for _ in self.adj_mat[random_starting_node]]  # Return edges for random node
        hq.heapify(heap)  # Heapify heap

        visited.add(random_starting_node)  # Add first node to visited

        # Set the starting node to be the current node
        curr_node = random_starting_node

        while heap and len(visited) != len(self.adj_mat):
            shortest_edge = hq.heappop(heap)  # Pop shortest_edge
            curr_node = self.adj_mat[curr_node].tolist().index(shortest_edge)  # Assign index to next node
            if curr_node not in visited:  # Check if neighboring node is already in visited
                visited.add(curr_node)
                self.mst.append(shortest_edge)  # Add edge to mst
                #neighbor_edges = [_ for _ in self.adj_mat[curr_node]]
                for i in self.adj_mat[curr_node]:
                    hq.heappush(heap, i)

        self.mst = [int(x) for x in self.mst]
        self.mst = np.array(self.mst)






