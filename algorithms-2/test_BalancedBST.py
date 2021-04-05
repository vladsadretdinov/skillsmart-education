import unittest

from BalancedBST import BalancedBST, BSTNode


class TestUM(unittest.TestCase):
    def setUp(self):
        self.bst = BalancedBST()

    def test_empty_tree(self):
        self.bst.GenerateTree([])
        self.assertEqual(self.bst.Root, None)
        self.assertEqual(self.bst.IsBalanced(self.bst.Root), True)

    def test_root_only(self):
        self.bst.GenerateTree([50])
        self.assertEqual(self.bst.Root.NodeKey, 50)
        self.assertEqual(self.bst.Root.Parent, None)
        self.assertEqual(self.bst.Root.LeftChild, None)
        self.assertEqual(self.bst.Root.RightChild, None)
        self.assertEqual(self.bst.Root.Level, 1)
        self.assertEqual(self.bst.IsBalanced(self.bst.Root), True)

    def test_generateBSST(self):
        #           58
        #         /    \
        #      35       66
        #     /  \     /
        #   30    50  60
        pseudo_random_arr = [58, 30, 60, 35, 66, 50]
        # sorted = [30, 35, 50, 58, 60, 66]
        self.bst.GenerateTree(pseudo_random_arr)
        self.assertEqual(self.bst.Root.NodeKey, 58)
        self.assertEqual(self.bst.Root.Parent, None)
        self.assertEqual(self.bst.Root.Level, 1)
        self.assertEqual(self.bst.IsBalanced(self.bst.Root), True)

        self.assertEqual(self.bst.Root.LeftChild.NodeKey, 35)
        self.assertEqual(self.bst.Root.LeftChild.Parent, self.bst.Root)
        self.assertEqual(self.bst.Root.LeftChild.Level, 2)
        self.assertEqual(self.bst.IsBalanced(self.bst.Root.LeftChild), True)

        self.assertEqual(self.bst.Root.RightChild.NodeKey, 66)
        self.assertEqual(self.bst.Root.RightChild.Parent, self.bst.Root)
        self.assertEqual(self.bst.Root.RightChild.Level, 2)
        self.assertEqual(self.bst.IsBalanced(self.bst.Root.RightChild), True)

        self.assertEqual(self.bst.Root.LeftChild.LeftChild.NodeKey, 30)
        self.assertEqual(self.bst.Root.LeftChild.LeftChild.Parent, self.bst.Root.LeftChild)
        self.assertEqual(self.bst.Root.LeftChild.LeftChild.Level, 3)
        self.assertEqual(self.bst.IsBalanced(self.bst.Root.LeftChild.LeftChild), True)
        self.assertEqual(self.bst.Root.LeftChild.LeftChild.LeftChild, None)
        self.assertEqual(self.bst.Root.LeftChild.LeftChild.RightChild, None)

        self.assertEqual(self.bst.Root.LeftChild.RightChild.NodeKey, 50)
        self.assertEqual(self.bst.Root.LeftChild.RightChild.Parent, self.bst.Root.LeftChild)
        self.assertEqual(self.bst.Root.LeftChild.RightChild.Level, 3)
        self.assertEqual(self.bst.IsBalanced(self.bst.Root.LeftChild.RightChild), True)
        self.assertEqual(self.bst.Root.LeftChild.RightChild.LeftChild, None)
        self.assertEqual(self.bst.Root.LeftChild.RightChild.RightChild, None)

        self.assertEqual(self.bst.Root.RightChild.LeftChild.NodeKey, 60)
        self.assertEqual(self.bst.Root.RightChild.LeftChild.Parent, self.bst.Root.RightChild)
        self.assertEqual(self.bst.Root.RightChild.LeftChild.Level, 3)
        self.assertEqual(self.bst.IsBalanced(self.bst.Root.RightChild.LeftChild), True)
        self.assertEqual(self.bst.Root.RightChild.LeftChild.LeftChild, None)
        self.assertEqual(self.bst.Root.RightChild.LeftChild.RightChild, None)

    def test_generateBSST2(self):
        #           6
        #         /    \
        #      3        9
        #     /  \     /  \
        #   2     5   8   10
        #  /     /   /
        # 1     4   7
        pseudo_random_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.bst.GenerateTree(pseudo_random_arr)
        self.assertEqual(self.bst.Root.NodeKey, 6)
        self.assertEqual(self.bst.Root.Parent, None)
        self.assertEqual(self.bst.Root.Level, 1)
        self.assertEqual(self.bst.IsBalanced(self.bst.Root), True)

    def test_generateBSST3(self):
        #          7
        #        /   \
        #      4      11
        #     / \    /  \
        #   2    6  9    13
        #  / \  /  / \   /
        # 1  3 5  8  10 12
        pseudo_random_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.bst.GenerateTree(pseudo_random_arr)
        self.assertEqual(self.bst.Root.NodeKey, 7)
        self.assertEqual(self.bst.Root.Parent, None)
        self.assertEqual(self.bst.Root.Level, 1)
        self.assertEqual(self.bst.IsBalanced(self.bst.Root), True)

    def test_generateBSST4(self):
        #           8
        #        /     \
        #      4        12
        #     / \      /  \
        #   2    6    10    14
        #  / \  / \  / \   /  \
        # 1  3 5  7 9  11 13  15
        pseudo_random_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.bst.GenerateTree(pseudo_random_arr)
        self.assertEqual(self.bst.Root.NodeKey, 8)
        self.assertEqual(self.bst.Root.Parent, None)
        self.assertEqual(self.bst.Root.Level, 1)
        self.assertEqual(self.bst.IsBalanced(self.bst.Root), True)

if __name__ == '__main__':
    unittest.main()
