import unittest
from binary_trees import BSTNode, BST


class TestUM(unittest.TestCase):
    def setUp(self):
        #          50
        #         /  \
        #      35      55
        #     /  \       \
        #   30    40      60
        #        /  \     /
        #       37  45   57

        self.parent_node = BSTNode(50, 'key50', None)
        self.tree = BST(self.parent_node)
        self.tree.AddKeyValue(35, 'key35')
        self.tree.AddKeyValue(55, 'key55')
        self.tree.AddKeyValue(30, 'key30')
        self.tree.AddKeyValue(40, 'key40')
        self.tree.AddKeyValue(60, 'key60')
        self.tree.AddKeyValue(37, 'key37')
        self.tree.AddKeyValue(45, 'key45')
        self.tree.AddKeyValue(57, 'key57')

    def test_wide_all_nodes(self):
        self.assertEqual(
            [50, 35, 55, 30, 40, 60, 37, 45, 57],
            [x.NodeKey for x in self.tree.WideAllNodes()]
        )

        self.tree = BST(None)
        self.assertEqual((), self.tree.WideAllNodes())

    def test_deep_all_nodes_preorder(self):
        self.assertEqual(
            [50, 35, 30, 40, 37, 45, 55, 60, 57],
            [x.NodeKey for x in self.tree.DeepAllNodes(2)]
        )
        self.tree = BST(None)
        self.assertEqual((), self.tree.DeepAllNodes(2))

    def test_deep_all_nodes_inorder(self):
        self.assertEqual(
            [30, 35, 37, 40, 45, 50, 55, 57, 60],
            [x.NodeKey for x in self.tree.DeepAllNodes(0)]
        )
        self.tree = BST(None)
        self.assertEqual((), self.tree.DeepAllNodes(0))

    def test_deep_all_nodes_postorder(self):
        self.assertEqual(
            [30, 37, 45, 40, 35, 57, 60, 55, 50],
            [x.NodeKey for x in self.tree.DeepAllNodes(1)]
        )
        self.tree = BST(None)
        self.assertEqual((), self.tree.DeepAllNodes(1))


if __name__ == '__main__':
    unittest.main()
