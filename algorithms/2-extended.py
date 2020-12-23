import unittest


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

# * 2.10. Существует интересный финт, обсуждаемый на курсе Стэнфордского университета CS106B -- фиктивный/пустой (dummy) узел.
# Пока нам при любых модификациях списка (добавление/удаление узла) приходится рассматривать три отдельные ситуации:
# работа с серединой списка, с его головой и с его хвостом.
# Фиктивный узел позволяет избавиться от этих краевых ситуаций, оставив только по одной универсальной операции на добавление и удаление.
# Идея в том, что мы добавляем в список два искусственных узла -- голову и хвост, которые пользователю класса не видны
# (они отличаются от видимых узлов, например, булевым флажком, а лучше всего это делать через наследование и перегрузку).
# Теперь, добавляя или удаляя узлы, мы всегда будем уверены, что у каждого из них имеется и предыдущий узел, и последующий,
# и от дополнительных проверок и модификаций полей head и tail можно избавиться.


class TestUM(unittest.TestCase):
    '''
    2.9. Напишите проверочные тесты для каждого из предыдущих заданий.
    '''

    def setUp(self):
        self.empty_list = LinkedList2()

        self.list_with_one_element = LinkedList2()
        self.alone_node = Node(13)
        self.list_with_one_element.add_in_tail(self.alone_node)

        self.list_with_7_elements = LinkedList2()
        self.node_1 = Node(1)
        self.node_2 = Node(2)
        self.node_3 = Node(1)
        self.node_4 = Node(1)
        self.node_5 = Node(4)
        self.node_6 = Node(5)
        self.node_7 = Node(1)
        self.list_with_7_elements.add_in_tail(self.node_1)
        self.list_with_7_elements.add_in_tail(self.node_2)
        self.list_with_7_elements.add_in_tail(self.node_3)
        self.list_with_7_elements.add_in_tail(self.node_4)
        self.list_with_7_elements.add_in_tail(self.node_5)
        self.list_with_7_elements.add_in_tail(self.node_6)
        self.list_with_7_elements.add_in_tail(self.node_7)

    ### FIND ###
    def test_find_empty_list(self):
        self.assertEqual(None, self.empty_list.find(1))

    def test_find_list_with_one_element(self):
        self.assertEqual(None, self.list_with_one_element.find(12))
        self.assertEqual(self.alone_node, self.list_with_one_element.find(13))

    def test_find_list_with_7_elements(self):
        self.assertEqual(None, self.list_with_7_elements.find(0))
        self.assertEqual(self.node_1, self.list_with_7_elements.find(1))
        self.assertEqual(self.node_2, self.list_with_7_elements.find(2))
        self.assertEqual(self.node_6, self.list_with_7_elements.find(5))
    ### FIND ###

    ### FIND_ALL ###
    def test_find_all_empty_list(self):
        self.assertEqual([], self.empty_list.find_all(1))
        self.assertEqual([], self.empty_list.find_all(2))

    def test_find_all_list_with_one_element(self):
        self.assertEqual(
            [self.alone_node],
            self.list_with_one_element.find_all(13)
        )
        self.assertEqual([], self.list_with_one_element.find_all(2))

    def test_find_all_list_with_7_elements(self):
        self.assertEqual([self.node_1, self.node_3, self.node_4, self.node_7],
                         self.list_with_7_elements.find_all(1))
        self.assertEqual([self.node_2], self.list_with_7_elements.find_all(2))
    ### FIND_ALL ###

    ### DELETE FLAG ALL = FALSE ###
    def test_delete_empty_list_false(self):
        self.empty_list.delete(1)
        self.assertEqual(None, self.empty_list.head)
        self.assertEqual(None, self.empty_list.tail)

    def test_delete_list_with_one_element_false(self):
        # удалить несуществующее значение
        self.list_with_one_element.delete(1)
        self.assertNotEqual(
            None,
            self.list_with_one_element.head
        )
        self.assertNotEqual(
            None,
            self.list_with_one_element.tail
        )

        # удалить существующее значение
        self.list_with_one_element.delete(13)
        self.assertEqual(
            None,
            self.list_with_one_element.head
        )
        self.assertEqual(
            None,
            self.list_with_one_element.tail
        )

    def test_delete_list_with_7_elements_false(self):
        # удалить несуществующий в списке элемент
        len_before = self.list_with_7_elements.len()
        self.list_with_7_elements.delete(777)
        self.assertEqual(
            len_before,
            self.list_with_7_elements.len()
        )

        # удалить существующий в списке элемент идущим первым
        self.list_with_7_elements.delete(1)
        self.assertNotEqual(
            1,
            self.list_with_7_elements.head.value
        )
    ### DELETE FLAG ALL = FALSE ###

    ### DELETE FLAG ALL = TRUE ###
    def test_delete_empty_list_true(self):
        self.empty_list.delete(1, True)
        self.assertEqual(None, self.empty_list.head)
        self.assertEqual(None, self.empty_list.tail)

    def test_delete_list_with_one_element_true(self):
        # удалить несуществующее значение
        self.list_with_one_element.delete(1, True)
        self.assertNotEqual(
            None,
            self.list_with_one_element.head
        )
        self.assertNotEqual(
            None,
            self.list_with_one_element.tail
        )

        # удалить существующее значение
        self.list_with_one_element.delete(13, True)
        self.assertEqual(
            None,
            self.list_with_one_element.head
        )
        self.assertEqual(
            None,
            self.list_with_one_element.tail
        )

    def test_delete_list_with_7_elements_true(self):
        # удалить несуществующий в списке элемент
        len_before = self.list_with_7_elements.len()
        self.list_with_7_elements.delete(777, True)
        self.assertEqual(
            len_before,
            self.list_with_7_elements.len()
        )

        # удалить существующий в списке элемент встречающийся один раз в списке
        len_before = self.list_with_7_elements.len()
        self.list_with_7_elements.delete(4, True)
        self.assertEqual(
            len_before - 1,
            self.list_with_7_elements.len()
        )

        # удалить существующий в списке элемент встречающийся четыре раза в списке
        len_before = self.list_with_7_elements.len()
        self.list_with_7_elements.delete(1, True)
        self.assertEqual(
            len_before - 4,
            self.list_with_7_elements.len()
        )
        self.assertEqual(
            self.node_6,
            self.list_with_7_elements.tail
        )
        self.assertEqual(
            None,
            self.list_with_7_elements.tail.next
        )
        self.assertEqual(
            None,
            self.list_with_7_elements.find(1)
        )
        self.assertEqual(
            self.node_2,
            self.list_with_7_elements.tail.prev
        )
        self.assertEqual(
            self.node_6,
            self.list_with_7_elements.head.next
        )
    ### DELETE FLAG ALL = FALSE ###

    ### INSERT ###
    def test_insert_empty_list(self):
        tmp = Node(1)
        self.empty_list.insert(None, tmp)
        self.assertEqual(tmp, self.empty_list.head)
        self.assertEqual(tmp, self.empty_list.tail)
        self.assertEqual(None, self.empty_list.head.prev)
        self.assertEqual(None, self.empty_list.tail.prev)

    def test_insert_list_with_one_element(self):
        len_before = self.list_with_one_element.len()
        tmp = Node(1)
        self.list_with_one_element.insert(self.alone_node, tmp)
        self.assertEqual(len_before + 1, self.list_with_one_element.len())
        self.assertEqual(self.alone_node, self.list_with_one_element.head)
        self.assertEqual(self.alone_node.next, tmp)
        self.assertEqual(tmp, self.list_with_one_element.tail)
        self.assertEqual(None, self.list_with_one_element.head.prev)
        self.assertEqual(self.alone_node, self.list_with_one_element.tail.prev)
        tmp_2 = Node(2)
        self.list_with_one_element.insert(None, tmp_2)
        self.assertEqual(tmp_2, self.list_with_one_element.tail)
        self.assertEqual(tmp, self.list_with_one_element.tail.prev)
        self.assertEqual(tmp_2, self.list_with_one_element.head.next.next)

    def test_insert_list_with_7_elements(self):
        len_before = self.list_with_7_elements.len()
        tmp = Node(1)
        self.list_with_7_elements.insert(self.node_2, tmp)
        self.assertEqual(len_before + 1, self.list_with_7_elements.len())
        self.assertEqual(tmp, self.list_with_7_elements.head.next.next)
        self.assertEqual(tmp.next, self.node_3)
        self.assertEqual(self.node_7, self.list_with_7_elements.tail)
        tmp_2 = Node(2)
        self.list_with_7_elements.insert(None, tmp_2)
        self.assertEqual(tmp_2, self.list_with_7_elements.tail)
        self.assertEqual(self.node_7, self.list_with_7_elements.tail.prev)
    ### INSERT ###

    ### ADD IN HEAD ###
    def test_add_in_head_empty_list(self):
        tmp = Node(1)
        self.empty_list.add_in_head(tmp)
        self.assertEqual(tmp, self.empty_list.head)
        self.assertEqual(tmp, self.empty_list.tail)
        self.assertEqual(None, self.empty_list.head.prev)
        self.assertEqual(None, self.empty_list.tail.prev)

    def test_add_in_head_list_with_one_element(self):
        len_before = self.list_with_one_element.len()
        tmp = Node(1)
        self.list_with_one_element.add_in_head(tmp)
        self.assertEqual(len_before + 1, self.list_with_one_element.len())
        self.assertEqual(tmp, self.list_with_one_element.head)
        self.assertEqual(tmp.next, self.alone_node)
        self.assertEqual(self.alone_node, self.list_with_one_element.tail)
        self.assertEqual(None, self.list_with_one_element.head.prev)
        self.assertEqual(tmp, self.list_with_one_element.tail.prev)
        tmp_2 = Node(2)
        self.list_with_one_element.add_in_head(tmp_2)
        self.assertEqual(self.alone_node, self.list_with_one_element.tail)
        self.assertEqual(tmp, self.list_with_one_element.tail.prev)
        self.assertEqual(tmp_2, self.list_with_one_element.head)

    def test_add_in_head_list_with_7_elements(self):
        len_before = self.list_with_7_elements.len()
        tmp = Node(1)
        self.list_with_7_elements.add_in_head(tmp)
        self.assertEqual(len_before + 1, self.list_with_7_elements.len())
        self.assertEqual(self.node_2, self.list_with_7_elements.head.next.next)
        self.assertEqual(tmp.next, self.node_1)
        self.assertEqual(self.node_7, self.list_with_7_elements.tail)
        tmp_2 = Node(2)
        self.list_with_7_elements.add_in_head(tmp_2)
        self.assertEqual(tmp_2, self.list_with_7_elements.head)
        self.assertEqual(self.node_6, self.list_with_7_elements.tail.prev)
    ### ADD IN HEAD ###


if __name__ == '__main__':
    unittest.main()
