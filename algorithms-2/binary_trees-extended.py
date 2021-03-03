import unittest

from binary_trees import BSTNode, BSTFind, BST


class TestUM(unittest.TestCase):
    def setUp(self):
        self.parent_node = BSTNode(1, 'key1', None)
        self.tree = BST(self.parent_node)

    def test(self):
        self.assertEqual(self.parent_node, self.tree.Root)
        self.assertEqual('key1', self.tree.Root.NodeValue)

        tree2 = BST(None)
        self.assertEqual(None, tree2.Root)
        self.assertEqual(0, tree2.Count())

    def test_add_key_value_empty_root(self):
        # check system hack
        tree2 = BST(None)
        tree2.AddKeyValue(12, 'key12')
        self.assertEqual(1, tree2.Count())
        self.assertEqual('key12', tree2.Root.NodeValue)
        self.assertEqual(None, tree2.Root.LeftChild)
        self.assertEqual(None, tree2.Root.RightChild)

    def test_add_key_value(self):
        self.tree.AddKeyValue(12, 'key12')

        self.assertEqual(None, self.tree.Root.LeftChild)
        self.assertEqual(12, self.tree.Root.RightChild.NodeKey)
        self.assertEqual('key12', self.tree.Root.RightChild.NodeValue)

        self.tree.AddKeyValue(0, 'key0')
        self.assertEqual(0, self.tree.Root.LeftChild.NodeKey)
        self.assertEqual('key0', self.tree.Root.LeftChild.NodeValue)

        self.tree.AddKeyValue(11, 'key11')
        self.assertEqual(None, self.tree.Root.RightChild.RightChild)
        self.assertEqual(11, self.tree.Root.RightChild.LeftChild.NodeKey)
        self.assertEqual(
            'key11',
            self.tree.Root.RightChild.LeftChild.NodeValue
        )

        self.tree.AddKeyValue(16, 'key16')
        self.assertEqual(16, self.tree.Root.RightChild.RightChild.NodeKey)
        self.assertEqual(
            'key16',
            self.tree.Root.RightChild.RightChild.NodeValue
        )

        self.tree.AddKeyValue(13, 'key13')
        self.assertEqual(
            13,
            self.tree.Root.RightChild.RightChild.LeftChild.NodeKey
        )
        self.assertEqual(
            'key13',
            self.tree.Root.RightChild.RightChild.LeftChild.NodeValue
        )

        self.tree.AddKeyValue(20, 'key20')
        self.assertEqual(
            20,
            self.tree.Root.RightChild.RightChild.RightChild.NodeKey
        )
        self.assertEqual(
            'key20',
            self.tree.Root.RightChild.RightChild.RightChild.NodeValue
        )

        self.tree.AddKeyValue(8, 'key8')
        self.assertEqual(
            None,
            self.tree.Root.RightChild.LeftChild.RightChild
        )
        self.assertEqual(
            8,
            self.tree.Root.RightChild.LeftChild.LeftChild.NodeKey
        )
        self.assertEqual(
            'key8',
            self.tree.Root.RightChild.LeftChild.LeftChild.NodeValue
        )

        self.tree.AddKeyValue(13, 'key13')
        self.assertEqual(False, self.tree.AddKeyValue(13, 'key13'))

    def test_find_node_by_key(self):
        self.assertEqual(self.parent_node, self.tree.FindNodeByKey(1).Node)
        self.assertEqual(True, self.tree.FindNodeByKey(1).NodeHasKey)
        self.assertEqual(False, self.tree.FindNodeByKey(1).ToLeft)

        self.assertEqual(self.parent_node, self.tree.FindNodeByKey(2).Node)
        self.assertEqual(False, self.tree.FindNodeByKey(2).NodeHasKey)
        self.assertEqual(False, self.tree.FindNodeByKey(2).ToLeft)

        self.assertEqual(self.parent_node, self.tree.FindNodeByKey(0).Node)
        self.assertEqual(False, self.tree.FindNodeByKey(0).NodeHasKey)
        self.assertEqual(True, self.tree.FindNodeByKey(0).ToLeft)

        self.tree.AddKeyValue(12, 'key12')
        self.tree.AddKeyValue(0, 'key0')
        self.tree.AddKeyValue(11, 'key11')
        self.tree.AddKeyValue(16, 'key16')
        self.tree.AddKeyValue(13, 'key13')
        self.tree.AddKeyValue(20, 'key20')
        self.tree.AddKeyValue(8, 'key8')

        self.assertEqual(
            self.tree.Root.RightChild.LeftChild.LeftChild, self.tree.FindNodeByKey(8).Node)
        self.assertEqual(True, self.tree.FindNodeByKey(8).NodeHasKey)
        self.assertEqual(False, self.tree.FindNodeByKey(8).ToLeft)

        self.assertEqual(
            self.tree.Root.RightChild.LeftChild.LeftChild, self.tree.FindNodeByKey(7).Node)
        self.assertEqual(False, self.tree.FindNodeByKey(7).NodeHasKey)
        self.assertEqual(True, self.tree.FindNodeByKey(7).ToLeft)

    def test_find_min_max(self):
        self.tree.AddKeyValue(12, 'key12')
        self.tree.AddKeyValue(0, 'key0')
        self.tree.AddKeyValue(11, 'key11')
        self.tree.AddKeyValue(16, 'key16')
        self.tree.AddKeyValue(13, 'key13')
        self.tree.AddKeyValue(20, 'key20')
        self.tree.AddKeyValue(8, 'key8')

        self.assertEqual(
            0,
            self.tree.FinMinMax(self.tree.Root, False).NodeKey
        )
        self.assertEqual(
            20,
            self.tree.FinMinMax(self.tree.Root, True).NodeKey
        )

        self.assertEqual(
            8,
            self.tree.FinMinMax(self.tree.Root.RightChild, False).NodeKey
        )
        self.assertEqual(
            20,
            self.tree.FinMinMax(self.tree.Root.RightChild, True).NodeKey
        )

    def test_count(self):
        self.assertEqual(1, self.tree.Count())

        self.tree.AddKeyValue(12, 'key12')
        self.tree.AddKeyValue(0, 'key0')
        self.tree.AddKeyValue(11, 'key11')

        self.assertEqual(4, self.tree.Count())

        self.tree.AddKeyValue(16, 'key16')
        self.tree.AddKeyValue(13, 'key13')
        self.tree.AddKeyValue(20, 'key20')
        self.tree.AddKeyValue(8, 'key8')

        self.assertEqual(8, self.tree.Count())

    def test_delete_empty_tree(self):
        tree2 = BST(None)
        self.assertEqual(0, tree2.Count())
        self.assertEqual(False, tree2.DeleteNodeByKey(777))

    def test_delete_root_leaf(self):
        self.assertEqual(1, self.tree.Count())

        self.tree.DeleteNodeByKey(1)
        self.assertEqual(None, self.tree.Root)
        self.assertEqual(0, self.tree.Count())

        self.tree.AddKeyValue(1, 'key1')
        self.tree.AddKeyValue(-5, 'key-5')
        self.tree.AddKeyValue(-2, 'key-2')
        self.tree.AddKeyValue(-6, 'key-6')
        self.assertEqual(4, self.tree.Count())
        self.tree.DeleteNodeByKey(1)
        self.assertEqual(3, self.tree.Count())
        self.assertEqual(-5, self.tree.Root.NodeKey)
        self.assertEqual(-2, self.tree.Root.RightChild.NodeKey)
        self.assertEqual(-6, self.tree.Root.LeftChild.NodeKey)

        self.tree = BST(BSTNode(1, 'key1', None))
        self.tree.AddKeyValue(12, 'key12')
        self.tree.AddKeyValue(0, 'key0')
        self.tree.AddKeyValue(11, 'key11')
        self.tree.AddKeyValue(16, 'key16')
        self.tree.AddKeyValue(13, 'key13')
        self.tree.AddKeyValue(20, 'key20')
        self.tree.AddKeyValue(8, 'key8')
        self.assertEqual(8, self.tree.Count())

        self.tree.DeleteNodeByKey(1)
        self.assertEqual(7, self.tree.Count())

    def test_delete_right_leaf_false(self):
        self.tree.AddKeyValue(12, 'key12')
        self.tree.AddKeyValue(0, 'key0')
        self.tree.AddKeyValue(11, 'key11')
        self.tree.AddKeyValue(16, 'key16')
        self.tree.AddKeyValue(13, 'key13')
        self.tree.AddKeyValue(20, 'key20')
        self.tree.AddKeyValue(8, 'key8')

        self.assertEqual(False, self.tree.DeleteNodeByKey(777))

        self.assertEqual(12, self.tree.FindNodeByKey(12).Node.NodeKey)
        self.assertEqual('key12', self.tree.FindNodeByKey(12).Node.NodeValue)

        self.tree.DeleteNodeByKey(12)

        self.assertEqual(False, self.tree.FindNodeByKey(12).NodeHasKey)

        self.assertEqual(
            13,
            self.tree.Root.RightChild.NodeKey
        )
        self.assertEqual(
            16,
            self.tree.Root.RightChild.RightChild.NodeKey
        )
        self.assertEqual(
            11,
            self.tree.Root.RightChild.LeftChild.NodeKey
        )
        self.assertEqual(
            13,
            self.tree.Root.RightChild.RightChild.Parent.NodeKey
        )
        self.assertEqual(
            13,
            self.tree.Root.RightChild.LeftChild.Parent.NodeKey
        )

    def test_delete_right_leaf_true(self):
        self.tree.AddKeyValue(12, 'key12')
        self.tree.AddKeyValue(0, 'key0')
        self.tree.AddKeyValue(11, 'key11')
        self.tree.AddKeyValue(16, 'key16')
        self.tree.AddKeyValue(20, 'key20')
        self.tree.AddKeyValue(8, 'key8')

        self.assertEqual(False, self.tree.DeleteNodeByKey(777))

        self.assertEqual(12, self.tree.FindNodeByKey(12).Node.NodeKey)
        self.assertEqual('key12', self.tree.FindNodeByKey(12).Node.NodeValue)

        self.tree.DeleteNodeByKey(12)

        self.assertEqual(False, self.tree.FindNodeByKey(12).NodeHasKey)

        self.assertEqual(
            16,
            self.tree.Root.RightChild.NodeKey
        )
        self.assertEqual(
            20,
            self.tree.Root.RightChild.RightChild.NodeKey
        )
        self.assertEqual(
            11,
            self.tree.Root.RightChild.LeftChild.NodeKey
        )
        self.assertEqual(
            16,
            self.tree.Root.RightChild.RightChild.Parent.NodeKey
        )
        self.assertEqual(
            16,
            self.tree.Root.RightChild.LeftChild.Parent.NodeKey
        )


if __name__ == '__main__':
    unittest.main()
