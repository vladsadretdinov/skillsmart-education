import unittest


class NativeDictionary:
    def __init__(self, sz):
        if sz < 1:
            self.size = sz
        else:
            self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        # в качестве key поступают строки!
        # всегда возвращает корректный индекс слота
        key = str(key)
        if self.is_key(key):
            return self.slots.index(key)
        try:
            index = len(key.encode('utf-8')) % self.size
            return index
        except ZeroDivisionError:
            return 0

    def is_key(self, key):
        # возвращает True если ключ имеется,
        # иначе False
        if key in self.slots:
            return True
        return False

    def put(self, key, value):
        # гарантированно записываем
        # значение value по ключу key

        if self.is_key(key):
            index = self.slots.index(key)
            self.values[index] = value
            return None

        counter = 0
        index = self.hash_fun(value)

        while counter < self.size:
            index = index + 1
            if index >= self.size:
                index = index - self.size
            if self.slots[index] is None:
                self.slots[index] = key
                self.values[index] = value
                return None
            counter = counter + 1

        return None

    def get(self, key):
        # возвращает value для key,
        # или None если ключ не найден
        try:
            index = self.slots.index(key)
            return self.values[index]
        except ValueError:
            return None


class TestUM(unittest.TestCase):
    def setUp(self):
        self.native_dict = NativeDictionary(17)

    def test_hash_fun(self):
        self.assertIn(
            self.native_dict.hash_fun('test'),
            range(0, self.native_dict.size)
        )

        self.assertIn(
            self.native_dict.hash_fun('test vlad'),
            range(0, self.native_dict.size)
        )

    def test_is_key(self):
        self.native_dict.slots[4] = "test"
        self.assertEqual(True, self.native_dict.is_key('test'))
        self.native_dict.slots[2] = "vlad"
        self.assertEqual(True, self.native_dict.is_key('vlad'))
        self.assertEqual(False, self.native_dict.is_key('error'))

    def test_put(self):
        self.native_dict.put("test", "vlad")
        self.assertEqual(True, self.native_dict.is_key('test'))

        self.native_dict.put("asdf", "vlad")
        self.assertEqual(True, self.native_dict.is_key('asdf'))

        self.assertEqual(False, self.native_dict.is_key('error'))

    def test_get(self):
        self.native_dict.put("test", "vlad")
        self.assertEqual("vlad", self.native_dict.get('test'))

        self.native_dict.put("test2", "vlad2")
        self.assertEqual("vlad2", self.native_dict.get('test2'))

        self.native_dict.put("test2", "vlad3")
        self.assertEqual("vlad3", self.native_dict.get('test2'))

        self.assertEqual(None, self.native_dict.get('test3'))

        self.native_dict.put("test2", "vlad4")
        self.assertEqual("vlad4", self.native_dict.get('test2'))
        self.native_dict.put("test2", "vlad4")
        self.assertEqual("vlad4", self.native_dict.get('test2'))

    def test_overwrite(self):
        for i in range(0, 100):
            self.native_dict.put("test1", "vlad1")
            self.assertEqual(
                "vlad1",
                self.native_dict.get("test1")
            )
        self.assertEqual(2, len(set(self.native_dict.slots)))
        self.assertEqual(2, len(set(self.native_dict.values)))

        self.assertEqual(
            "vlad1",
            self.native_dict.get("test1")
        )

        for i in range(0, 17):
            self.native_dict.put("test1", "vlad2")
        self.assertEqual(2, len(set(self.native_dict.slots)))
        self.assertEqual(2, len(set(self.native_dict.values)))

        for i in range(0, 17):
            self.native_dict.put("test" + str(i), "vlad" + str(i))

        for i in range(0, 17):
            self.assertEqual(
                "vlad" + str(i),
                self.native_dict.get("test" + str(i))
            )

        self.native_dict.put("test5", "5vlad")
        self.assertEqual("5vlad", self.native_dict.get('test5'))

        for i in range(0, 17):
            self.assertEqual(True, self.native_dict.is_key("test" + str(i)))

        self.native_dict.put("test 5", "5 vlad")
        self.assertEqual(None, self.native_dict.get('test 5'))

        self.assertEqual(17, len(set(self.native_dict.slots)))
        self.assertEqual(17, len(set(self.native_dict.values)))

        self.native_dict.put("test5", "vlad6")
        self.assertEqual("vlad6", self.native_dict.get('test5'))
        self.assertEqual(17, len(set(self.native_dict.slots)))
        self.assertEqual(16, len(set(self.native_dict.values)))

    def test_small_size(self):
        self.native_dict = NativeDictionary(1)
        self.native_dict.put("test1", "vlad1")
        self.assertEqual('vlad1', self.native_dict.get('test1'))

        self.native_dict.put("test1", "vlad2")
        self.assertEqual('vlad2', self.native_dict.get('test1'))

        self.native_dict.put("test2", "vlad3")
        self.assertEqual(None, self.native_dict.get('test2'))

    def test_zero_native_dict(self):
        zero_native_dict = NativeDictionary(0)
        zero_native_dict.put('test', 'vlad')
        self.assertEqual(None, zero_native_dict.get('test'))
        self.assertEqual(0, len(set(zero_native_dict.slots)))
        self.assertEqual(0, len(set(zero_native_dict.values)))

    def test_zero_native_dict1(self):
        zero_native_dict = NativeDictionary(-10)
        zero_native_dict.put('test', 'vlad')
        self.assertEqual(None, zero_native_dict.get('test'))
        self.assertEqual(0, len(set(zero_native_dict.slots)))
        self.assertEqual(0, len(set(zero_native_dict.values)))

    def test_by_mater(self):
        for i in range(100):
            self.native_dict.put(i, 123456789)
        pass


if __name__ == '__main__':
    unittest.main()
