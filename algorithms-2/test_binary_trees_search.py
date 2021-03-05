import unittest

from binary_trees_search import BSTNode, BST_SEARCH


class TestUM(unittest.TestCase):
    def setUp(self):
        self.parent_node = BSTNode(1, 'key1', None)
        self.tree = BST_SEARCH(self.parent_node)
        self.tree.AddKeyValue(12, 'key12')
        self.tree.AddKeyValue(0, 'key0')
        self.tree.AddKeyValue(11, 'key11')
        self.tree.AddKeyValue(16, 'key16')
        self.tree.AddKeyValue(13, 'key13')
        self.tree.AddKeyValue(20, 'key20')
        self.tree.AddKeyValue(8, 'key8')

    def test_wide_all_nodes(self):
        self.tree.WideAllNodes()
        self.assertEqual(
            [1, 0, 12, 11, 16, 8, 13, 20],
            [x.NodeKey for x in self.tree.WideAllNodes()]
        )

        self.tree = BST_SEARCH(None)
        self.assertEqual((), self.tree.WideAllNodes())


if __name__ == '__main__':
    unittest.main()
