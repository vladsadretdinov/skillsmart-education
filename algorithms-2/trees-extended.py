import unittest


class SimpleTreeNode:
    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:
    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def recursive_traversal_delete(self, f_node, parent):
        if parent is None:
            parent = self.Root
        for index, node in enumerate(parent.Children):
            if node is f_node:
                del parent.Children[index]
                return
            if len(node.Children) > 0:
                self.recursive_traversal_delete(f_node, node)

    def recursive_traversal_get(self, parent):
        nodes = []
        if parent is None:
            nodes.append(self.Root)
            parent = self.Root
        for node in parent.Children:
            nodes.append(node)
            if len(node.Children) > 0:
                nodes.extend(self.recursive_traversal_get(node))
        return nodes

    def AddChild(self, ParentNode, NewChild):
        # ваш код добавления нового дочернего узла существующему ParentNode
        ParentNode.Children.append(NewChild)

    def DeleteNode(self, NodeToDelete):
        # ваш код удаления существующего узла NodeToDelete (некорневой)
        self.recursive_traversal_delete(NodeToDelete, None)

    def GetAllNodes(self):
        # ваш код выдачи всех узлов дерева в определённом порядке
        return self.recursive_traversal_get(None)

    def FindNodesByValue(self, val):
        # ваш код поиска узлов по значению
        all_nodes = self.GetAllNodes()
        filtered_nodes = [x for x in all_nodes if x.NodeValue == val]
        return filtered_nodes

    def MoveNode(self, OriginalNode, NewParent):
        # ваш код перемещения узла вместе с его поддеревом --
        # в качестве дочернего для узла NewParent
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)

    def Count(self):
        # количество всех узлов в дереве
        all_nodes = self.GetAllNodes()
        return len(all_nodes)

    def LeafCount(self):
        # количество листьев в дереве
        all_nodes = self.GetAllNodes()
        leaf_nodes = [x for x in all_nodes if len(x.Children) == 0]
        return len(leaf_nodes)

    def set_levels(self, parent=None, level=0):
        if parent is None:
            self.Root.level = level
            parent = self.Root
        for node in parent.Children:
            node.level = level + 1
            if len(node.Children) > 0:
                self.set_levels(node, level + 1)
        return None


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
