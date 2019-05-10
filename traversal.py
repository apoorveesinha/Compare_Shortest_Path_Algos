from graph import BaseGraph

test_cases = [
    ([(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)], 2),
    ([(0, 1), (1, 2), (2, 3), (0, 4), (4, 5), (5, 3), (1, 5), (5, 2)], 2),
    # ([(1, 0), (2, 1), (3, 2), (4, 0), (5, 4), (3, 5), (5, 1), (2, 5)], 2),
    ([(1, 0), (2, 0), (2, 1), (0, 2), (3, 2), (3, 3)], 2),
]


class Graph(BaseGraph):

    def BFS(self, s):

        self.space += (len(self.graph))
        visited = [False] * (len(self.graph))

        queue = []

        self.space += 1
        queue.append(s)

        self.max_space = self.space

        visited[s] = True

        while queue:

            self.space -= 1
            s = queue.pop(0)

            print(self.list_people[s].name, end=" ")

            for i in self.graph[s]:
                self.comparisons += 1
                if not visited[i]:
                    self.space += 1
                    self.max_space = max(self.max_space, self.space)

                    queue.append(i)
                    visited[i] = True
        print()

    def DFSUtil(self, v, visited):

        visited[v] = True
        print(self.list_people[v].name, end=" ")

        for i in self.graph[v]:

            self.comparisons += 1

            if not visited[i]:
                self.recursions += 1
                self.DFSUtil(i, visited)

    def DFS(self, v):
        self.space += len(self.graph)
        visited = [False] * (len(self.graph))

        self.max_space = max(self.max_space, self.space)

        self.recursions += 1
        self.DFSUtil(v, visited)

        print()
