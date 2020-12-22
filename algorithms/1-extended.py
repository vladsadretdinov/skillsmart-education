import unittest


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
        while node != None:
            print(node.value)
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

            # перейти к след элементу
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


def sum_two_list(list1, list2):
    '''
    * 1.8. Напишите функцию, которая получает на вход два связанных списка, состоящие из целых значений,
    и если их длины равны, возвращает список, каждый элемент которого равен сумме соответствующих элементов входных списков.
    '''

    if list1.len() == list2.len():
        arr1 = []
        arr2 = []
        response = []

        node = list1.head
        while node is not None:
            arr1.append(node.value)
            node = node.next

        node = list2.head
        while node is not None:
            arr2.append(node.value)
            node = node.next

        for i, j in zip(arr1, arr2):
            response.append(i + j)

        return response
    else:
        # сообщение о том что списки разной длины?
        return []


class TestUM(unittest.TestCase):
    def setUp(self):
        self.empty_list = LinkedList()

        self.list_with_one_element = LinkedList()
        self.alone_node = Node(13)
        self.list_with_one_element.add_in_tail(self.alone_node)

        self.list_with_7_elements = LinkedList()
        self.node_1 = Node(1)
        self.node_2 = Node(2)
        self.node_3 = Node(3)
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

    ### LEN ###
    def test_len_empty_list(self):
        self.assertEqual(0, self.empty_list.len())

    def test_len_list_with_one_element(self):
        self.assertEqual(1, self.list_with_one_element.len())

    def test_len_list_with_7_elements(self):
        self.assertEqual(7, self.list_with_7_elements.len())
    ### LEN ###

    ### CLEAN ###
    def test_clean_empty_list(self):
        self.empty_list.clean()
        self.assertEqual(None, self.empty_list.head)
        self.assertEqual(None, self.empty_list.tail)

    def test_clean_list_with_one_element(self):
        self.list_with_one_element.clean()
        self.assertEqual(None, self.list_with_one_element.head)
        self.assertEqual(None, self.list_with_one_element.tail)

    def test_clean_list_with_7_elements(self):
        self.list_with_7_elements.clean()
        self.assertEqual(None, self.list_with_7_elements.head)
        self.assertEqual(None, self.list_with_7_elements.tail)

    ### CLEAN ###

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
        self.assertEqual([self.node_1, self.node_4, self.node_7],
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

        # удалить существующий в списке элемент встречающийся три раза в списке
        len_before = self.list_with_7_elements.len()
        self.list_with_7_elements.delete(1, True)
        self.assertEqual(
            len_before - 3,
            self.list_with_7_elements.len()
        )
        self.assertEqual(
            self.node_6,
            self.list_with_7_elements.tail
        )
    ### DELETE FLAG ALL = FALSE ###

    ### INSERT FLAG AFTERNODE - None ###
    def test_insert_empty_list_none(self):
        len_before = self.empty_list.len()
        tmp = Node(1)
        self.empty_list.insert(None, tmp)
        self.assertEqual(len_before + 1, self.empty_list.len())
        self.assertEqual(tmp, self.empty_list.head)
        self.assertEqual(tmp, self.empty_list.tail)

    def test_insert_list_with_one_element_none(self):
        len_before = self.list_with_one_element.len()
        tmp = Node(1)
        self.list_with_one_element.insert(None, tmp)
        self.assertEqual(len_before + 1, self.list_with_one_element.len())
        self.assertEqual(tmp, self.list_with_one_element.head)
        self.assertEqual(tmp.next, self.alone_node)
        self.assertEqual(self.alone_node, self.list_with_one_element.tail)

    def test_insert_list_with_7_elements_none(self):
        len_before = self.list_with_7_elements.len()
        tmp = Node(1)
        self.list_with_7_elements.insert(None, tmp)
        self.assertEqual(len_before + 1, self.list_with_7_elements.len())
        self.assertEqual(tmp, self.list_with_7_elements.head)
        self.assertEqual(tmp.next, self.node_1)
        self.assertEqual(self.node_7, self.list_with_7_elements.tail)
    ### INSERT FLAG AFTERNODE - None ###

    ### INSERT ###
    def test_insert_list_with_one_element(self):
        len_before = self.list_with_one_element.len()
        tmp = Node(1)
        self.list_with_one_element.insert(self.alone_node, tmp)
        self.assertEqual(len_before + 1, self.list_with_one_element.len())
        self.assertEqual(self.alone_node, self.list_with_one_element.head)
        self.assertEqual(self.alone_node.next, tmp)
        self.assertEqual(tmp, self.list_with_one_element.tail)

    def test_insert_list_with_7_elements(self):
        len_before = self.list_with_7_elements.len()
        tmp = Node(1)
        self.list_with_7_elements.insert(self.node_2, tmp)
        self.assertEqual(len_before + 1, self.list_with_7_elements.len())
        self.assertEqual(tmp, self.list_with_7_elements.head.next.next)
        self.assertEqual(tmp.next, self.node_3)
        self.assertEqual(self.node_7, self.list_with_7_elements.tail)
    ### INSERT ###

    ### SUM_TO_LIST ###
    def test_sum_to_list_empty_list(self):
        self.assertEqual([], sum_two_list(LinkedList(), self.empty_list))
        tmp_list = LinkedList()
        tmp_list.add_in_tail(Node(1))
        self.assertEqual([], sum_two_list(tmp_list, self.empty_list))

    def test_sum_to_list_list_with_one_element(self):
        self.assertEqual(
            [],
            sum_two_list(
                LinkedList(),
                self.list_with_one_element
            )
        )
        tmp_list = LinkedList()
        tmp_list.add_in_tail(Node(12))
        self.assertEqual(
            [25],
            sum_two_list(
                tmp_list,
                self.list_with_one_element
            )
        )

    def test_sum_to_list_list_with_7_elements(self):
        self.assertEqual(
            [],
            sum_two_list(
                LinkedList(),
                self.list_with_7_elements
            )
        )
        tmp_list = LinkedList()
        tmp_list.add_in_tail(Node(1))
        tmp_list.add_in_tail(Node(1))
        tmp_list.add_in_tail(Node(1))
        tmp_list.add_in_tail(Node(1))
        tmp_list.add_in_tail(Node(1))
        tmp_list.add_in_tail(Node(1))
        tmp_list.add_in_tail(Node(1))
        self.assertEqual(
            [
                self.node_1.value + 1,
                self.node_2.value + 1,
                self.node_3.value + 1,
                self.node_4.value + 1,
                self.node_5.value + 1,
                self.node_6.value + 1,
                self.node_7.value + 1,
            ],
            sum_two_list(
                tmp_list,
                self.list_with_7_elements
            )
        )
    ### SUM_TO_LIST ###


if __name__ == '__main__':
    unittest.main()
