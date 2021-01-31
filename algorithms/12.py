# наследуйте этот класс от HashTable
# или расширьте его методами из HashTable
class PowerSet:

    def __init__(self):
        # ваша реализация хранилища
        self.pset = []
        self._step = 1

    def size(self):
        # количество элементов в множестве
        return len(self.pset)

    def hash_fun(self, value):
        index = len(str(value).encode('utf-8')) % self.size()
        return index

    def seek_slot(self, value):
        # находит индекс пустого или уже созданного слота для значения, или None
        counter = 0
        index = self.hash_fun(value)
        if self.pset[index] is None:
            return index
        while counter < self.size():
            index = index + self._step
            if index >= self.size():
                index = index - self.size()
            if self.pset[index] is None:
                return index
            if self.pset[index] is value:
                return index
            counter = counter + 1
        return None

    def put(self, value):
        # всегда срабатывает
        if self.size() == 0:
            self.pset.append(value)
        else:
            index = self.seek_slot(value)
            if index is None:
                self.pset.append(value)
            else:
                self.pset[index] = value
        return None

    def get(self, value):
        # возвращает True если value имеется в множестве,
        # иначе False
        if value in self.pset:
            return True
        return False

    def remove(self, value):
        # возвращает True если value удалено
        # иначе False
        try:
            index = self.pset.index(value)
            del self.pset[index]
            return True
        except ValueError:
            return False

    def intersection(self, set2):
        # пересечение текущего множества и set2
        new_pset = PowerSet()

        len_1 = self.size()
        len_2 = set2.size()
        min_len = len_2 if len_1 > len_2 else len_1

        for i in range(min_len):
            if self.pset[i] in set2.pset:
                new_pset.put(self.pset[i])
            if set2.pset[i] in self.pset:
                new_pset.put(set2.pset[i])

        if len_1 > len_2:
            for i in range(min_len, len_1):
                if self.pset[i] in set2.pset:
                    new_pset.put(self.pset[i])
        else:
            for i in range(min_len, len_2):
                if set2.pset[i] in self.pset:
                    new_pset.put(set2.pset[i])

        return new_pset

    def union(self, set2):
        # объединение текущего множества и set2
        new_pset = PowerSet()
        new_pset.pset = self.pset[::]
        for i in set2.pset:
            new_pset.put(i)
        return new_pset

    def difference(self, set2):
        # разница текущего множества и set2
        new_pset = PowerSet()
        for i in self.pset:
            if set2.get(i) is False:
                new_pset.put(i)
        return new_pset

    def issubset(self, set2):
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        for i in set2.pset:
            if self.get(i) is True:
                pass
            else:
                return False
        return True
