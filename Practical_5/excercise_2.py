from collections import deque, defaultdict
import heapq

class Graph:
    def __init__(self, weighted=False):
        self.graph = defaultdict(list)
        self.weighted = weighted

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2, weight=1):
        if self.weighted:
            self.graph[vertex1].append((vertex2, weight))
            self.graph[vertex2].append((vertex1, weight))  # For undirected weighted graph
        else:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def print_graph(self):
        for vertex in self.graph:
            if self.weighted:
                edges = ', '.join(f"{nbr}({w})" for nbr, w in self.graph[vertex])
            else:
                edges = ' '.join(map(str, self.graph[vertex]))
            print(f"{vertex}: {edges}")

    def shortest_path_bfs(self, start, end):
        queue = deque([(start, [start])])
        visited = set([start])
        while queue:
            current, path = queue.popleft()
            if current == end:
                return path
            for neighbor in (nbr for nbr in self.graph[current] if not self.weighted or isinstance(nbr, int)):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None

    def has_cycle(self):
        visited = set()
        def dfs(v, parent):
            visited.add(v)
            for neighbor in (nbr for nbr in self.graph[v] if not self.weighted or isinstance(nbr, int)):
                if neighbor not in visited:
                    if dfs(neighbor, v):
                        return True
                elif neighbor != parent:
                    return True
            return False
        for vertex in self.graph:
            if vertex not in visited:
                if dfs(vertex, None):
                    return True
        return False

    def dijkstra(self, start, end):
        if not self.weighted:
            return None
        heap = [(0, start, [start])]
        visited = set()
        while heap:
            cost, vertex, path = heapq.heappop(heap)
            if vertex == end:
                return (cost, path)
            if vertex in visited:
                continue
            visited.add(vertex)
            for neighbor, weight in self.graph[vertex]:
                if neighbor not in visited:
                    heapq.heappush(heap, (cost + weight, neighbor, path + [neighbor]))
        return None

    def is_bipartite(self):
        color = {}
        for vertex in self.graph:
            if vertex not in color:
                queue = deque([vertex])
                color[vertex] = 0
                while queue:
                    v = queue.popleft()
                    for neighbor in (nbr for nbr in self.graph[v] if not self.weighted or isinstance(nbr, int)):
                        if neighbor not in color:
                            color[neighbor] = 1 - color[v]
                            queue.append(neighbor)
                        elif color[neighbor] == color[v]:
                            return False
        return True

# Test code for unweighted graph
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_graph()

print("\nShortest path (BFS) from 0 to 3:", g.shortest_path_bfs(0, 3))
print("Has cycle?", g.has_cycle())
print("Is bipartite?", g.is_bipartite())

# Test code for weighted graph
gw = Graph(weighted=True)
gw.add_edge(0, 1, 4)
gw.add_edge(0, 2, 1)
gw.add_edge(2, 1, 2)
gw.add_edge(1, 3, 1)
gw.add_edge(2, 3, 5)
gw.print_graph()

print("\nDijkstra's shortest path from 0 to 3:", gw.dijkstra(0, 3))
