from graph import Graph
from algorithms import dijkstra, floyd_warshall


def main():
    print("=== Emergency Evacuation System ===")

    V = int(input("Enter number of nodes: "))
    g = Graph(V)

    while True:
        print("\n===== MENU =====")
        print("1. Add Route")
        print("2. Block Route")
        print("3. Display Graph")
        print("4. Dijkstra")
        print("5. Floyd Warshall")
        print("6. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            u = int(input("From node: "))
            v = int(input("To node: "))
            w = int(input("Weight: "))
            g.add_edge(u, v, w)

        elif choice == 2:
            u = int(input("From node: "))
            v = int(input("To node: "))
            g.block_edge(u, v)

        elif choice == 3:
            g.display()

        elif choice == 4:
            src = int(input("Enter source node: "))
            dijkstra(g.graph, g.V, src)

        elif choice == 5:
            floyd_warshall(g.graph, g.V)

        elif choice == 6:
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
