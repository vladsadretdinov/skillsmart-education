import unittest


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
            if self.__ascending is True:
                itr = self.tail
                while itr is not None:
                    compared = self.compare(value, itr.value)
                    if compared >= 0:
                        item.next = itr.next

                        if itr is self.tail:
                            self.tail = item
                        else:
                            itr.next.prev = item

                        item.prev = itr
                        itr.next = item

                        return None
                    else:
                        itr = itr.prev

                self.head.prev = item
                item.next = self.head
                self.head = item

            else:
                itr = self.head
                while itr is not None:
                    compared = self.compare(value, itr.value)
                    if compared >= 0:
                        item.prev = itr.prev

                        if itr is self.head:
                            self.head = item
                        else:
                            itr.prev.next = item

                        item.next = itr
                        itr.prev = item

                        return None
                    else:
                        itr = itr.next

                self.tail.next = item
                item.prev = self.tail
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


class TestUM(unittest.TestCase):
    def setUp(self):
        self.upward_list = OrderedList(True)
        self.downward_list = OrderedList(False)

    def test_add(self):
        ### UPWARD LIST ###
        self.assertEqual(0, self.upward_list.len())

        self.upward_list.add(10)
        self.assertEqual(1, self.upward_list.len())
        self.assertEqual(10, self.upward_list.head.value)
        self.assertEqual(10, self.upward_list.tail.value)
        self.assertEqual(None, self.upward_list.head.prev)
        self.assertEqual(None, self.upward_list.head.next)

        self.upward_list.add(12)
        self.assertEqual(2, self.upward_list.len())
        self.assertEqual(None, self.upward_list.head.prev)
        self.assertEqual(10, self.upward_list.head.value)
        self.assertEqual(12, self.upward_list.head.next.value)

        self.assertEqual(None, self.upward_list.tail.next)
        self.assertEqual(12, self.upward_list.tail.value)
        self.assertEqual(10, self.upward_list.tail.prev.value)

        self.upward_list.add(11)
        self.assertEqual(3, self.upward_list.len())
        self.assertEqual(None, self.upward_list.head.prev)
        self.assertEqual(10, self.upward_list.head.value)
        self.assertEqual(11, self.upward_list.head.next.value)

        self.assertEqual(None, self.upward_list.tail.next)
        self.assertEqual(12, self.upward_list.tail.value)
        self.assertEqual(11, self.upward_list.tail.prev.value)

        self.upward_list.add(11)
        self.assertEqual(4, self.upward_list.len())
        self.assertEqual(None, self.upward_list.head.prev)
        self.assertEqual(10, self.upward_list.head.value)
        self.assertEqual(11, self.upward_list.head.next.value)
        self.assertEqual(11, self.upward_list.head.next.next.value)

        self.assertEqual(None, self.upward_list.tail.next)
        self.assertEqual(12, self.upward_list.tail.value)
        self.assertEqual(11, self.upward_list.tail.prev.value)
        self.assertEqual(11, self.upward_list.tail.prev.prev.value)

        self.upward_list.add(9)
        self.upward_list.add(8)
        self.upward_list.add(11)
        self.upward_list.add(7)
        self.upward_list.add(12)
        self.assertEqual(
            [7, 8, 9, 10, 11, 11, 11, 12, 12],
            [x.value for x in self.upward_list.get_all()]
        )
        ### UPWARD LIST ###

        ### DOWNWARD LIST ###
        self.assertEqual(0, self.downward_list.len())

        self.downward_list.add(10)
        self.assertEqual(1, self.downward_list.len())
        self.assertEqual(10, self.downward_list.head.value)
        self.assertEqual(10, self.downward_list.tail.value)
        self.assertEqual(None, self.downward_list.head.prev)
        self.assertEqual(None, self.downward_list.head.next)

        self.downward_list.add(12)
        self.assertEqual(2, self.downward_list.len())
        self.assertEqual(None, self.downward_list.head.prev)
        self.assertEqual(12, self.downward_list.head.value)
        self.assertEqual(10, self.downward_list.head.next.value)

        self.assertEqual(None, self.downward_list.tail.next)
        self.assertEqual(10, self.downward_list.tail.value)
        self.assertEqual(12, self.downward_list.tail.prev.value)

        self.downward_list.add(11)
        self.assertEqual(3, self.downward_list.len())
        self.assertEqual(None, self.downward_list.head.prev)
        self.assertEqual(12, self.downward_list.head.value)
        self.assertEqual(11, self.downward_list.head.next.value)

        self.assertEqual(None, self.downward_list.tail.next)
        self.assertEqual(10, self.downward_list.tail.value)
        self.assertEqual(11, self.downward_list.tail.prev.value)

        self.downward_list.add(11)
        self.assertEqual(4, self.downward_list.len())
        self.assertEqual(None, self.downward_list.head.prev)
        self.assertEqual(12, self.downward_list.head.value)
        self.assertEqual(11, self.downward_list.head.next.value)
        self.assertEqual(11, self.downward_list.head.next.next.value)

        self.assertEqual(None, self.downward_list.tail.next)
        self.assertEqual(10, self.downward_list.tail.value)
        self.assertEqual(11, self.downward_list.tail.prev.value)
        self.assertEqual(11, self.downward_list.tail.prev.prev.value)

        self.downward_list.add(9)
        self.downward_list.add(8)
        self.downward_list.add(11)
        self.downward_list.add(7)
        self.downward_list.add(12)
        self.assertEqual(
            [12, 12, 11, 11, 11, 10, 9, 8, 7],
            [x.value for x in self.downward_list.get_all()]
        )
        ### DOWNWARD LIST ###

    def test_find(self):
        ### UPWARD LIST ###
        self.upward_list.add(10)
        self.assertNotEqual(None, self.upward_list.find(10))
        self.assertEqual(10, self.upward_list.find(10).value)
        self.assertEqual(10, self.upward_list.get_all()[0].value)

        self.upward_list.add(12)
        self.assertNotEqual(None, self.upward_list.find(12))
        self.assertEqual(12, self.upward_list.find(12).value)
        self.assertEqual(12, self.upward_list.get_all()[1].value)

        self.upward_list.add(11)
        self.assertNotEqual(None, self.upward_list.find(11))
        self.assertEqual(11, self.upward_list.find(11).value)
        self.assertEqual(11, self.upward_list.get_all()[1].value)
        ### UPWARD LIST ###

        # ### DOWNWARD LIST ###
        self.downward_list.add(10)
        self.assertNotEqual(None, self.downward_list.find(10))
        self.assertEqual(10, self.downward_list.find(10).value)
        self.assertEqual(10, self.downward_list.get_all()[0].value)

        self.downward_list.add(12)
        self.assertNotEqual(None, self.downward_list.find(12))
        self.assertEqual(12, self.downward_list.find(12).value)
        self.assertEqual(12, self.downward_list.get_all()[0].value)

        self.downward_list.add(11)
        self.assertNotEqual(None, self.downward_list.find(11))
        self.assertEqual(11, self.downward_list.find(11).value)
        self.assertEqual(11, self.downward_list.get_all()[1].value)
        ### DOWNWARD LIST ###

    def test_delete(self):
        ### UPWARD LIST ###
        self.upward_list.add(10)
        self.upward_list.add(12)
        self.upward_list.add(11)

        self.assertEqual(None, self.upward_list.delete(10))
        self.assertEqual(2, self.upward_list.len())
        self.assertEqual(11, self.upward_list.get_all()[0].value)
        self.assertEqual(12, self.upward_list.get_all()[1].value)

        self.assertEqual(None, self.upward_list.delete(12))
        self.assertEqual(1, self.upward_list.len())
        self.assertEqual(11, self.upward_list.get_all()[0].value)

        self.assertEqual(None, self.upward_list.delete(11))
        self.assertEqual(0, self.upward_list.len())
        ### UPWARD LIST ###

        # ### DOWNWARD LIST ###
        self.downward_list.add(10)
        self.downward_list.add(12)
        self.downward_list.add(11)

        self.assertEqual(None, self.downward_list.delete(10))
        self.assertEqual(2, self.downward_list.len())
        self.assertEqual(12, self.downward_list.get_all()[0].value)
        self.assertEqual(11, self.downward_list.get_all()[1].value)

        self.assertEqual(None, self.downward_list.delete(12))
        self.assertEqual(1, self.downward_list.len())
        self.assertEqual(11, self.downward_list.get_all()[0].value)

        self.assertEqual(None, self.downward_list.delete(11))
        self.assertEqual(0, self.downward_list.len())
        ### DOWNWARD LIST ###

    def test_clean(self):
        ### UPWARD LIST ###
        self.upward_list.add(10)
        self.upward_list.add(12)
        self.upward_list.add(11)

        self.assertEqual(None, self.upward_list.clean(False))
        self.assertEqual(0, self.upward_list.len())
        self.assertEqual([], self.upward_list.get_all())
        self.assertEqual(None, self.upward_list.head)
        self.assertEqual(None, self.upward_list.tail)
        ### UPWARD LIST ###

        # ### DOWNWARD LIST ###
        self.downward_list.add(10)
        self.downward_list.add(12)
        self.downward_list.add(11)

        self.assertEqual(None, self.downward_list.clean(False))
        self.assertEqual(0, self.downward_list.len())
        self.assertEqual([], self.downward_list.get_all())
        self.assertEqual(None, self.downward_list.head)
        self.assertEqual(None, self.downward_list.tail)
        ### DOWNWARD LIST ###


if __name__ == '__main__':
    unittest.main()
