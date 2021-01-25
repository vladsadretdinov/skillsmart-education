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
