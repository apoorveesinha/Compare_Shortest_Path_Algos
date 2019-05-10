import mst
import traversal
import shortest_path

list_people = []

TRAVERSAL = 1
MST = 2
SHORTEST_PATH = 3


class Person:

    def __init__(self, uid, name):
        self.name = name
        self.id = uid
        self.friends = []

    def add_friend(self, id_person):
        if id_person not in self.friends:
            self.friends.append(id_person)

    def remove_friend(self, id_person):
        if id_person in self.friends:
            self.friends.remove(id_person)


def test_heading(test_number):
    print('------------------------------------------------')
    print('------------------ Test {test_num} ---------------------'.format(test_num=test_number))
    print('------------------------------------------------\n')


def get_test_case(test_cases, n):
    return test_cases[n - 1]


def add_edges(g, edges, weighted=False, directed=False):
    for edge in edges:
        person1 = list_people[edge[0]]
        person1.add_friend(edge[1])

        if not directed:
            person2 = list_people[edge[1]]
            person2.add_friend(edge[0])

        if not weighted:
            g.addEdge(edge[0], edge[1])
        else:
            g.addEdge(edge[0], edge[1], edge[2])


if __name__ == '__main__':

    for i in range(10):
        person = Person(i, "Name" + str((i + 1)))
        list_people.append(person)

    print('Choices:')
    print('1. Traversal')
    print('2. MST')
    print('3. Shortest Path')
    choice = int(input())

    if choice == TRAVERSAL:

        test_cases = traversal.test_cases
        print(test_cases)
        for test_num, test_case_pair in enumerate(test_cases):
            test_heading(test_num + 1)

            test_case = test_case_pair[0]
            source = test_case_pair[1]

            g1 = traversal.Graph(list_people)
            g2 = traversal.Graph(list_people)

            add_edges(g1, test_case)
            add_edges(g2, test_case)

            g1.BFS(source)
            print(g1.print_statistics("BFS"))

            g2.DFS(source)
            print(g2.print_statistics("DFS"))

    elif choice == MST:

        test_cases = mst.test_cases
        print(test_cases)
        for test_num, test_case_pair in enumerate(test_cases):
            test_heading(test_num + 1)

            test_case = test_case_pair[0]
            vertices = test_case_pair[1]

            g1 = mst.Graph(list_people, vertices)
            g2 = mst.Graph(list_people, vertices)

            add_edges(g1, test_case, weighted=True)
            add_edges(g2, test_case, weighted=True)

            g1.primMST()
            g2.KruskalMST()

            print(g1.print_statistics("Prim's"))
            print(g2.print_statistics("Kruskal"))

    elif choice == SHORTEST_PATH:

        test_cases = shortest_path.test_cases
        print(test_cases)
        for test_num, test_case_triplet in enumerate(test_cases):
            test_heading(test_num + 1)

            test_case = test_case_triplet[0]
            vertices = test_case_triplet[1]
            directed = test_case_triplet[2]

            g1 = shortest_path.Graph(list_people, vertices)
            g2 = shortest_path.Graph(list_people, vertices)

            add_edges(g1, test_case, weighted=True, directed=directed)
            add_edges(g2, test_case, weighted=True, directed=directed)

            g1.BellmanFord(0)
            g2.dijkstra(0, directed=directed)

            print(g1.print_statistics("Bellmon Ford"))
            print(g2.print_statistics("Dijkstra"))
