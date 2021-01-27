class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        # в качестве key поступают строки!
        # всегда возвращает корректный индекс слота
        if self.is_key(key):
            return self.slots.index(key)
        index = len(key.encode('utf-8')) % self.size
        return index

    def is_key(self, key):
        # возвращает True если ключ имеется,
        # иначе False
        if key in self.slots:
            return True
        return False

    def put(self, key, value):
        # гарантированно записываем
        # значение value по ключу key
        counter = 0
        index = self.hash_fun(value)

        if self.is_key(key):
            self.slots[index] = key
            self.values[index] = value
            return None
        while counter < self.size:
            index = index + 3
            if index >= self.size:
                index = index - self.size
            if self.slots[index] == key:
                self.values[index] = value
                return None
            elif self.slots[index] is None:
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
