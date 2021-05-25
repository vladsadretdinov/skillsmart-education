import unittest

from Even_trees_and_forests import SimpleTreeNode, SimpleTree


class TestUM(unittest.TestCase):
    def test0(self):
        #
        #            1
        #         /  |  \
        #        2   3   4
        #
        self.parent_node = SimpleTreeNode(1, None)
        self.tree = SimpleTree(self.parent_node)

        child2 = SimpleTreeNode(2, self.parent_node)
        self.tree.AddChild(self.parent_node, child2)
        child3 = SimpleTreeNode(3, self.parent_node)
        self.tree.AddChild(self.parent_node, child3)
        child4 = SimpleTreeNode(4, self.parent_node)
        self.tree.AddChild(self.parent_node, child4)

        self.assertEqual(self.tree.EvenTrees(), [])

    def test_vertical(self):
        #
        #   1 - 2 x 3 - 4 x 5 - 6
        #
        self.parent_node = SimpleTreeNode(1, None)
        self.tree = SimpleTree(self.parent_node)

        child2 = SimpleTreeNode(2, self.parent_node)
        self.tree.AddChild(self.parent_node, child2)
        child3 = SimpleTreeNode(3, child2)
        self.tree.AddChild(child2, child3)
        child4 = SimpleTreeNode(4, child3)
        self.tree.AddChild(child3, child4)
        child5 = SimpleTreeNode(5, child4)
        self.tree.AddChild(child4, child5)
        child6 = SimpleTreeNode(6, child5)
        self.tree.AddChild(child5, child6)

        self.assertEqual(self.tree.EvenTrees(), [child2, child3, child4, child5])

    def test1(self):
        #
        #           1
        #         /   x
        #        2     3
        #              |
        #              4
        #
        self.parent_node = SimpleTreeNode(1, None)
        self.tree = SimpleTree(self.parent_node)

        child2 = SimpleTreeNode(2, self.parent_node)
        self.tree.AddChild(self.parent_node, child2)
        child3 = SimpleTreeNode(3, self.parent_node)
        self.tree.AddChild(self.parent_node, child3)
        child4 = SimpleTreeNode(4, child3)
        self.tree.AddChild(child3, child4)

        self.assertEqual(self.tree.EvenTrees(), [self.parent_node, child3])

    def test2(self):
        #
        #            1
        #         x  x   \
        #        6   3     2
        #        |   |   x  x  \  \
        #        8   4   7   5  17 18
        #       x x      |   |
        #      10  9     11  12
        #      |   |     x
        #      15  16    13
        #                |
        #                14
        #
        self.parent_node = SimpleTreeNode(1, None)
        self.tree = SimpleTree(self.parent_node)

        child6 = SimpleTreeNode(6, self.parent_node)
        self.tree.AddChild(self.parent_node, child6)
        child3 = SimpleTreeNode(3, self.parent_node)
        self.tree.AddChild(self.parent_node, child3)
        child2 = SimpleTreeNode(2, self.parent_node)
        self.tree.AddChild(self.parent_node, child2)

        child7 = SimpleTreeNode(7, child2)
        self.tree.AddChild(child2, child7)
        child5 = SimpleTreeNode(5, child2)
        self.tree.AddChild(child2, child5)

        child4 = SimpleTreeNode(4, child3)
        self.tree.AddChild(child3, child4)

        child8 = SimpleTreeNode(8, child6)
        self.tree.AddChild(child6, child8)

        child10 = SimpleTreeNode(10, child8)
        self.tree.AddChild(child8, child10)
        child9 = SimpleTreeNode(9, child8)
        self.tree.AddChild(child8, child9)

        child15 = SimpleTreeNode(15, child10)
        self.tree.AddChild(child10, child15)
        child16 = SimpleTreeNode(16, child9)
        self.tree.AddChild(child9, child16)

        child11 = SimpleTreeNode(11, child7)
        self.tree.AddChild(child7, child11)
        child12 = SimpleTreeNode(12, child5)
        self.tree.AddChild(child5, child12)

        child13 = SimpleTreeNode(13, child11)
        self.tree.AddChild(child11, child13)
        child14 = SimpleTreeNode(14, child13)
        self.tree.AddChild(child13, child14)

        child17 = SimpleTreeNode(17, child2)
        self.tree.AddChild(child2, child17)

        child18 = SimpleTreeNode(18, child2)
        self.tree.AddChild(child2, child18)

        self.assertEqual(
            self.tree.EvenTrees(),
            [
                self.parent_node, child6,
                child8, child10,
                child8, child9,
                self.parent_node, child3,
                child2, child7,
                child11, child13,
                child2, child5
            ]
        )


if __name__ == '__main__':
    unittest.main()
