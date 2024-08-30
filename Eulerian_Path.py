def find_eulerian_path(graph):
    def find_path(v):
        while graph[v]:
            u = graph[v].pop()
            find_path(u)
        path.append(v)

    graph = {v: set(neighbors) for v, neighbors in graph.items()}
    path = []
    start_vertex = next((v for v in graph if len(graph[v]) % 2 == 1), None)

    if start_vertex is None:
        start_vertex = next(iter(graph))

    find_path(start_vertex)
    return path[::-1]

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

print(find_eulerian_path(graph))
