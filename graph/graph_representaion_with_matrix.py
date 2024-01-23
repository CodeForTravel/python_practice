# Adjacency Matrix Representation


class UndirectedUnweightedGraphMatrix:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = [[0] * nodes for _ in range(nodes)]

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def display(self):
        for row in self.graph:
            print(row)


class DirectedUnweightedGraphMatrix:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = [[0] * nodes for _ in range(nodes)]

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        # self.graph[v][u] = 1

    def display(self):
        for row in self.graph:
            print(row)


class UndirectedWeightedGraphMatrix:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = [[0] * nodes for _ in range(nodes)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def display(self):
        for row in self.graph:
            print(row)


# Example usage:
nodes = 5
graph_matrix = UndirectedUnweightedGraphMatrix(nodes)
graph_matrix.add_edge(0, 1)
graph_matrix.add_edge(0, 4)
graph_matrix.add_edge(1, 2)
graph_matrix.add_edge(1, 3)
graph_matrix.add_edge(1, 4)
graph_matrix.add_edge(2, 3)
print("Adjacency Matrix of UndirectedUnweightedGraphMatrix:")
graph_matrix.display()


directed_graph_matrix = DirectedUnweightedGraphMatrix(nodes)
directed_graph_matrix.add_edge(0, 1)
directed_graph_matrix.add_edge(0, 4)
directed_graph_matrix.add_edge(1, 2)
directed_graph_matrix.add_edge(1, 3)
directed_graph_matrix.add_edge(1, 4)
directed_graph_matrix.add_edge(2, 3)
print("Adjacency Matrix of DirectedUnweightedGraphMatrix:")
directed_graph_matrix.display()


weighted_undirected_graph_matrix = UndirectedWeightedGraphMatrix(nodes)
weighted_undirected_graph_matrix.add_edge(0, 1, 2)
weighted_undirected_graph_matrix.add_edge(0, 4, 3)
weighted_undirected_graph_matrix.add_edge(1, 2, 1)
weighted_undirected_graph_matrix.add_edge(1, 3, 4)
weighted_undirected_graph_matrix.add_edge(1, 4, 2)
weighted_undirected_graph_matrix.add_edge(2, 3, 3)
print("Adjacency Matrix of UndirectedWeightedGraphMatrix:")
weighted_undirected_graph_matrix.display()
