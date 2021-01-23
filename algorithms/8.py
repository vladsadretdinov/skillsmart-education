class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        # -1 если v1 < v2
        # 0 если v1 == v2
        # +1 если v1 > v2
        if v1 < v2:
            return -1
        if v1 == v2:
            return 0
        return 1

    def add(self, value):
        # автоматическая вставка value
        # в нужную позицию

        item = Node(value)

        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
            self.tail = item
        else:
            # встать в начало списка
            itr = self.head

            # итерироваться пока не конец списка
            while itr is not None:
                compared = self.compare(value, itr.value)
                if self.__ascending is True:
                    if compared == 1:
                        if itr.next is not None:
                            itr.next.prev = item
                            item.next = itr.next
                            item.prev = itr
                            itr.next = item
                        else:
                            item.prev = self.tail
                            self.tail.next = item
                            self.tail = item
                        return None
                    elif compared <= 0:
                        pass
                    itr = itr.next
                else:
                    if compared == 1:
                        if itr.prev is not None:
                            itr.prev.next = item
                            item.prev = itr.prev
                            item.next = itr
                            itr.prev = item
                        else:
                            self.head = item
                            self.head.next = itr
                            itr.prev = item
                        return None
                    elif compared <= 0:
                        pass
                    itr = itr.next

            item.prev = self.tail
            self.tail.next = item
            self.tail = item

        return None

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def delete(self, val):
        # если список пустой то сразу выйти
        if self.head is None:
            return None

        # встать в начало списка
        itr = self.head
        prev = itr.prev

        # итерироваться пока не конец списка
        while itr is not None:
            if itr.value == val:
                # если это первый элемент то сместить голову
                if itr is self.head:
                    self.head = itr.next
                    # если всего был один элемент - очистить и хвост
                    if itr is self.tail:
                        self.tail = None
                    # если нет то очистить пред значение для головы
                    else:
                        self.head.prev = None
                else:
                    if itr is self.tail:
                        self.tail = itr.prev
                    else:
                        itr.next.prev = prev
                    prev.next = itr.next

                return None

            prev = itr
            itr = itr.next

        return None

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None
        return None

    def len(self):
        # если список пустой то сразу выйти
        if self.head is None:
            return 0

        # встать в начало списка
        itr = self.head
        count = 0

        # итерироваться пока не конец списка
        while itr is not None:
            itr = itr.next
            count = count + 1

        return count

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        # переопределённая версия для строк
        clean_v1 = v1.strip()
        clean_v2 = v2.strip()
        if clean_v1 < clean_v2:
            return -1
        if clean_v1 == clean_v2:
            return 0
        return 1
