import unittest
from DFS import Vertex, SimpleGraph


class TestUM(unittest.TestCase):
    def test_DepthFirstSearch(self):
        #    A --- B
        #    |\    | \
        #    |  \  |  E
        #    |    \| /
        #    C --- D_
        #          | |
        #          |_|

        self.size = 5
        self.sg = SimpleGraph(self.size)
        self.sg.AddVertex("A")
        self.sg.AddVertex("B")
        self.sg.AddVertex("C")
        self.sg.AddVertex("D")
        self.sg.AddVertex("E")

        self.assertEqual(self.sg.m_adjacency, [[0] * self.size for _ in range(self.size)])
        self.sg.AddEdge(0, 2)  # A + C
        self.sg.AddEdge(0, 1)  # A + B
        self.sg.AddEdge(0, 3)  # A + D
        self.sg.AddEdge(3, 3)  # D + D
        self.sg.AddEdge(1, 4)  # B + E
        self.sg.AddEdge(3, 4)  # D + E
        self.sg.AddEdge(1, 3)  # B + D
        self.sg.AddEdge(2, 3)  # C + D
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

        case = self.sg.DepthFirstSearch(0, 0)
        self.assertEqual(
            [x.Value for x in case],
            ['A', 'B', 'A'],
        )

        case = self.sg.DepthFirstSearch(3, 3)
        self.assertEqual(
            [x.Value for x in case],
            ['D', 'D'],
        )

        case = self.sg.DepthFirstSearch(0, 4)
        self.assertEqual(
            [x.Value for x in case],
            ['A', 'B', 'E'],
        )

        case = self.sg.DepthFirstSearch(1, 2)
        self.assertEqual(
            [x.Value for x in case],
            ['B', 'A', 'C'],
        )

        case = self.sg.DepthFirstSearch(4, 2)
        self.assertEqual(
            [x.Value for x in case],
            ['E', 'B', 'A', 'C'],
        )

        case = self.sg.DepthFirstSearch(3, 4)
        self.assertEqual(
            [x.Value for x in case],
            ['D', 'E'],
        )


    def test_DepthFirstSearch2(self):
        #    A     B
        #    |\    |
        #    |  \  |  E
        #    |    \| /
        #    C --- D_
        #          | |
        #          |_|

        self.size = 5
        self.sg = SimpleGraph(self.size)
        self.sg.AddVertex("A")
        self.sg.AddVertex("B")
        self.sg.AddVertex("C")
        self.sg.AddVertex("D")
        self.sg.AddVertex("E")

        self.assertEqual(self.sg.m_adjacency, [[0] * self.size for _ in range(self.size)])
        self.sg.AddEdge(0, 2)  # A + C
        self.sg.AddEdge(0, 3)  # A + D
        self.sg.AddEdge(3, 3)  # D + D
        self.sg.AddEdge(3, 4)  # D + E
        self.sg.AddEdge(1, 3)  # B + D
        self.sg.AddEdge(2, 3)  # C + D
        self.assertEqual(
            self.sg.m_adjacency,
            [
                [0, 0, 1, 1, 0],
                [0, 0, 0, 1, 0],
                [1, 0, 0, 1, 0],
                [1, 1, 1, 1, 1],
                [0, 0, 0, 1, 0],
            ],
        )

        case = self.sg.DepthFirstSearch(0, 4)
        self.assertEqual(
            [x.Value for x in case],
            ['A', 'C', 'D', 'E'],
        )

        case = self.sg.DepthFirstSearch(4, 0)
        self.assertEqual(
            [x.Value for x in case],
            ['E', 'D', 'A'],
        )

    def test_DepthFirstSearch3(self):
        #           _
        #          | |
        #    A     B_|
        #    |\
        #    |  \     E
        #    |    \  /
        #    C --- D_
        #          | |
        #          |_|

        self.size = 5
        self.sg = SimpleGraph(self.size)
        self.sg.AddVertex("A")
        self.sg.AddVertex("B")
        self.sg.AddVertex("C")
        self.sg.AddVertex("D")
        self.sg.AddVertex("E")

        self.assertEqual(self.sg.m_adjacency, [[0] * self.size for _ in range(self.size)])
        self.sg.AddEdge(0, 2)  # A + C
        self.sg.AddEdge(0, 3)  # A + D
        self.sg.AddEdge(3, 3)  # D + D
        self.sg.AddEdge(3, 4)  # D + E
        self.sg.AddEdge(2, 3)  # C + D
        self.sg.AddEdge(1, 1)  # B + B
        self.assertEqual(
            self.sg.m_adjacency,
            [
                [0, 0, 1, 1, 0],
                [0, 1, 0, 0, 0],
                [1, 0, 0, 1, 0],
                [1, 0, 1, 1, 1],
                [0, 0, 0, 1, 0],
            ],
        )

        case = self.sg.DepthFirstSearch(0, 4)
        self.assertEqual(
            [x.Value for x in case],
            ['A', 'C', 'D', 'E'],
        )

        case = self.sg.DepthFirstSearch(4, 0)
        self.assertEqual(
            [x.Value for x in case],
            ['E', 'D', 'A'],
        )

        case = self.sg.DepthFirstSearch(0, 1)
        self.assertEqual(
            [x.Value for x in case],
            [],
        )

        case = self.sg.DepthFirstSearch(4, 1)
        self.assertEqual(
            [x.Value for x in case],
            [],
        )

        case = self.sg.DepthFirstSearch(1, 1)
        self.assertEqual(
            [x.Value for x in case],
            ['B', 'B'],
        )


if __name__ == "__main__":
    unittest.main()
