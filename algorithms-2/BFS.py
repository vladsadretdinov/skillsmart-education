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
        self.bfs_path = []

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
        result = []
        end = self.bfs_path[-1]
        while list(end.values())[0] is not None:
            k = list(end.keys())[0]
            v = list(end.values())[0]
            result.append(k)
            for x in self.bfs_path:
                if list(x.keys())[0] == v:
                    end = x
                    break
        result.append(list(end.keys())[0])
        result.reverse()
        return [self.vertex[x] for x in result]

    def breadth_first_search(self, VFrom, VTo, append=False):
        self.vertex[VFrom].Hit = True
        if append is True:
            self.bfs_queue.append(self.vertex[VFrom])
            self.bfs_path.append({VFrom: None})

        if self.m_adjacency[VFrom][VTo] == 1:
            self.vertex[VTo].Hit = True
            self.bfs_path.append({VTo: VFrom})
            return self.breadth_first_search_make_path(True)
        else:
            if len(self.bfs_queue) == 0:
                return []
            else:
                next_vertex = None
                for vertex, is_edge in enumerate(self.m_adjacency[VFrom]):
                    if vertex != VFrom and is_edge == 1 and self.vertex[vertex].Hit is False and vertex != list(self.bfs_path[-1].keys())[0]: # vertex not in self.bfs_path and
                        self.bfs_queue.append(self.vertex[vertex])
                        self.bfs_path.append({vertex: VFrom})
                        if next_vertex is None:
                            next_vertex = vertex
                self.bfs_queue.pop(0)
                if next_vertex is None:
                    next_vertex = list(self.bfs_path[-1].keys())[0]
                return self.breadth_first_search(next_vertex, VTo)


    def BreadthFirstSearch(self, VFrom, VTo):
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету

        # cleaning
        self.bfs_queue = []
        self.bfs_path = []
        for vertex in self.vertex:
            vertex.Hit = False

        return self.breadth_first_search(VFrom, VTo, True)
