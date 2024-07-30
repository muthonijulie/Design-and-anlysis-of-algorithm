import sys

# Declaring the list of nodes for the graph
# Sample graph (nodes and edges)
nodes = [  
    [0, 0, 1, 0, 1, 0],  # A
    [0, 0, 1, 0, 0, 1],  # B
    [1, 1, 0, 1, 1, 0],  # C
    [0, 0, 1, 0, 0, 1],  # D
    [1, 0, 1, 0, 0, 1],  # E
    [0, 1, 0, 1, 1, 0]   # F
]

edges = [  
    [0, 0, 4, 0, 5, 0],  # A to others
    [0, 0, 11, 0, 0, 7], # B to others
    [4, 11, 0, 9, 3, 0], # C to others
    [0, 0, 9, 0, 0, 2],  # D to others
    [5, 0, 3, 0, 0, 6],  # E to others
    [0, 7, 0, 2, 6, 0]   # F to others
]

# Initialization for Dijkstra's algorithm
visitedAndDistance = [[0, float('inf')] for _ in range(len(nodes))]
startNode = 0  # Starting from node A (index 0)
visitedAndDistance[startNode][1] = 0

# Implementation of Dijkstra's algorithm
while True:
    # Find the unvisited node with the smallest distance
    toVisit = -1
    for i in range(len(nodes)):
        if visitedAndDistance[i][0] == 0 and (toVisit == -1 or visitedAndDistance[i][1] < visitedAndDistance[toVisit][1]):
            toVisit = i
    
    if toVisit == -1:
        break
    
    # Update distances to neighbors
    for neighborIndex in range(len(nodes[toVisit])):
        if nodes[toVisit][neighborIndex] == 1 and visitedAndDistance[neighborIndex][0] == 0:
            newDistance = visitedAndDistance[toVisit][1] + edges[toVisit][neighborIndex]
            if visitedAndDistance[neighborIndex][1] > newDistance:
                visitedAndDistance[neighborIndex][1] = newDistance
    
    # Mark the current node as visited
    visitedAndDistance[toVisit][0] = 1

# The resulting distances from the start node to each other node
print("Node distances from start node:")
for i, (visited, distance) in enumerate(visitedAndDistance):
    print(f"Node {chr(ord('A') + i)}: {distance}")
