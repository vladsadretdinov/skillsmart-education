class Vertex:
    def __init__(self, val):
        self.Value = val
        self.Hit = False


class SimpleGraph:
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        self.dfs_stack = []

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

    def depth_first_search(self, VFrom, VTo, append=False):
        self.vertex[VFrom].Hit = True
        if append is True:
            self.dfs_stack.append(self.vertex[VFrom])
        is_all_edges_passed = True

        if self.m_adjacency[VFrom][VTo] == 1:
            self.vertex[VTo].Hit = True
            self.dfs_stack.append(self.vertex[VTo])
            return self.dfs_stack
        else:
            for vertex, is_edge in enumerate(self.m_adjacency[VFrom]):
                if vertex != VFrom and is_edge == 1 and self.vertex[vertex].Hit is False:
                    is_all_edges_passed = False
                    return self.depth_first_search(vertex, VTo, True)

        if is_all_edges_passed is True:
            self.dfs_stack.pop()

        if len(self.dfs_stack) == 0:
            return []
        else:
            for ind, vertex in enumerate(self.vertex):
                if vertex.Value == self.dfs_stack[-1].Value:
                    return self.depth_first_search(ind, VTo)


    def DepthFirstSearch(self, VFrom, VTo):
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету

        # cleaning
        self.dfs_stack = []
        for vertex in self.vertex:
            vertex.Hit = False

        return self.depth_first_search(VFrom, VTo, True)
