from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, node, visited):
        if node not in visited:
            print(node, end="->")
            visited.add(node)
            neighbors = self.graph.get(node, [])
            for i in neighbors:
                self.dfs(i, visited)

    def dfs_traversal(self, start_node):
        visited = set()
        self.dfs(start_node, visited)

    def display(self):
        for node, neighbors in self.graph.items():
            print(f"{node}: {neighbors}")


# Example usage:
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 5)
graph.add_edge(2, 6)
graph.add_edge(3, 4)
graph.add_edge(3, 7)
graph.add_edge(7, 8)
graph.add_edge(4, 8)


graph.display()

start_node = 7
graph.dfs_traversal(start_node)
