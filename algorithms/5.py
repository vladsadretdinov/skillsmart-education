class Queue:
    def __init__(self):
        # инициализация хранилища данных
        self.queue = []

    def enqueue(self, item):
        # вставка в хвост
        self.queue.append(item)

    def dequeue(self):
        # выдача из головы
        if self.size() == 0:
            return None
        return self.queue.pop(0)

    def size(self):
        # размер очереди
        return len(self.queue)
