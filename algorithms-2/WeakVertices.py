from itertools import  combinations


class Vertex:
    def __init__(self, val):
        self.Value = val


class SimpleGraph:
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        # ваш код добавления новой вершины
        # с значением value
        # в свободное место массива vertex
        new_vertex = Vertex(v)
        try:
            new_index = self.vertex.index(None)
        except ValueError as e:
            return None
        self.vertex[new_index] = new_vertex

    # здесь и далее, параметры v -- индекс вершины
    # в списке  vertex
    def RemoveVertex(self, v):
        # ваш код удаления вершины со всеми её рёбрами
        self.vertex[v] = None
        for row in self.m_adjacency:
            row[v] = 0
        self.m_adjacency[v] = [0] * self.max_vertex

    def IsEdge(self, v1, v2):
        # True если есть ребро между вершинами v1 и v2
        if self.m_adjacency[v1][v2] == 1:
            return True
        return False

    def AddEdge(self, v1, v2):
        # добавление ребра между вершинами v1 и v2
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1, v2):
        # удаление ребра между вершинами v1 и v2
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0

    def WeakVertices(self):
        # возвращает список узлов вне треугольников
        out_of_triangles = []
        for index in range(len(self.vertex)):
            left = enumerate(self.m_adjacency[index][:index])
            right = enumerate(self.m_adjacency[index][index+1:])
            possible_neighbours = [(ind, is_edge) for ind, is_edge in left] + [(ind + index + 1, is_edge) for ind, is_edge in right]
            neighbours = list(filter(lambda v: v[1] == 1, possible_neighbours))
            if len(neighbours) < 2:
                out_of_triangles.append(self.vertex[index])
            else:
                is_out = True
                combo = combinations(neighbours, 2)
                for c in combo:
                    v1, v2 = c
                    if self.IsEdge(v1[0], v2[0]):
                        is_out = False
                        break
                if is_out is True:
                    out_of_triangles.append(self.vertex[index])

        return out_of_triangles
