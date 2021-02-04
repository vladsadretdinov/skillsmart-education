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
