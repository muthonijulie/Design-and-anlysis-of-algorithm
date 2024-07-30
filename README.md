Initialization:

The MST class is initialized with the number of vertices in the graph.
minKey Function:

This function finds the vertex with the minimum key value that hasn't been included in the MST yet. It iterates through all vertices, checking if they are not included in the MST and have a smaller key value than the current minimum.
printMST Function:

This function prints the edges of the MST and their respective weights. It uses the parent array, which stores the MST, to determine the edges.
primMST Function:

This function constructs the MST using Prim's algorithm:
It initializes the parent array to store the MST, the key array to store the minimum edge weights, and the mstSet array to track included vertices.
It sets the key value of the first vertex to 0 to start from it.
It iterates V-1 times (since the MST will have V vertices).
In each iteration, it picks the vertex with the minimum key value that hasn't been included in the MST yet, and updates the key values and parent indices of its adjacent vertices.
After constructing the MST, it prints the result using the printMST function.Total Minimum Weight Calculation:
Inside the printMST function, a variable total_weight is introduced to accumulate the weights of the edges in the MST.
As the edges are printed, their weights are added to total_weight.
Finally, the total weight of the MST is printed.