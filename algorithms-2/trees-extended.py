import unittest

from trees import SimpleTreeNode, SimpleTree


class TestUM(unittest.TestCase):
    def setUp(self):
        self.parent_node = SimpleTreeNode(1, None)
        self.tree = SimpleTree(self.parent_node)
        self.assertEqual(self.parent_node, self.tree.Root)

    def test_add_child(self):
        child2 = SimpleTreeNode(2, self.parent_node)
        self.tree.AddChild(self.parent_node, child2)
        self.assertEqual(child2, self.tree.Root.Children[0])

        child3 = SimpleTreeNode(3, self.parent_node)
        self.tree.AddChild(self.parent_node, child3)
        self.assertEqual(child3, self.tree.Root.Children[1])

    def test_delete_child(self):
        child2 = SimpleTreeNode(2, self.parent_node)
        self.tree.AddChild(self.parent_node, child2)

        child3 = SimpleTreeNode(3, self.parent_node)
        self.tree.AddChild(self.parent_node, child3)

        self.tree.DeleteNode(child2)
        self.assertEqual(child3, self.tree.Root.Children[0])

        child4 = SimpleTreeNode(4, child3)
        self.tree.AddChild(child3, child4)

        child5 = SimpleTreeNode(5, child3)
        self.tree.AddChild(child3, child5)

        self.tree.DeleteNode(child4)
        self.assertEqual(child5, self.tree.Root.Children[0].Children[0])

    def test_get_all_nodes(self):
        self.assertEqual([self.parent_node], self.tree.GetAllNodes())

        child2 = SimpleTreeNode(2, self.parent_node)
        self.tree.AddChild(self.parent_node, child2)

        child3 = SimpleTreeNode(3, self.parent_node)
        self.tree.AddChild(self.parent_node, child3)

        self.assertEqual(
            [self.parent_node, child2, child3],
            self.tree.GetAllNodes()
        )

        child4 = SimpleTreeNode(4, child2)
        self.tree.AddChild(child2, child4)

        child5 = SimpleTreeNode(5, child2)
        self.tree.AddChild(child2, child5)

        self.assertEqual(
            [self.parent_node, child2, child4, child5, child3],
            self.tree.GetAllNodes()
        )

        child6 = SimpleTreeNode(6, child4)
        self.tree.AddChild(child4, child6)

        child7 = SimpleTreeNode(7, child4)
        self.tree.AddChild(child4, child7)

        self.assertEqual(
            [self.parent_node, child2, child4, child6, child7, child5, child3],
            self.tree.GetAllNodes()
        )

    def test_find_nodes(self):
        child2 = SimpleTreeNode(2, self.parent_node)
        self.tree.AddChild(self.parent_node, child2)

        child3 = SimpleTreeNode(3, self.parent_node)
        self.tree.AddChild(self.parent_node, child3)

        child4 = SimpleTreeNode(4, child2)
        self.tree.AddChild(child2, child4)

        child5 = SimpleTreeNode(5, child2)
        self.tree.AddChild(child2, child5)

        child2_again = SimpleTreeNode(2, child4)
        self.tree.AddChild(child4, child2_again)

        child2_another_one = SimpleTreeNode(2, child4)
        self.tree.AddChild(child4, child2_another_one)

        self.assertEqual(
            [],
            self.tree.FindNodesByValue(0)
        )

        self.assertEqual(
            [child5],
            self.tree.FindNodesByValue(5)
        )

        self.assertEqual(
            [child2, child2_again, child2_another_one],
            self.tree.FindNodesByValue(2)
        )

    def test_count_all_nodes(self):

        self.assertEqual(1, self.tree.Count())

        child2 = SimpleTreeNode(2, self.parent_node)
        self.tree.AddChild(self.parent_node, child2)

        child3 = SimpleTreeNode(3, self.parent_node)
        self.tree.AddChild(self.parent_node, child3)

        child4 = SimpleTreeNode(4, child2)
        self.tree.AddChild(child2, child4)

        self.assertEqual(4, self.tree.Count())

        child5 = SimpleTreeNode(5, child2)
        self.tree.AddChild(child2, child5)

        child6 = SimpleTreeNode(6, child4)
        self.tree.AddChild(child4, child6)

        child7 = SimpleTreeNode(7, child4)
        self.tree.AddChild(child4, child7)

        self.assertEqual(7, self.tree.Count())

    def test_count_all_leaves(self):

        self.assertEqual(1, self.tree.LeafCount())

        child2 = SimpleTreeNode(2, self.parent_node)
        self.tree.AddChild(self.parent_node, child2)

        child3 = SimpleTreeNode(3, self.parent_node)
        self.tree.AddChild(self.parent_node, child3)

        self.assertEqual(2, self.tree.LeafCount())

        child4 = SimpleTreeNode(4, child2)
        self.tree.AddChild(child2, child4)

        child5 = SimpleTreeNode(5, child2)
        self.tree.AddChild(child2, child5)

        self.assertEqual(3, self.tree.LeafCount())

        child6 = SimpleTreeNode(6, child4)
        self.tree.AddChild(child4, child6)

        child7 = SimpleTreeNode(7, child4)
        self.tree.AddChild(child4, child7)

        self.assertEqual(4, self.tree.LeafCount())

    def test_move_node(self):
        child2 = SimpleTreeNode(2, self.parent_node)
        self.tree.AddChild(self.parent_node, child2)

        child3 = SimpleTreeNode(3, self.parent_node)
        self.tree.AddChild(self.parent_node, child3)

        child4 = SimpleTreeNode(4, child2)
        self.tree.AddChild(child2, child4)

        child5 = SimpleTreeNode(5, child2)
        self.tree.AddChild(child2, child5)

        child6 = SimpleTreeNode(6, child4)
        self.tree.AddChild(child4, child6)

        child7 = SimpleTreeNode(7, child4)
        self.tree.AddChild(child4, child7)

        self.assertEqual(0, len(child3.Children))

        self.tree.MoveNode(child4, child3)

        self.assertEqual(1, len(child2.Children))
        self.assertEqual(child5, child2.Children[0])

        self.assertEqual(1, len(child3.Children))
        self.assertEqual(child4, child3.Children[0])
        self.assertEqual(2, len(child4.Children))
        self.assertEqual([child6, child7], child4.Children)

    def test_set_levels(self):
        self.tree.set_levels()
        self.assertEqual(0, self.tree.Root.level)

        child2 = SimpleTreeNode(2, self.parent_node)
        self.tree.AddChild(self.parent_node, child2)

        child3 = SimpleTreeNode(3, self.parent_node)
        self.tree.AddChild(self.parent_node, child3)

        self.tree.set_levels()
        self.assertEqual(1, child3.level)

        child4 = SimpleTreeNode(4, child2)
        self.tree.AddChild(child2, child4)

        child5 = SimpleTreeNode(5, child2)
        self.tree.AddChild(child2, child5)

        self.tree.set_levels()
        self.assertEqual(2, child4.level)

        child6 = SimpleTreeNode(6, child4)
        self.tree.AddChild(child4, child6)

        child7 = SimpleTreeNode(7, child4)
        self.tree.AddChild(child4, child7)

        self.tree.set_levels()
        self.assertEqual(3, child7.level)


if __name__ == '__main__':
    unittest.main()
