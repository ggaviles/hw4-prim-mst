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

        # Create a version of the adjacency matrix where all zeros are infinity
        adjacency_matrix = self.adj_mat
        adjacency_matrix[adjacency_matrix == 0] = np.inf  # Replace all zeros with infinity

        heap = [_ for _ in adjacency_matrix[random_starting_node]]  # Return edges for random node
        hq.heapify(heap)  # Heapify heap
        print(heap)

        visited.add(random_starting_node)  # Add first node to visited
        print(visited)

        # Set the starting node to be the current node
        prev_node = random_starting_node

        # Initialize mst as empty adjacency matrix
        self.mst = np.zeros((len(self.adj_mat), len(self.adj_mat)))

        while heap and len(visited) != len(adjacency_matrix):
            shortest_edge = hq.heappop(heap)  # Pop shortest_edge
            print(shortest_edge)
            curr_node = adjacency_matrix[prev_node].tolist().index(shortest_edge)  # Assign index to next node
            print(curr_node)
            print(self.mst)
            if curr_node not in visited:  # Check if neighboring node is already in visited
                visited.add(curr_node)
                print(visited)
                self.mst[prev_node][curr_node] = shortest_edge
                self.mst[curr_node][prev_node] = shortest_edge
                #neighbor_edges = [_ for _ in self.adj_mat[curr_node]]
                for i in adjacency_matrix[curr_node]:
                    hq.heappush(heap, i)
                #for i in adjacency_matrix[curr_node]:
                    #hq.heappush(heap, i)
                #prev_node = curr_node
            prev_node = curr_node
            print(heap)


        self.mst = np.array(self.mst).astype(int)
        print(self.mst)





