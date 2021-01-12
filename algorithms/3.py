import ctypes


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
