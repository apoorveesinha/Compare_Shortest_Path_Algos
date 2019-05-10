from collections import defaultdict

INF = 999999999999


class BaseGraph:

    def __init__(self, list_people=None):

        if list_people:
            self.list_people = list_people
        else:
            self.list_people = []

        self.comparisons = 0
        self.copies = 0
        self.time_taken = 0
        self.space = 0
        self.max_space = 0
        self.recursions = 0
        self.max_loop_depth = 0
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.space += 1

    def print_statistics(self, stats_name):
        print('------------------------------------------------')
        print('--------------------- {name} ----------------------'.format(name=stats_name))
        print('------------------------------------------------\n')

        print("Comparisons:", self.comparisons)
        print("Copies (Duplicates Made):", self.copies)
        print("Space At Last:", self.space, "(Visited Array + Variables/Queue Space)")
        print("Maximum Space Taken:", self.max_space)
        print("Recursions/Function Calls Made:", self.recursions)

        print('------------------------------------------------')


class WeightedGraph:

    def __init__(self, list_people=None, vertices=None):

        if list_people:
            self.list_people = list_people
        else:
            self.list_people = []

        if vertices:
            self.V = vertices

        self.comparisons = 0
        self.copies = 0
        self.time_taken = 0
        self.space = 0
        self.max_space = 0
        self.recursions = 0
        self.max_loop_depth = 0
        self.graph = []

    def convert_graph_form(self, directed=False):
        graph_temp = [[0 for _ in range(self.V)] for __ in range(self.V)]
        for i, j, wt in self.graph:
            graph_temp[i][j] = wt
            if not directed:
                graph_temp[j][i] = wt
        self.graph = graph_temp

    def convert_graph_form_INF(self, directed=False):
        graph_temp = [[INF for _ in range(self.V)] for __ in range(self.V)]
        for i, j, wt in self.graph:
            graph_temp[i][j] = wt
            if not directed:
                graph_temp[j][i] = wt
        for i in range(self.V):
            graph_temp[i][i] = 0
        self.graph = graph_temp

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def printArr(self, dist):
        print("Vertex   Distance from Source")
        for i in range(self.V):
            print("%d \t\t %d" % (i, dist[i]))

    def print_statistics(self, stats_name):
        print('------------------------------------------------')
        print('--------------------- {name} ----------------------'.format(name=stats_name))
        print('------------------------------------------------\n')

        print("Comparisons:", self.comparisons)
        print("Copies (Duplicates Made):", self.copies)
        print("Space At Last:", str(self.space) + 'units', "(Visited Array + Variables/Queue Space)")
        print("Maximum Space Taken:", str(self.max_space) + 'units')
        print("Recursions/Function Calls Made:", self.recursions)
        if self.max_loop_depth > 0:
            print("Maximum Loop Depth:", self.max_loop_depth)
        print('------------------------------------------------')
