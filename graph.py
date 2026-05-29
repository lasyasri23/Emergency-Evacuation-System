INF = 10**9
BLOCKED = -1


class Graph:
    def __init__(self, v):
        self.V = v
        self.graph = [[INF for _ in range(v)] for _ in range(v)]

        for i in range(v):
            self.graph[i][i] = 0

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def block_edge(self, u, v):
        self.graph[u][v] = BLOCKED
        self.graph[v][u] = BLOCKED

    def display(self):
        print("\n--- Graph Matrix ---")
        for i in range(self.V):
            for j in range(self.V):
                if self.graph[i][j] == INF:
                    print("INF", end=" ")
                elif self.graph[i][j] == BLOCKED:
                    print("BLK", end=" ")
                else:
                    print(self.graph[i][j], end=" ")
            print()
