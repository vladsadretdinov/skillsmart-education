import unittest

# Например, если мы делаем последовательно push(1), push(2) и push(3) для исходно пустого стека,
# то вызовы pop() вернут 3, потом 2, и потом 1. Сам стек в итоге снова окажется пустым.

# Переделайте реализацию стека так, чтобы она работала не с хвостом списка как с верхушкой стека, а с его головой.

class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        # Операция pop извлекает последний втолкнутый в стек элемент
        if self.size() == 0:
            return None
        return self.stack.pop(0)

    def push(self, value):
        # Операция push помещает элемент в этот вход -- говорят, на самый верх стека.
        self.stack.insert(0, value)
        return None

    def peek(self):
        # peek() -- получить верхний элемент стека, но не удалять его.
        length = self.size()
        if length == 0:
            return None
        return self.stack[0]

    def __getitem__(self, i):
        if i < 0 or i >= self.size():
            raise IndexError('Index is out of bounds')
        return self.stack[i]


class TestUM(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_len(self):
        self.assertEqual(0, self.stack.size())

        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        self.assertEqual(3, self.stack.size())

        self.stack.pop()
        self.stack.pop()

        self.assertEqual(1, self.stack.size())

    def test_push(self):
        self.assertEqual(0, self.stack.size())

        self.stack.push(1)
        self.assertEqual(1, self.stack[0])
        self.assertEqual(1, self.stack.size())

        self.stack.push(2)
        self.assertEqual(2, self.stack[0])
        self.assertEqual(2, self.stack.size())

        self.stack.push('vlad')
        self.assertEqual('vlad', self.stack[0])
        self.assertEqual(3, self.stack.size())

    def test_pop(self):
        self.assertEqual(0, self.stack.size())
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push('vlad')

        self.assertEqual('vlad', self.stack.pop())
        self.assertEqual(2, self.stack.size())

        self.assertEqual(2, self.stack.pop())
        self.assertEqual(1, self.stack.size())

        self.assertEqual(1, self.stack.pop())
        self.assertEqual(0, self.stack.size())

        self.assertEqual(None, self.stack.pop())
        self.assertEqual(0, self.stack.size())

        self.assertEqual(None, self.stack.pop())
        self.assertEqual(0, self.stack.size())

    def test_peek(self):
        self.assertEqual(0, self.stack.size())

        self.stack.push(1)
        self.assertEqual(1, self.stack.peek())
        self.assertEqual(1, self.stack.size())

        self.stack.push(2)
        self.assertEqual(2, self.stack.peek())
        self.assertEqual(2, self.stack.size())

        self.stack.push('vlad')
        self.assertEqual('vlad', self.stack.peek())
        self.assertEqual(3, self.stack.size())

if __name__ == '__main__':
    unittest.main()
