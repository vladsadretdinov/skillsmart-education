import unittest

from heap import Heap


class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def test_make_heap_depth(self):
        self.heap = Heap()
        self.heap.MakeHeap([1], 0)
        self.assertEqual(len(self.heap.HeapArray), 1)

        self.heap = Heap()
        self.heap.MakeHeap([1, 2, 3], 1)
        self.assertEqual(len(self.heap.HeapArray), 3)

        self.heap = Heap()
        self.heap.MakeHeap([1, 2, 3, 4, 5, 6, 7], 2)
        self.assertEqual(len(self.heap.HeapArray), 7)

        self.heap = Heap()
        self.heap.MakeHeap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 3)
        self.assertEqual(len(self.heap.HeapArray), 15)

        self.heap = Heap()
        self.heap.MakeHeap([1, 2, 3, 4, 5], 1)
        self.assertEqual(len(self.heap.HeapArray), 3)
        self.assertEqual(self.heap.HeapArray, [3, 1, 2])

    def test_add(self):
        self.heap = Heap()
        self.heap.MakeHeap([11, 9, 4, 7, 8, 3, 1, 2, 5, 6], 3)
        self.assertEqual(len(self.heap.HeapArray), 15)
        self.assertEqual(self.heap.Add(10), True)
        self.assertEqual(len(self.heap.HeapArray), 15)
        self.assertEqual(self.heap.HeapArray, [11, 10, 4, 7, 9, 3, 1, 2, 5, 6, 8, None, None, None, None])

        self.assertEqual(self.heap.Add(15), True)
        self.assertEqual(self.heap.HeapArray, [15, 10, 11, 7, 9, 4, 1, 2, 5, 6, 8, 3, None, None, None])

        self.assertEqual(self.heap.Add(13), True)
        self.assertEqual(self.heap.HeapArray, [15, 10, 13, 7, 9, 11, 1, 2, 5, 6, 8, 3, 4, None, None])

        self.assertEqual(self.heap.Add(12), True)
        self.assertEqual(self.heap.HeapArray, [15, 10, 13, 7, 9, 11, 12, 2, 5, 6, 8, 3, 4, 1, None])

        self.assertEqual(self.heap.Add(14), True)
        self.assertEqual(self.heap.HeapArray, [15, 10, 14, 7, 9, 11, 13, 2, 5, 6, 8, 3, 4, 1, 12])

        self.assertEqual(self.heap.Add(777), False)
        self.assertEqual(self.heap.HeapArray, [15, 10, 14, 7, 9, 11, 13, 2, 5, 6, 8, 3, 4, 1, 12])

        self.heap = Heap()
        self.heap.MakeHeap([11, 9, 4, 7, 8, 3, 1, 2, 5, 6], 1)
        self.assertEqual(self.heap.HeapArray, [11, 9, 4])
        self.assertEqual(self.heap.Add(777), False)

        self.heap = Heap()
        self.heap.MakeHeap([11, 9, 4, 7, 8, 3, 1, 2, 5, 6], 0)
        self.assertEqual(self.heap.HeapArray, [11])
        self.assertEqual(self.heap.Add(777), False)

        self.heap = Heap()
        self.heap.MakeHeap([], 0)
        self.assertEqual(self.heap.HeapArray, [None])
        self.assertEqual(self.heap.Add(777), True)
        self.assertEqual(self.heap.HeapArray, [777])

    def test_get_max(self):
        self.heap = Heap()
        self.heap.MakeHeap([777], 0)
        self.assertEqual(self.heap.GetMax(), 777)
        self.assertEqual(self.heap.GetMax(), -1)

        self.heap = Heap()
        self.heap.MakeHeap([11, 9, 4, 7, 8, 3, 1, 2, 5, 6], 3)

        self.assertEqual(self.heap.GetMax(), 11)
        self.assertEqual(
            self.heap.HeapArray,
            [9, 8, 4, 7, 6, 3, 1, 2, 5, None, None, None, None, None, None],
        )

        self.assertEqual(self.heap.GetMax(), 9)
        self.assertEqual(
            self.heap.HeapArray,
            [8, 7, 4, 5, 6, 3, 1, 2, None, None, None, None, None, None, None],
        )

        self.assertEqual(self.heap.GetMax(), 8)
        self.assertEqual(
            self.heap.HeapArray,
            [7, 6, 4, 5, 2, 3, 1, None, None, None, None, None, None, None, None],
        )

        self.assertEqual(self.heap.GetMax(), 7)
        self.assertEqual(
            self.heap.HeapArray,
            [6, 5, 4, 1, 2, 3, None, None, None, None, None, None, None, None, None],
        )

        self.assertEqual(self.heap.GetMax(), 6)
        self.assertEqual(
            self.heap.HeapArray,
            [5, 3, 4, 1, 2, None, None, None, None, None, None, None, None, None, None],
        )

        self.assertEqual(self.heap.GetMax(), 5)
        self.assertEqual(
            self.heap.HeapArray,
            [4, 3, 2, 1, None, None, None, None, None, None, None, None, None, None, None],
        )

        self.assertEqual(self.heap.GetMax(), 4)
        self.assertEqual(
            self.heap.HeapArray,
            [3, 1, 2, None, None, None, None, None, None, None, None, None, None, None, None],
        )

        self.assertEqual(self.heap.GetMax(), 3)
        self.assertEqual(
            self.heap.HeapArray,
            [2, 1, None, None, None, None, None, None, None, None, None, None, None, None, None],
        )

        self.assertEqual(self.heap.GetMax(), 2)
        self.assertEqual(
            self.heap.HeapArray,
            [1, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        )

        self.assertEqual(self.heap.GetMax(), 1)
        self.assertEqual(
            self.heap.HeapArray,
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        )

        self.assertEqual(self.heap.GetMax(), -1)
        self.assertEqual(
            self.heap.HeapArray,
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        )
        self.assertEqual(len(self.heap.HeapArray), 15)


if __name__ == "__main__":
    unittest.main()
