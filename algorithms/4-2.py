class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        # Операция pop извлекает последний втолкнутый в стек элемент
        if self.size() == 0:
            return None
        return self.stack.pop(0)

    def push(self, value):
        # Операция push помещает элемент в этот вход -- говорят, на самый верх стека.
        self.stack.insert(0, value)
        return None

    def peek(self):
        # peek() -- получить верхний элемент стека, но не удалять его.
        length = self.size()
        if length == 0:
            return None
        return self.stack[0]
