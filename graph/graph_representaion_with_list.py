# Adjacency List Representation


from collections import defaultdict


class UndirectedUnweightedGraphList:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def display(self):
        for node, neighbors in self.graph.items():
            print(f"{node}: {neighbors}")


class DirectedUnweightedGraphList:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def display(self):
        for node, neighbors in self.graph.items():
            print(f"{node}: {neighbors}")


class UndirectedWeightedGraphList:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def display(self):
        for node, neighbors in self.graph.items():
            print(f"{node}: {neighbors}")


# Example usage:
undirected_graph_list = UndirectedUnweightedGraphList()
undirected_graph_list.add_edge(0, 1)
undirected_graph_list.add_edge(0, 4)
undirected_graph_list.add_edge(1, 2)
undirected_graph_list.add_edge(1, 3)
undirected_graph_list.add_edge(1, 4)
undirected_graph_list.add_edge(2, 3)
print("Adjacency List of UndirectedUnweightedGraphList:")
undirected_graph_list.display()


directed_graph_list = DirectedUnweightedGraphList()
directed_graph_list.add_edge(0, 1)
directed_graph_list.add_edge(0, 4)
directed_graph_list.add_edge(1, 2)
directed_graph_list.add_edge(1, 3)
directed_graph_list.add_edge(1, 4)
directed_graph_list.add_edge(2, 3)
print("Adjacency List of UndirectedUnweightedGraphList:")
directed_graph_list.display()


weighted_directed_graph_list = UndirectedWeightedGraphList()
weighted_directed_graph_list.add_edge(0, 1, 2)
weighted_directed_graph_list.add_edge(0, 4, 3)
weighted_directed_graph_list.add_edge(1, 2, 1)
weighted_directed_graph_list.add_edge(1, 3, 4)
weighted_directed_graph_list.add_edge(1, 4, 2)
weighted_directed_graph_list.add_edge(2, 3, 3)
print("Adjacency List of UndirectedWeightedGraphList:")
weighted_directed_graph_list.display()
