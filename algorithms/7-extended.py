import unittest


class Deque:
    def __init__(self):
        # инициализация внутреннего хранилища
        self.deque = []

    def addFront(self, item):
        # добавление в голову
        self.deque.insert(0, item)

    def addTail(self, item):
        # добавление в хвост
        self.deque.append(item)

    def removeFront(self):
        # удаление из головы
        if self.size() == 0:
            return None
        return self.deque.pop(0)

    def removeTail(self):
        # удаление из хвоста
        if self.size() == 0:
            return None
        return self.deque.pop()

    def size(self):
        # размер очереди
        return len(self.deque)

    def __getitem__(self, i):
        if i < 0 or i >= self.size():
            raise IndexError('Index is out of bounds')
        return self.deque[i]


class TestUM(unittest.TestCase):
    def setUp(self):
        self.deque = Deque()

    def test_addFront(self):
        self.assertEqual(0, self.deque.size())

        self.deque.addFront(1)
        self.deque.addFront(2)
        self.deque.addFront(3)

        self.assertEqual(3, self.deque.size())

        self.assertEqual(3, self.deque[0])
        self.assertEqual(2, self.deque[1])
        self.assertEqual(1, self.deque[2])

    def test_addTail(self):
        self.assertEqual(0, self.deque.size())

        self.deque.addTail(1)
        self.deque.addTail(2)
        self.deque.addTail(3)

        self.assertEqual(3, self.deque.size())

        self.assertEqual(1, self.deque[0])
        self.assertEqual(2, self.deque[1])
        self.assertEqual(3, self.deque[2])

    def test_removeFront(self):
        self.assertEqual(0, self.deque.size())

        self.assertEqual(None, self.deque.removeFront())
        self.assertEqual(0, self.deque.size())

        self.deque.addTail(1)
        self.deque.addTail(2)
        self.deque.addTail(3)

        self.assertEqual(1, self.deque.removeFront())
        self.assertEqual(2, self.deque.size())

        self.assertEqual(2, self.deque.removeFront())
        self.assertEqual(1, self.deque.size())

        self.assertEqual(3, self.deque.removeFront())
        self.assertEqual(0, self.deque.size())

        self.assertEqual(None, self.deque.removeFront())
        self.assertEqual(0, self.deque.size())

    def test_removeTail(self):
        self.assertEqual(0, self.deque.size())

        self.assertEqual(None, self.deque.removeTail())
        self.assertEqual(0, self.deque.size())

        self.deque.addTail(1)
        self.deque.addTail(2)
        self.deque.addTail(3)

        self.assertEqual(3, self.deque.removeTail())
        self.assertEqual(2, self.deque.size())

        self.assertEqual(2, self.deque.removeTail())
        self.assertEqual(1, self.deque.size())

        self.assertEqual(1, self.deque.removeTail())
        self.assertEqual(0, self.deque.size())

        self.assertEqual(None, self.deque.removeTail())
        self.assertEqual(0, self.deque.size())


if __name__ == '__main__':
    unittest.main()
