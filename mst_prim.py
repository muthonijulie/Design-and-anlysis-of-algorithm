
import sys

class MST:
    def __init__(self, vertices):
        self.V = vertices

    # A utility function to find the vertex with minimum key value
    # from the set of vertices not yet included in MST
    def minKey(self, key, mstSet):
        min = sys.maxsize
        min_index = -1

        for v in range(self.V):
            if not mstSet[v] and key[v] < min:
                min = key[v]
                min_index = v

        return min_index

    # A utility function to print the constructed MST stored in parent[]
    def printMST(self, parent, graph):
        print("Edge \tWeight")
        total_weight = 0
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", graph[i][parent[i]])
            total_weight += graph[i][parent[i]]
        print("Total Minimum Weight:", total_weight)

    # Function to construct and print MST for a graph represented
    # using adjacency matrix representation
    def primMST(self, graph):
        # Array to store constructed MST
        parent = [None] * self.V
        # Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.V
        # To represent set of vertices included in MST
        mstSet = [False] * self.V

        # Always include first 1st vertex in MST.
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        parent[0] = -1  # type: ignore # First node is always root of MST

        # The MST will have V vertices
        for count in range(self.V - 1):
            # Pick the minimum key vertex from the set of vertices
            # not yet included in MST
            u = self.minKey(key, mstSet)

            # Add the picked vertex to the MST Set
            mstSet[u] = True

            # Update key value and parent index of the adjacent
            # vertices of the picked vertex.
            for v in range(self.V):
                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if graph[u][v] != 0 and not mstSet[v] and key[v] > graph[u][v]:
                    key[v] = graph[u][v]
                    parent[v] = u # type: ignore

        # Print the constructed MST
        self.printMST(parent, graph)

# Driver's code
if __name__ == "__main__":
    graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]

    mst = MST(5)
    mst.primMST(graph)
