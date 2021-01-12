import ctypes
import unittest


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        '''
        5.1. Добавьте метод insert(i, itm), который вставляет в i-ю позицию объект itm, сдвигая вперёд все последующие элементы. Учтите, что новая длина массива может превысить размер буфера.

        В обоих случаях, если индекс i лежит вне допустимых границ, генерируйте исключение.

        Важно, единственное исключение: для метода insert() параметр i может принимать значение, равное длине рабочего массива count, в таком случае добавление происходит в его хвост.
        '''
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')

        if self.count == self.capacity:
            # old index of end of array
            start = self.capacity
            self.resize(2*self.capacity)
        else:
            # old index of end of array
            start = self.count

        while start != i:
            self.array[start] = self.array[start-1]
            start -= 1
        self.array[start] = itm
        self.count += 1

    def delete(self, i):
        '''
        5.2. Добавьте метод delete(i), который удаляет объект из i-й позиции, при необходимости сжимая буфер.

        В обоих случаях, если индекс i лежит вне допустимых границ, генерируйте исключение.
        '''
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')

        old_count = self.count - 1
        old_array = self.array

        if self.capacity >= 16:
            k = (self.count - 1) / self.capacity
            if k < 0.5:
                new_capacity = int(self.capacity / 1.5)
                if new_capacity < 16:
                    new_capacity = 16
                self.resize(new_capacity)

        for index in range(i):
            self.array[index] = old_array[index]
        for index in range(i + 1, old_count + 1):
            self.array[index-1] = old_array[index]

        self.array[old_count] = (ctypes.py_object)()

        self.count -= 1


class TestUM(unittest.TestCase):
    def setUp(self):
        self.da_empty = DynArray()
        self.da = DynArray()
        self.da_full = DynArray()

        for i in range(8):
            self.da.append(i)

        for i in range(16):
            self.da_full.append(i)

    def test_insert_wrong_position(self):
        '''
        -- попытка вставки элемента в недопустимую позицию;
        '''
        self.assertRaises(IndexError, self.da_empty.insert, -1, 777)
        self.assertRaises(IndexError, self.da_empty.insert, 1, 777)

        self.assertRaises(IndexError, self.da.insert, -1, 777)
        self.assertRaises(IndexError, self.da.insert, 9, 777)

        self.assertRaises(IndexError, self.da_full.insert, -1, 777)
        self.assertRaises(IndexError, self.da_full.insert, 17, 777)

    def test_insert(self):
        '''
        -- вставка элемента, когда в итоге размер буфера не превышен (проверьте также размер буфера);
        '''

        self.da_empty.insert(0, 777)
        self.assertEqual(1, len(self.da_empty))
        self.assertEqual(777, self.da_empty[0])
        self.assertRaises(IndexError, self.da_empty.__getitem__, 1)
        self.assertEqual(16, self.da_empty.capacity)

        self.da.insert(4, 777)
        self.assertEqual(9, len(self.da))
        self.assertEqual(777, self.da[4])
        self.assertRaises(IndexError, self.da.__getitem__, 9)
        self.assertEqual(16, self.da.capacity)

    def test_insert_exceeding(self):
        '''
        -- вставка элемента, когда в результате превышен размер буфера (проверьте также корректное изменение размера буфера);
        '''
        for i in range(16):
            self.da_empty.append(i)
        self.da_empty.insert(16, 777)
        self.assertEqual(17, len(self.da_empty))
        self.assertEqual(777, self.da_empty[16])
        self.assertEqual(15, self.da_empty[15])
        self.assertRaises(IndexError, self.da_empty.__getitem__, 17)
        self.assertEqual(32, self.da_empty.capacity)

        for i in range(8+16):
            self.da.append(i)
        self.da.insert(8, 777)
        self.assertEqual(33, len(self.da))
        self.assertEqual(777, self.da[8])
        self.assertEqual(0, self.da[9])
        self.assertEqual(64, self.da.capacity)

        self.da_full.insert(0, 777)
        self.assertEqual(17, len(self.da_full))
        self.assertEqual(777, self.da_full[0])
        self.assertEqual(0, self.da_full[1])
        self.assertEqual(32, self.da_full.capacity)

    def test_delete_wrong_position(self):
        '''
        -- попытка удаления элемента в недопустимой позиции.
        '''

        self.assertRaises(IndexError, self.da_empty.delete, -1)
        self.assertRaises(IndexError, self.da_empty.delete, 0)

        self.assertRaises(IndexError, self.da.delete, -1)
        self.assertRaises(IndexError, self.da.delete, 9)
        self.assertRaises(IndexError, self.da.delete, 18)

        self.assertRaises(IndexError, self.da_full.delete, -1)
        self.assertRaises(IndexError, self.da_full.delete, 17)
        self.assertRaises(IndexError, self.da_full.delete, 20)

    def test_delete(self):
        '''
        -- удаление элемента, когда в результате размер буфера остаётся прежним (проверьте также размер буфера);
        '''

        self.da_empty.append(777)
        self.da_empty.delete(0)
        self.assertEqual(0, len(self.da_empty))
        self.assertRaises(IndexError, self.da_empty.__getitem__, 0)
        self.assertRaises(IndexError, self.da_empty.__getitem__, 1)
        self.assertEqual(16, self.da_empty.capacity)

        self.da.delete(4)
        self.assertEqual(7, len(self.da))
        self.assertEqual(5, self.da[4])
        self.assertRaises(IndexError, self.da.__getitem__, 8)
        self.assertEqual(16, self.da.capacity)

        self.da_full.delete(15)
        self.assertEqual(15, len(self.da_full))
        self.assertEqual(14, self.da_full[14])
        self.assertRaises(IndexError, self.da_full.__getitem__, 15)
        self.assertEqual(16, self.da_full.capacity)

    def test_delete_decreasing(self):
        '''
        -- удаление элемента, когда в результате понижается размер буфера (проверьте также корректное изменение размера буфера);
        '''

        self.da_full.append(777)

        self.da_full.delete(13)
        self.da_full.delete(13)

        self.assertEqual(15, len(self.da_full))
        self.assertEqual(777, self.da_full[14])
        self.assertRaises(IndexError, self.da_full.__getitem__, 15)
        self.assertEqual(21, self.da_full.capacity)


        self.da_empty.resize(79)
        for i in range(46):
            self.da_empty.append(i)

        for i in range(40):
            self.da_empty.delete(len(self.da_empty)-1)

        for i in range(5):
            self.da_empty.delete(0)

        self.assertEqual(1, len(self.da_empty))
        self.assertEqual(16, self.da_empty.capacity)
        self.assertEqual(5, self.da_empty[0])

if __name__ == '__main__':
    unittest.main()
