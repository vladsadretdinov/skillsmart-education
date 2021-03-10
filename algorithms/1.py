class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            # print(node.value)
            node = node.next
        return None

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        '''
        1.4. Добавьте в класс LinkedList метод поиска всех узлов по конкретному значению (возвращается стандартный питоновский список найденных узлов).
        '''

        # если список пустой то сразу выйти
        if self.head is None:
            return []

        response = []

        # встать в начало списка
        itr = self.head

        # итерироваться пока не конец списка
        while itr is not None:
            if itr.value == val:
                response.append(itr)
            itr = itr.next

        return response

    def delete(self, val, all=False):
        '''
        1.1. Добавьте в класс LinkedList метод удаления одного узла по его значению
        где флажок all=False по умолчанию -- удаляем только первый нашедшийся элемент.

        1.2. Дополните этот метод удалением всех узлов по конкретному значению (флажок all=True).
        '''

        # если список пустой то сразу выйти
        if self.head is None:
            return None

        # встать в начало списка
        itr = self.head
        prev = None

        # итерироваться пока не конец списка
        while itr is not None:
            deleted = False
            if itr.value == val:
                # если это первый элемент то сместить голову
                if itr is self.head:
                    self.head = itr.next
                    # если всего был один элемент - очистить и хвост
                    if itr is self.tail:
                        self.tail = None
                else:
                    if itr is self.tail:
                        self.tail = prev
                    prev.next = itr.next

                if all is False:
                    return None

                deleted = True

            # перейти к след элементу
            if deleted is False:
                prev = itr

            itr = itr.next

        return None

    def clean(self):
        '''
        1.3. Добавьте в класс LinkedList метод очистки всего содержимого (создание пустого списка)
        '''

        self.head = None
        self.tail = None
        return None

    def len(self):
        '''
        1.5. Добавьте в класс LinkedList метод вычисления текущей длины списка
        '''

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

    def insert(self, afterNode, newNode):
        '''
        # 1.6. Добавьте в класс LinkedList метод вставки узла newNode после заданного узла afterNode (из списка)
        '''

        # если список пустой то просто добавить и выйти
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return None

        if afterNode is None:
            tmp = self.head
            self.head = newNode
            self.head.next = tmp
        else:
            # встать в начало списка
            itr = self.head

            # итерироваться пока не конец списка
            while itr is not None:
                if itr is afterNode:
                    if itr is self.tail:
                        self.tail = newNode
                    tmp = itr.next
                    itr.next = newNode
                    newNode.next = tmp
                    return None
                itr = itr.next
        return None
