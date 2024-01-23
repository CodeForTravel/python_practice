from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start_node):
        visited = set()
        queue = deque([start_node])

        while queue:
            current_node = queue.popleft()
            if current_node not in visited:
                print(current_node, end=" ")
                visited.add(current_node)
                queue.extend(self.graph[current_node])

    def display(self):
        for node, neighbors in self.graph.items():
            print(f"{node}: {neighbors}")


# Example Usage:
graph = Graph()

# Adding edges to the graph
graph.add_edge(1, 2)
graph.add_edge(1, 6)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(6, 5)

graph.display()
# Starting BFS traversal from node 1
print("BFS Traversal starting from node 1:")
graph.bfs(1)
