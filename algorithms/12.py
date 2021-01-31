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

    def put(self, value):
        # всегда срабатывает
        if value in self.pset:
            return None
        else:
            self.pset.append(value)
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
        for i in self.pset:
            if i in set2.pset:
                new_pset.put(i)
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
