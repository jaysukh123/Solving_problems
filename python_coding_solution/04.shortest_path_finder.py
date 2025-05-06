# Problem:
# You are given a weighted graph where nodes are cities and edges represent distances.
# Find the shortest path from a given start city to a destination city using Dijkstra's Algorithm.
# Print the path and total distance.


# Dijkstra's algorithm to find shortest path in a graph
import heapq  # for using priority queue

# Function to find the shortest path using Dijkstra's Algorithm
def find_shortest_path(graph, start, end):
    # Priority queue stores (distance, current_city, path)
    queue = [(0, start, [start])]
    visited = set()

    while queue:
        current_distance, current_city, path = heapq.heappop(queue)

        if current_city in visited:
            continue

        visited.add(current_city)

        # If we reached the destination
        if current_city == end:
            return path, current_distance

        # Check neighbors
        for neighbor in graph[current_city]:
            if neighbor not in visited:
                distance = current_distance + graph[current_city][neighbor]
                heapq.heappush(queue, (distance, neighbor, path + [neighbor]))

    # If there's no path
    return None, float('inf')

# Graph of cities and distances
cities = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'C': 3, 'D': 9},
    'C': {'A': 10, 'B': 3, 'D': 1},
    'D': {'B': 9, 'C': 1}
}

# Starting and ending cities
start = 'A'
end = 'D'

# Call the function
shortest_path, total_distance = find_shortest_path(cities, start, end)

# Print result
if shortest_path:
    print("Shortest path from", start, "to", end, "is:")
    print(" -> ".join(shortest_path))
    print("Total distance:", total_distance)
else:
    print("Sorry, no path found between", start, "and", end)
