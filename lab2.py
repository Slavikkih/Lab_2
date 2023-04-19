import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


def tsp(graph, start):
    distances = dijkstra(graph, start)

    farthest_node = max(distances, key=distances.get)

    shortest_path = dijkstra(graph, start=farthest_node)[start]

    nodes = set(graph.keys())
    nodes.remove(start)
    nodes.remove(farthest_node)
    for node in nodes:
        path = dijkstra(graph, start=node)
        length = path[start] + path[farthest_node]
        if length < shortest_path:
            shortest_path = length

    return shortest_path


filename = input("Введіть назву файлу з даними: ")
with open(filename, 'r') as f:
    data = f.readlines()

graph = {}
for i, line in enumerate(data):
    row = [int(x) for x in line.split()]
    graph[i] = {j: row[j] for j in range(len(row)) if row[j] > 0}

shortest_path = tsp(graph, 0)

print("Найкоротший шлях, що проходить через всі точки:", shortest_path)

for node in graph:
    distances = dijkstra(graph, node)
    shortest_distances = [distances[n] for n in sorted(distances) if n != node]
    print(f"Найкоротші відстані від вершини {node} до інших: {shortest_distances}")
