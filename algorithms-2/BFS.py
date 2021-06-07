class Vertex:
    def __init__(self, val):
        self.Value = val
        self.Hit = False


class SimpleGraph:
    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        self.bfs_queue = []
        self.bfs_path = {}

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

    def breadth_first_search_make_path(self, loop=False):
        start = list(self.bfs_path.keys())[0]
        path = [list(self.bfs_path.keys())[-1]]
        while path[-1] != start:
            path.append(self.bfs_path[path[-1]])
        path.reverse()
        if loop is True:
            path.append(start)
        return [self.vertex[x] for x in path]

    def breadth_first_search(self, VFrom, VTo):
        self.vertex[VFrom].Hit = True

        if self.m_adjacency[VFrom][VTo] == 1:
            self.vertex[VTo].Hit = True
            if VTo not in self.bfs_path:
                self.bfs_path[VTo] = VFrom
                return self.breadth_first_search_make_path(False)
            else:
                return self.breadth_first_search_make_path(True)
        else:
            for vertex, is_edge in enumerate(self.m_adjacency[VFrom]):
                if vertex != VFrom and is_edge == 1 and self.vertex[vertex].Hit is False:
                    if vertex not in self.bfs_queue:
                        self.bfs_queue.append(vertex)
                        self.bfs_path[vertex] = VFrom
            self.bfs_queue.pop(0)

            if len(self.bfs_queue) == 0:
                return []

            return self.breadth_first_search(self.bfs_queue[0], VTo)

    def BreadthFirstSearch(self, VFrom, VTo):
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету

        # cleaning
        self.bfs_queue = []
        self.bfs_path = {}
        for vertex in self.vertex:
            vertex.Hit = False
        self.bfs_queue.append(VFrom)
        self.bfs_path[VFrom] = None
        return self.breadth_first_search(VFrom, VTo)
