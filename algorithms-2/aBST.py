class aBST:

    def __init__(self, depth):
        # правильно рассчитайте размер массива для дерева глубины depth:
        # depth - tree_size
        # 0 - 1
        # 1 - 3
        # 2 - 7
        # 3 - 15
        # and so on...
        tree_size = 2 ** (depth + 1) - 1
        self.Tree = [None] * tree_size  # массив ключей

    def recursive_find_node_by_key(self, key, parent_index=0):
        if parent_index > len(self.Tree) - 1:
            return {
                'Index': parent_index,
                'IndexHasKey': False,
                'OutOfRange': True
            }

        expected_key = self.Tree[parent_index]

        if expected_key is None:
            return {
                'Index': parent_index,
                'IndexHasKey': False,
                'OutOfRange': False
            }

        if expected_key == key:
            return {
                'Index': parent_index,
                'IndexHasKey': True,
                'OutOfRange': False
            }
        elif key >= expected_key:
            next_index = 2 * parent_index + 2
        else:
            next_index = 2 * parent_index + 1

        return self.recursive_find_node_by_key(key, next_index)

    def FindKeyIndex(self, key):
        # ищем в массиве индекс ключа
        if len(self.Tree) == 0:
            return None
        find_node = self.recursive_find_node_by_key(key)
        if find_node['Index'] is None:
            return None
        if find_node['Index'] == 0:
            return 0
        index = find_node['Index'] if find_node['IndexHasKey'] else - \
            find_node['Index']

        if find_node['OutOfRange'] is True:
            return None
        return index

    def AddKey(self, key):
        # добавляем ключ в массив
        # индекс добавленного/существующего ключа или -1 если не удалось
        insert_index = self.FindKeyIndex(key)
        if insert_index is None:
            return -1
        insert_index = abs(insert_index)
        if self.Tree[insert_index] is None:
            self.Tree[insert_index] = key
            return insert_index
        elif self.Tree[insert_index] == key:
            return insert_index
        return -1
