import sys
from graph import WeightedGraph

test_cases = [
    ([(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)], 4, False),
    ([(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)], 5, False),
    ([(0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11), (2, 3, 7), (2, 5, 4), (2, 8, 2), (3, 4, 9),
      (3, 5, 14), (4, 5, 10), (5, 6, 2), (6, 7, 1), (6, 8, 6), (7, 8, 7)], 9,  False),
]


class Graph(WeightedGraph):

    def BellmanFord(self, src):

        dist = [float("Inf")] * self.V
        self.space += self.V
        dist[src] = 0

        for i in range(self.V - 1):
            self.copies += 1
            for u, v, w in self.graph:
                self.copies += 3
                self.comparisons += 2
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        self.max_loop_depth = max(self.max_loop_depth, 2)

        for u, v, w in self.graph:
            self.copies += 3
            self.comparisons += 2
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return
        self.max_loop_depth = max(self.max_loop_depth, 1)

        self.max_space = self.space
        self.printArr(dist)

    def floydWarshall(self):
        self.convert_graph_form_INF()

        dist = [[item for item in loop_var] for loop_var in self.graph]

        for k in range(self.V):

            for i in range(self.V):

                for j in range(self.V):

                    dist[i][j] = min(dist[i][j],
                                     dist[i][k] + dist[k][j])

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

    def minDistance(self, key, mstSet):

        minm = sys.maxsize
        min_index = None
        self.copies += 2

        for v in range(self.V):
            self.comparisons += 2
            self.copies += 1
            if key[v] < minm and not mstSet[v]:
                minm = key[v]
                min_index = v

        return min_index

    def dijkstra(self, src, directed=False):
        self.convert_graph_form_INF(directed=directed)

        dist = [sys.maxsize] * self.V
        self.space += self.V
        dist[src] = 0
        sptSet = [False] * self.V
        self.space += V

        for cout in range(self.V):
            self.copies += 1
            self.max_loop_depth = max(self.max_loop_depth, 1)
            u = self.minDistance(dist, sptSet)
            self.max_loop_depth = max(self.max_loop_depth, 2)

            sptSet[u] = True

            for v in range(self.V):
                self.copies += 1
                self.comparisons += 3
                self.max_loop_depth = max(self.max_loop_depth, 3)
                if self.graph[u][v] > 0 and (not sptSet[v]) and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.max_space = self.space
        self.printSolution(dist)
