import unittest
from balanced_tree import GenerateBBSTArray


class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_array(self):
        self.assertEqual(GenerateBBSTArray(None), None)
        self.assertEqual(GenerateBBSTArray([]), None)

    def test_array_with_one_element(self):
        self.assertEqual(GenerateBBSTArray([13]), [13])

    def test_generateBSST(self):
        #          50
        #         /  \
        #      35      55
        #     /  \    /  \
        #   30   40  58   60
        #
        #         into
        #
        #          50
        #         /  \
        #      35      58
        #     /  \    /  \
        #   30   40  55   60

        pseudo_random_arr = [40, 58, 30, 60, 35, 55, 50]
        self.assertEqual(GenerateBBSTArray(pseudo_random_arr), [50, 35, 58, 30, 40, 55, 60])


if __name__ == '__main__':
    unittest.main()
