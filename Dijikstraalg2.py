import heapq

def dijkstra(graph, start, end):
    queue = []
    heapq.heappush(queue, (0, start))
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    path = []

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    current_node = end
    while previous_nodes[current_node] is not None:
        path.insert(0, current_node)
        current_node = previous_nodes[current_node]
    if path:
        path.insert(0, current_node)
    return distances[end], path

graph = {
    'A': {'B': 4, 'C': 5},
    'B': {'A': 4, 'D': 9, 'C': 11},
    'C': {'A': 5, 'B': 11, 'E': 3},
    'D': {'B': 9, 'E': 7, 'F': 2},
    'E': {'C': 3, 'D': 7, 'F': 6},
    'F': {'D': 2, 'E': 6}
}

start = 'A'
end = 'F'
distance, path = dijkstra(graph, start, end)
print(f"Distance: {distance}")
print(f"Path: {''.join(path)}")
