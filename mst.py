import sys
from graph import WeightedGraph


test_cases = [
    ([(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)], 4),
    ([(0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)], 5),
]


class Graph(WeightedGraph):

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def minKey(self, key, mstSet):

        minm = sys.maxsize
        min_index = None
        self.copies += 2

        for v in range(self.V):
            self.copies += 1

            self.comparisons += 2
            if key[v] < minm and not mstSet[v]:

                minm = key[v]
                min_index = v

        return min_index

    def primMST(self):
        self.convert_graph_form()
        self.space += len(self.graph) * len(self.graph[0])

        key = [sys.maxsize] * self.V
        self.space += self.V

        parent = [None] * self.V
        self.space += self.V

        key[0] = 0
        mstSet = [False] * self.V
        self.space += self.V

        parent[0] = -1

        for cout in range(self.V):

            self.max_loop_depth = max(self.max_loop_depth, 1)

            u = self.minKey(key, mstSet)
            self.max_loop_depth = max(self.max_loop_depth, 2)

            mstSet[u] = True

            for v in range(self.V):
                self.copies += 1

                self.max_loop_depth = max(self.max_loop_depth, 3)

                self.comparisons += 3
                if 0 < self.graph[u][v] < key[v] and not mstSet[v]:

                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.max_space = self.space
        self.printMST(parent)

    def find(self, parent, i):
        self.comparisons += 1
        if parent[i] == i:
            return i
        self.recursions += 1
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        self.comparisons += 1
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot

        elif rank[xroot] > rank[yroot]:
            self.comparisons += 1
            parent[yroot] = xroot

        else:
            self.comparisons += 1
            parent[yroot] = xroot
            rank[xroot] += 1

    def KruskalMST(self):

        self.space += len(self.graph) * len(self.graph[0])
        result = []

        i = 0
        e = 0
        self.copies += 1

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            self.copies += 1

            self.space += 2
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            self.comparisons += 1

            self.max_loop_depth = max(self.max_loop_depth, 1)

            u, v, w = self.graph[i]
            self.copies += 3

            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            self.copies += 2

            if x != y:
                self.comparisons += 1

                e = e + 1

                result.append([u, v, w])

                self.space += 3
                self.union(parent, rank, x, y)

        self.max_space = self.space

        print("Following are the edges in the constructed MST")
        for u, v, weight in result:
            print("%d -- %d == %d" % (u, v, weight))
