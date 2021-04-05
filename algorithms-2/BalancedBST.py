class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла


class BalancedBST:

    def __init__(self):
        self.Root = None  # корень дерева

    def nodes_as_array(self, parent=None):
        nodes = []
        if parent is None:
            nodes.append(self.Root.NodeKey)
            parent = self.Root
        else:
            nodes.append(parent.NodeKey)

        if parent.LeftChild is not None:
            nodes.extend(self.nodes_as_array(parent.LeftChild))
        if parent.RightChild is not None:
            nodes.extend(self.nodes_as_array(parent.RightChild))
        return nodes

    def __generate_tree(self, parent, arr):
        arr_length = len(arr)
        middle = arr_length // 2

        new_node = BSTNode(key=arr[middle], parent=parent)
        new_node.Level = parent.Level + 1

        left_branch = arr[0:middle]
        right_branch = arr[middle:] if middle > arr_length else arr[middle+1:]

        if len(left_branch) >= 1:
            new_node.LeftChild = self.__generate_tree(new_node, left_branch)
            new_node.LeftChild.Level = new_node.Level + 1

        if len(right_branch) >= 1:
            new_node.RightChild = self.__generate_tree(new_node, right_branch)
            new_node.RightChild.Level = new_node.Level + 1

        return new_node

    def GenerateTree(self, a):
        # создаём дерево с нуля из неотсортированного массива a

        if not a:
            return None

        arr_length = len(a)

        if arr_length == 1:
            self.Root = BSTNode(key=a[0], parent=None)
            self.Root.Level = 1
            return None

        sorted_arr = sorted(a)

        middle = arr_length // 2
        self.Root = BSTNode(key=sorted_arr[middle], parent=None)
        self.Root.Level = 1

        left_branch = sorted_arr[0:middle]
        right_branch = sorted_arr[middle:] if middle > arr_length else sorted_arr[middle+1:]

        self.Root.LeftChild = self.__generate_tree(parent=self.Root, arr=left_branch)
        self.Root.RightChild = self.__generate_tree(parent=self.Root, arr=right_branch)

    def __is_balanced(self, root_node):
        depth = root_node.Level
        if root_node.LeftChild is not None:
            if root_node.LeftChild.NodeKey > root_node.NodeKey:
                return -1
            new_depth = self.__is_balanced(root_node.LeftChild)
            if new_depth > depth:
                depth = new_depth
        if root_node.RightChild is not None:
            if root_node.RightChild.NodeKey < root_node.NodeKey:
                return -1
            new_depth = self.__is_balanced(root_node.RightChild)
            if new_depth > depth:
                depth = new_depth
        return depth

    def IsBalanced(self, root_node):
        # сбалансировано ли дерево с корнем root_node
        if root_node is None:
            return True

        if root_node.LeftChild is None:
            left_depth = root_node.Level
        else:
            left_depth = self.__is_balanced(root_node.LeftChild)

        if root_node.RightChild is None:
            right_depth = root_node.Level
        else:
            right_depth = self.__is_balanced(root_node.RightChild)

        if left_depth == -1 or right_depth == -1:
            return False

        return True if abs(left_depth - right_depth) <= 1 else False
