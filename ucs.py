from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1][vertex2] = weight
            self.adjacency_list[vertex2][vertex1] = weight
        else:
            print("One or both vertices do not exist.")

    def display(self):
        for vertex in self.adjacency_list:
            print(vertex, "-->", self.adjacency_list[vertex])

    def ucs(self, start, goal):
        visited = set()
        pq = PriorityQueue()
        pq.put((0, start))
        while not pq.empty():
            cost, vertex = pq.get()
            if vertex == goal:
                return cost
            if vertex not in visited:
                visited.add(vertex)
                for neighbor, weight in self.adjacency_list[vertex].items():
                    if neighbor not in visited:
                        pq.put((cost + weight, neighbor))
        return float("inf")


g = Graph()

text = """
Oradea zerind 71
Oradea Sibiu 151
zerind Arad 75
Arad Timisoara 118
Arad Sibiu 140
Timisoara Lugoj 111
Lugoj Mehadia 70
Mehadia Drobeta 75
Drobeta Craiova 120
Craiova Pitesti 138
Craiova Rimnicu_Vilcea 80
Pitesti Rimnicu_Vilcea 97
Pitesti Bucharest 101
Bucharest Giurgiu 90
Bucharest Urziceni 85
Bucharest Fagaras 211
Urziceni Vaslui 142
Urziceni Hirsova 98
Hirsova Eforie 86
Vaslui Iasi 142
Iasi Neamt 87
Fagaras Sibiu 99
Sibiu Rimnicu_Vilcea 80
"""

lines = text.strip().split('\n')
for line in lines:
    parts = line.split()
    vertex1 = parts[0]
    vertex2 = parts[1]
    weight = int(parts[2])
    g.add_vertex(vertex1)
    g.add_vertex(vertex2)
    g.add_edge(vertex1, vertex2, weight)

print("UCS cost from Oradea to Bucharest:", g.ucs('Arad', 'Bucharest'))
