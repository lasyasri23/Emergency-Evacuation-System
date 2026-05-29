INF = 10**9
BLOCKED = -1


def dijkstra(graph, V, src):
    dist = [INF] * V
    visited = [False] * V
    parent = [-1] * V

    dist[src] = 0

    for _ in range(V):
        u = min_distance(dist, visited, V)

        if u == -1:
            break

        visited[u] = True

        for v in range(V):
            if graph[u][v] == BLOCKED:
                continue

            if (not visited[v] and
                graph[u][v] != INF and
                dist[u] + graph[u][v] < dist[v]):

                dist[v] = dist[u] + graph[u][v]
                parent[v] = u

    print("\n--- Dijkstra Result ---")

    for i in range(V):
        print(f"\nNode {i} Distance: {dist[i]}")

        if dist[i] != INF:
            print("Path: ", end="")
            print_path(parent, i)
            print()


def print_path(parent, j):
    if j == -1:
        return
    print_path(parent, parent[j])
    print(j, end=" → ")


def min_distance(dist, visited, V):
    min_val = INF
    min_index = -1

    for i in range(V):
        if not visited[i] and dist[i] < min_val:
            min_val = dist[i]
            min_index = i

    return min_index


def floyd_warshall(graph, V):
    dist = [row[:] for row in graph]

    for i in range(V):
        for j in range(V):
            if dist[i][j] == BLOCKED:
                dist[i][j] = INF

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    print("\n--- Floyd Warshall Result ---")

    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print("INF", end=" ")
            else:
                print(dist[i][j], end=" ")
        print()
