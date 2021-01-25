import unittest


class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        # в качестве value поступают строки!
        # всегда возвращает корректный индекс слота
        index = len(value.encode('utf-8')) % self.size
        return index

    def seek_slot(self, value):
        # находит индекс пустого слота для значения, или None
        counter = 0
        index = self.hash_fun(value)
        if self.slots[index] is None:
            return index
        while counter < self.size:
            index = index + self.step
            if index >= self.size:
                index = index - self.size
            if self.slots[index] is None:
                return index
            counter = counter + 1
        return None

    def put(self, value):
        # записываем значение по хэш-функции

        # возвращается индекс слота или None,
        # если из-за коллизий элемент не удаётся
        # разместить

        index = self.seek_slot(value)
        if index is None:
            return None
        else:
            self.slots[index] = value
        return index

    def find(self, value):
        # находит индекс слота со значением, или None
        for i in range(len(self.slots)):
            if self.slots[i] == value:
                return i
        return None


class TestUM(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable(17, 3)

    def test_hash_fun(self):
        self.assertEqual(4, self.hash_table.hash_fun('test'))
        self.assertIn(
            self.hash_table.hash_fun('test'),
            range(0, self.hash_table.size)
        )

        self.assertEqual(9, self.hash_table.hash_fun('test vlad'))
        self.assertIn(
            self.hash_table.hash_fun('test vlad'),
            range(0, self.hash_table.size)
        )

    def test_seek_slot(self):
        self.assertEqual(4, self.hash_table.seek_slot('test'))
        self.hash_table.slots[4] = "test"
        self.assertEqual(7, self.hash_table.seek_slot('test'))

        for i in range(0, 17):
            self.hash_table.slots[i] = "value"
        self.assertEqual(None, self.hash_table.seek_slot('test'))

    def test_put(self):
        self.assertEqual(4, self.hash_table.put("test"))
        self.assertEqual("test", self.hash_table.slots[4])

        for _i in range(0, 16):
            self.assertNotEqual(None, self.hash_table.put("test"))

        for i in self.hash_table.slots:
            self.assertEqual("test", i)

        self.assertEqual(None, self.hash_table.put("test"))

    def test_find(self):
        self.hash_table.put("test")
        self.assertEqual(4, self.hash_table.find("test"))

        self.hash_table.put("vlad")
        self.assertEqual(7, self.hash_table.find("vlad"))

        self.assertEqual(None, self.hash_table.find("none"))


if __name__ == '__main__':
    unittest.main()
