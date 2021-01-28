import unittest


class BloomFilter:
    def __init__(self, f_len):
        # создаём битовый массив длиной f_len ...
        self.filter_len = f_len
        self.arr = [False] * f_len

    def hash1(self, str1):
        # 17
        res = 0
        for c in str1:
            code = ord(c)
            res = (res * 17) + code
            res = res % self.filter_len
        return res

    def hash2(self, str1):
        # 223
        res = 0
        for c in str1:
            code = ord(c)
            res = (res * 223) + code
            res = res % self.filter_len
        return res

    def add(self, str1):
        # добавляем строку str1 в фильтр
        index1 = self.hash1(str1)
        index2 = self.hash2(str1)

        self.arr[index1] = True
        self.arr[index2] = True

    def is_value(self, str1):
        # проверка, имеется ли строка str1 в фильтре
        index1 = self.hash1(str1)
        index2 = self.hash2(str1)

        if index1 & index2:
            return True
        return False


class TestUM(unittest.TestCase):
    def test(self):
        numbers = BloomFilter(10)
        numbers.add('0123456789')
        self.assertEqual(True, numbers.is_value('0123456789'))
        numbers.add('1234567890')
        self.assertEqual(True, numbers.is_value('1234567890'))
        numbers.add('2345678910')
        self.assertEqual(True, numbers.is_value('2345678910'))
        numbers.add('3456789012')
        self.assertEqual(True, numbers.is_value('3456789012'))
        numbers.add('4567890123')
        self.assertEqual(True, numbers.is_value('4567890123'))
        numbers.add('5678901234')
        self.assertEqual(True, numbers.is_value('5678901234'))
        numbers.add('6789012345')
        self.assertEqual(True, numbers.is_value('6789012345'))
        numbers.add('7890123456')
        self.assertEqual(True, numbers.is_value('7890123456'))
        numbers.add('8901234567')
        self.assertEqual(True, numbers.is_value('8901234567'))
        numbers.add('9012345678')
        self.assertEqual(True, numbers.is_value('9012345678'))
        self.assertEqual(True, numbers.is_value('90123456780'))
        self.assertEqual(False, numbers.is_value('1112345678'))


if __name__ == '__main__':
    unittest.main()
