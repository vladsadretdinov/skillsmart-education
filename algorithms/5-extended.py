import unittest


class Queue:
    def __init__(self):
        # инициализация хранилища данных
        self.queue = []

    def enqueue(self, item):
        # вставка в хвост
        self.queue.append(item)

    def dequeue(self):
        # выдача из головы
        if self.size() == 0:
            return None
        return self.queue.pop(0)

    def size(self):
        # размер очереди
        return len(self.queue)

    def __getitem__(self, i):
        if i < 0 or i >= self.size():
            raise IndexError('Index is out of bounds')
        return self.queue[i]


class TestUM(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_len(self):
        self.assertEqual(0, self.queue.size())

        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

        self.assertEqual(3, self.queue.size())

        self.queue.dequeue()
        self.queue.dequeue()

        self.assertEqual(1, self.queue.size())

    def test_enqueue(self):
        self.assertEqual(0, self.queue.size())

        self.queue.enqueue(1)
        self.assertEqual(1, self.queue[0])
        self.assertEqual(1, self.queue.size())

        self.queue.enqueue(2)
        self.assertEqual(2, self.queue[1])
        self.assertEqual(2, self.queue.size())

        self.queue.enqueue('vlad')
        self.assertEqual('vlad', self.queue[2])
        self.assertEqual(3, self.queue.size())

    def test_dequeue(self):
        self.assertEqual(0, self.queue.size())
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue('vlad')

        self.assertEqual(1, self.queue.dequeue())
        self.assertEqual(2, self.queue.size())

        self.assertEqual(2, self.queue.dequeue())
        self.assertEqual(1, self.queue.size())

        self.assertEqual('vlad', self.queue.dequeue())
        self.assertEqual(0, self.queue.size())

        self.assertEqual(None, self.queue.dequeue())
        self.assertEqual(0, self.queue.size())

        self.assertEqual(None, self.queue.dequeue())
        self.assertEqual(0, self.queue.size())


if __name__ == '__main__':
    unittest.main()
