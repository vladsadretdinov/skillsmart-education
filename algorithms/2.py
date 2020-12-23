class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        '''
        2.1. Добавьте в класс LinkedList2 метод поиска первого узла по его значению.
        '''
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        '''
        2.2. Добавьте в класс LinkedList2 метод поиска всех узлов по конкретному значению (возвращается список найденных узлов).
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
        2.3. Добавьте в класс LinkedList2 метод удаления одного узла по его значению.
            delete(val, all=False)
        где флажок all=False по умолчанию -- удаляем только первый нашедшийся элемент.

        2.4. Дополните этот метод удалением всех узлов по конкретному значению (флажок all=True).
        '''

        # если список пустой то сразу выйти
        if self.head is None:
            return None

        # встать в начало списка
        itr = self.head
        prev = itr.prev

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
                    # если нет то очистить пред значение для головы
                    else:
                        self.head.prev = None
                else:
                    if itr is self.tail:
                        self.tail = itr.prev
                    else:
                        itr.next.prev = prev
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
        2.7. Добавьте в класс LinkedList2 метод очистки всего содержимого (создание пустого списка) -- clean()
        '''

        self.head = None
        self.tail = None
        return None

    def len(self):
        '''
        2.8. Добавьте в класс LinkedList2 метод вычисления текущей длины списка -- len()
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
        2.5. Добавьте в класс LinkedList2 метод вставки узла после заданного узла.

        Если afterNode = None и список пустой, добавьте новый элемент первым в списке.
        Если afterNode = None и список непустой, добавьте новый элемент последним в списке.
        '''
        if afterNode is None:
            if self.head is None:
                self.head = newNode
                self.tail = newNode
                return None
            else:
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
                return None

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
                newNode.prev = itr
                return None
            itr = itr.next
        return None

    def add_in_head(self, newNode):
        '''
        2.6. Добавьте в класс LinkedList2 метод вставки узла самым первым элементом.
        '''
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if self.head is self.tail:
                tmp = self.tail
            else:
                tmp = self.head
            self.head = newNode
            self.head.next = tmp
            tmp.prev = newNode
        return None
