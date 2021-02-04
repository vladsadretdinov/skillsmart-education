import unittest


class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        # всегда возвращает корректный индекс слота
        key = str(key)
        if self.is_key(key):
            return self.slots.index(key)
        try:
            index = len(key.encode('utf-8')) % self.size
            return index
        except ZeroDivisionError:
            return 0

    def _find_unpopular_key(self):
        return self.hits.index(min(self.hits))

    def is_key(self, key):
        # возвращает True если ключ имеется,
        # иначе False
        if key in self.slots:
            return True
        return False

    def put(self, key, value):
        # гарантированно записываем
        # значение value по ключу key

        if self.size <= 0:
            return None

        if self.is_key(key):
            index = self.slots.index(key)
            self.values[index] = value
            return None

        counter = 0
        index = self.hash_fun(key)

        while counter < self.size:
            index = index + 1
            if index >= self.size:
                index = index - self.size
            if self.slots[index] is None:
                self.slots[index] = key
                self.values[index] = value
                return None
            counter = counter + 1

        index = self._find_unpopular_key()
        self.slots[index] = key
        self.values[index] = value
        self.hits[index] = 0

        return None

    def get(self, key):
        # возвращает value для key,
        # или None если ключ не найден
        index = self.get_key_index(key)

        if index is None:
            return None

        self.hits[index] += 1
        return self.values[index]

    def get_key_index(self, key):
        # возвращает индекс ключа,
        # или None если ключ не найден
        try:
            return self.slots.index(key)
        except ValueError:
            return None


class TestUM(unittest.TestCase):
    def setUp(self):
        self.native_cache = NativeCache(17)

    def test_hash_fun(self):
        self.assertIn(
            self.native_cache.hash_fun('test'),
            range(0, self.native_cache.size)
        )

        self.assertIn(
            self.native_cache.hash_fun('test vlad'),
            range(0, self.native_cache.size)
        )

    def test_is_key(self):
        self.native_cache.slots[4] = "test"
        self.assertEqual(True, self.native_cache.is_key('test'))
        self.native_cache.slots[2] = "vlad"
        self.assertEqual(True, self.native_cache.is_key('vlad'))
        self.assertEqual(False, self.native_cache.is_key('error'))

    def test_find_unpopular_key(self):
        for i in range(10):
            self.native_cache.hits[i] = 5
        self.assertEqual(10, self.native_cache._find_unpopular_key())

        for i in range(7, 15):
            self.native_cache.hits[i] = 3
        self.assertEqual(15, self.native_cache._find_unpopular_key())

        self.native_cache.hits[15] = 4
        self.native_cache.hits[16] = 4
        self.assertEqual(7, self.native_cache._find_unpopular_key())

    def test_get(self):
        self.native_cache.put("test", "vlad")
        self.assertEqual(
            0, self.native_cache.hits[self.native_cache.get_key_index('test')]
        )
        self.assertEqual("vlad", self.native_cache.get('test'))
        self.assertEqual(
            1, self.native_cache.hits[self.native_cache.get_key_index('test')]
        )
        self.assertEqual("vlad", self.native_cache.get('test'))
        self.assertEqual("vlad", self.native_cache.get('test'))
        self.assertEqual("vlad", self.native_cache.get('test'))
        self.assertEqual(
            4, self.native_cache.hits[self.native_cache.get_key_index('test')]
        )

        self.native_cache.put("test2", "vlad2")
        self.assertEqual("vlad2", self.native_cache.get('test2'))

        self.native_cache.put("test2", "vlad3")
        self.assertEqual("vlad3", self.native_cache.get('test2'))

        self.assertEqual(None, self.native_cache.get('test3'))

        self.native_cache.put("test2", "vlad4")
        self.assertEqual("vlad4", self.native_cache.get('test2'))
        self.native_cache.put("test2", "vlad4")
        self.assertEqual("vlad4", self.native_cache.get('test2'))

    def test_small_size(self):
        self.native_cache = NativeCache(1)
        self.native_cache.put("test1", "vlad1")
        self.assertEqual('vlad1', self.native_cache.get('test1'))

        self.native_cache.put("test1", "vlad2")
        self.assertEqual('vlad2', self.native_cache.get('test1'))

        self.native_cache.put("test2", "vlad3")
        self.assertEqual('vlad3', self.native_cache.get('test2'))

    def test_zero_native_cache(self):
        zero_native_cache = NativeCache(0)
        zero_native_cache.put('test', 'vlad')
        self.assertEqual(None, zero_native_cache.get('test'))
        self.assertEqual(0, len(set(zero_native_cache.slots)))
        self.assertEqual(0, len(set(zero_native_cache.values)))

    def test_zero_native_cache1(self):
        zero_native_cache = NativeCache(-10)
        zero_native_cache.put('test', 'vlad')
        self.assertEqual(None, zero_native_cache.get('test'))
        self.assertEqual(0, len(set(zero_native_cache.slots)))
        self.assertEqual(0, len(set(zero_native_cache.values)))

    def test_overwrite(self):
        for i in range(0, 100):
            self.native_cache.put("test1", "vlad1")
            self.assertEqual(
                "vlad1",
                self.native_cache.get("test1")
            )
        self.assertEqual(2, len(set(self.native_cache.slots)))
        self.assertEqual(2, len(set(self.native_cache.values)))

        self.assertEqual(
            "vlad1",
            self.native_cache.get("test1")
        )

        for i in range(0, 17):
            self.native_cache.put("test1", "vlad2")
        self.assertEqual(2, len(set(self.native_cache.slots)))
        self.assertEqual(2, len(set(self.native_cache.values)))

        for i in range(0, 17):
            self.native_cache.put("test" + str(i), "vlad" + str(i))

        for i in range(0, 17):
            self.assertEqual(
                "vlad" + str(i),
                self.native_cache.get("test" + str(i))
            )

        self.native_cache.put("test5", "5vlad")
        self.assertEqual("5vlad", self.native_cache.get('test5'))

        for i in range(0, 17):
            self.assertEqual(True, self.native_cache.is_key("test" + str(i)))

        self.native_cache.put("test 5", "5 vlad")
        self.assertEqual('5 vlad', self.native_cache.get('test 5'))

        self.assertEqual(17, len(set(self.native_cache.slots)))
        self.assertEqual(17, len(set(self.native_cache.values)))

        self.native_cache.put("test5", "vlad6")
        self.assertEqual("vlad6", self.native_cache.get('test5'))
        self.assertEqual(17, len(set(self.native_cache.slots)))
        self.assertEqual(16, len(set(self.native_cache.values)))

    def test_rewrite_unpopular_key(self):
        for i in range(0, 17):
            self.native_cache.put("test" + str(i), "vlad" + str(i))

        for i in range(0, 16):
            self.assertEqual(
                "vlad" + str(i),
                self.native_cache.get("test" + str(i))
            )
            self.assertEqual(
                1,
                self.native_cache.hits[
                    self.native_cache.get_key_index("test" + str(i))
                ]
            )

        self.assertEqual(
            0,
            self.native_cache.hits[
                self.native_cache.get_key_index("test16")
            ]
        )

        self.assertEqual(17, len(set(self.native_cache.slots)))
        self.assertEqual(17, len(set(self.native_cache.values)))

        self.native_cache.put('key', 'value')
        for i in range(0, 16):
            self.assertEqual(
                "vlad" + str(i),
                self.native_cache.get("test" + str(i))
            )
            self.assertEqual(
                2,
                self.native_cache.hits[
                    self.native_cache.get_key_index("test" + str(i))
                ]
            )

        self.assertEqual(None, self.native_cache.get_key_index("test16"))
        self.assertEqual(
            0,
            self.native_cache.hits[
                self.native_cache.get_key_index("key")
            ]
        )


if __name__ == '__main__':
    unittest.main()
