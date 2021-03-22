import unittest
from aBST import aBST


class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def test_tree_size(self):
        abst = aBST(0)
        self.assertEqual(len(abst.Tree), 1)
        abst = aBST(1)
        self.assertEqual(len(abst.Tree), 3)
        abst = aBST(2)
        self.assertEqual(len(abst.Tree), 7)
        abst = aBST(3)
        self.assertEqual(len(abst.Tree), 15)

    def test_find(self):
        abst = aBST(0)
        self.assertEqual(abst.FindKeyIndex(50), 0)
        abst = aBST(1)
        self.assertEqual(abst.FindKeyIndex(50), 0)
        abst = aBST(2)
        self.assertEqual(abst.FindKeyIndex(50), 0)
        abst = aBST(3)
        self.assertEqual(abst.FindKeyIndex(50), 0)
        abst = aBST(4)
        self.assertEqual(abst.FindKeyIndex(50), 0)

    def test_add_root_only_tree(self):
        abst = aBST(0)
        self.assertEqual(abst.FindKeyIndex(50), 0)
        self.assertEqual(abst.AddKey(50), 0)
        self.assertEqual(abst.FindKeyIndex(50), 0)
        self.assertEqual(abst.Tree, [50])
        self.assertEqual(abst.AddKey(50), 0)

    def test_add_depth_1(self):
        abst = aBST(1)
        self.assertEqual(abst.AddKey(50), 0)

        self.assertEqual(abst.FindKeyIndex(45), -1)
        self.assertEqual(abst.FindKeyIndex(55), -2)

        self.assertEqual(abst.AddKey(45), 1)
        self.assertEqual(abst.AddKey(55), 2)

        self.assertEqual(abst.FindKeyIndex(50), 0)
        self.assertEqual(abst.FindKeyIndex(45), 1)
        self.assertEqual(abst.FindKeyIndex(55), 2)
        self.assertEqual(abst.Tree, [50, 45, 55])

        self.assertEqual(abst.AddKey(50), 0)
        self.assertEqual(abst.AddKey(45), 1)
        self.assertEqual(abst.AddKey(55), 2)

    def test_add_depth_2(self):
        #          50
        #         /  \
        #      35      55
        #        \
        #        45

        abst = aBST(2)
        self.assertEqual(abst.AddKey(50), 0)

        self.assertEqual(abst.FindKeyIndex(35), -1)
        self.assertEqual(abst.FindKeyIndex(55), -2)
        self.assertEqual(abst.AddKey(35), 1)
        self.assertEqual(abst.AddKey(55), 2)
        self.assertEqual(abst.Tree, [50, 35, 55, None, None, None, None])

        self.assertEqual(abst.FindKeyIndex(50), 0)
        self.assertEqual(abst.FindKeyIndex(35), 1)
        self.assertEqual(abst.FindKeyIndex(55), 2)

        self.assertEqual(abst.FindKeyIndex(45), -4)
        self.assertEqual(abst.AddKey(45), 4)
        self.assertEqual(abst.FindKeyIndex(45), 4)
        self.assertEqual(abst.Tree, [50, 35, 55, None, 45, None, None])

        self.assertEqual(abst.FindKeyIndex(48), None)
        self.assertEqual(abst.AddKey(48), -1)
        self.assertEqual(abst.Tree, [50, 35, 55, None, 45, None, None])

    def test_add_depth_3(self):
        #          50
        #         /  \
        #      35      55
        #     /  \       \
        #   30    40      60
        #        /  \     /
        #       37  45   57

        #  0,  1,  2,  3,  4,    5,  6,    7,    8,  9, 10,   11,  12,  13,   14
        # 50, 35, 55, 30, 40, None, 60, None, None, 37, 45, None, None, 57, None

        abst = aBST(3)
        self.assertEqual(abst.AddKey(50), 0)

        self.assertEqual(abst.AddKey(35), 1)
        self.assertEqual(abst.AddKey(55), 2)

        self.assertEqual(abst.AddKey(60), 6)
        self.assertEqual(abst.AddKey(40), 4)
        self.assertEqual(abst.AddKey(30), 3)

        self.assertEqual(abst.AddKey(45), 10)
        self.assertEqual(abst.AddKey(57), 13)
        self.assertEqual(abst.AddKey(37), 9)

        self.assertEqual(
            abst.Tree,
            [50, 35, 55, 30, 40, None, 60, None, None, 37, 45, None, None, 57, None],
        )

        self.assertEqual(abst.AddKey(39), -1)
        self.assertEqual(abst.AddKey(48), -1)


if __name__ == '__main__':
    unittest.main()
