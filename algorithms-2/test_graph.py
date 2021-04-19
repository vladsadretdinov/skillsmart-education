import unittest
from graph import Vertex, SimpleGraph


class TestUM(unittest.TestCase):
    def setUp(self):
        self.size = 5
        self.sg = SimpleGraph(self.size)
        self.sg.AddVertex("A")
        self.sg.AddVertex("B")
        self.sg.AddVertex("C")
        self.sg.AddVertex("D")
        self.sg.AddVertex("E")

    def test_init(self):
        sg = SimpleGraph(3)
        self.assertEqual(sg.max_vertex, 3)
        self.assertEqual(sg.m_adjacency, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.assertEqual(sg.vertex, [None, None, None])

    def test_add_vertex_without_adjacency(self):
        self.sg.AddVertex("F")
        self.assertEqual(len(self.sg.vertex), self.size)
        self.assertEqual([x.Value for x in self.sg.vertex], ["A", "B", "C", "D", "E"])
        self.assertEqual(self.sg.m_adjacency, [[0] * self.size for _ in range(self.size)])
        self.assertEqual(
            self.sg.m_adjacency,
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
        )

    def test_add_edge(self):
        self.assertEqual(self.sg.m_adjacency, [[0] * self.size for _ in range(self.size)])
        self.sg.AddEdge(0, 2)  # A + C
        self.assertEqual(self.sg.m_adjacency[0][2], 1)
        self.assertEqual(self.sg.m_adjacency[2][0], 1)
        self.assertEqual(self.sg.IsEdge(0, 2), True)

        self.sg.AddEdge(0, 1)  # A + B
        self.assertEqual(self.sg.m_adjacency[0][1], 1)
        self.assertEqual(self.sg.m_adjacency[1][0], 1)
        self.assertEqual(self.sg.IsEdge(0, 1), True)

        self.sg.AddEdge(0, 3)  # A + D
        self.assertEqual(self.sg.m_adjacency[0][3], 1)
        self.assertEqual(self.sg.m_adjacency[3][0], 1)
        self.assertEqual(self.sg.IsEdge(0, 3), True)

        self.sg.AddEdge(3, 3)  # D + D
        self.assertEqual(self.sg.m_adjacency[3][3], 1)
        self.assertEqual(self.sg.m_adjacency[3][3], 1)
        self.assertEqual(self.sg.IsEdge(3, 3), True)

        self.sg.AddEdge(1, 4)  # B + E
        self.assertEqual(self.sg.m_adjacency[1][4], 1)
        self.assertEqual(self.sg.m_adjacency[4][1], 1)
        self.assertEqual(self.sg.IsEdge(1, 4), True)

        self.sg.AddEdge(3, 4)  # D + E
        self.assertEqual(self.sg.m_adjacency[3][4], 1)
        self.assertEqual(self.sg.m_adjacency[3][4], 1)
        self.assertEqual(self.sg.IsEdge(3, 4), True)

        self.sg.AddEdge(1, 3)  # B + D
        self.assertEqual(self.sg.m_adjacency[1][3], 1)
        self.assertEqual(self.sg.m_adjacency[3][1], 1)
        self.assertEqual(self.sg.IsEdge(1, 3), True)

        self.sg.AddEdge(2, 3)  # C + D
        self.assertEqual(self.sg.m_adjacency[2][3], 1)
        self.assertEqual(self.sg.m_adjacency[3][2], 1)
        self.assertEqual(self.sg.IsEdge(2, 3), True)

        self.assertEqual(
            self.sg.m_adjacency,
            [
                [0, 1, 1, 1, 0],
                [1, 0, 0, 1, 1],
                [1, 0, 0, 1, 0],
                [1, 1, 1, 1, 1],
                [0, 1, 0, 1, 0],
            ],
        )

    def test_delete_vertex(self):
        self.assertEqual(self.sg.m_adjacency, [[0] * self.size for _ in range(self.size)])
        self.sg.AddEdge(0, 2)  # A + C
        self.assertEqual(self.sg.m_adjacency[0][2], 1)
        self.assertEqual(self.sg.m_adjacency[2][0], 1)
        self.assertEqual(self.sg.IsEdge(0, 2), True)
        self.assertEqual(
            self.sg.m_adjacency,
            [
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
        )

        self.sg.RemoveVertex(2)

        self.assertEqual(self.sg.vertex[2], None)
        self.assertEqual(self.sg.m_adjacency[0][2], 0)
        self.assertEqual(self.sg.m_adjacency[2][0], 0)
        self.assertEqual(self.sg.IsEdge(0, 2), False)
        self.assertEqual(
            self.sg.m_adjacency,
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
        )

    def test_delete_edge(self):
        self.assertEqual(self.sg.m_adjacency, [[0] * self.size for _ in range(self.size)])
        self.sg.AddEdge(0, 2)  # A + C
        self.assertEqual(self.sg.m_adjacency[0][2], 1)
        self.assertEqual(self.sg.m_adjacency[2][0], 1)
        self.assertEqual(self.sg.IsEdge(0, 2), True)
        self.assertEqual(
            self.sg.m_adjacency,
            [
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
        )

        self.sg.RemoveEdge(0, 2)

        self.assertEqual(self.sg.m_adjacency[0][2], 0)
        self.assertEqual(self.sg.m_adjacency[2][0], 0)
        self.assertEqual(self.sg.IsEdge(0, 2), False)
        self.assertEqual(
            self.sg.m_adjacency,
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
        )


if __name__ == "__main__":
    unittest.main()
