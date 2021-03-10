class BSTNode:

    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class BSTFind:  # промежуточный результат поиска

    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:

    def __init__(self, node):
        self.Root = node  # корень дерева, или None

    def recursive_find_node_by_key(self, key, parent=None):
        if parent is None:
            parent = self.Root

        if parent is None:
            return {
                'Node': None,
                'NodeHasKey': False,
                'ToLeft': False
            }

        next_parent = None

        if parent.NodeKey == key:
            return {
                'Node': parent,
                'NodeHasKey': True,
                'ToLeft': False
            }
        elif key >= parent.NodeKey:
            next_parent = parent.RightChild
        elif key < parent.NodeKey:
            next_parent = parent.LeftChild

        if next_parent is not None:
            return self.recursive_find_node_by_key(key, next_parent)

        return {
            'Node': parent,
            'NodeHasKey': False,
            'ToLeft': False if parent.NodeKey < key else True
        }

    def FindNodeByKey(self, key):
        # ищем в дереве узел и сопутствующую информацию по ключу
        # возвращает BSTFind
        founded_node = self.recursive_find_node_by_key(key)
        bst_find = BSTFind()

        bst_find.Node = founded_node['Node']
        bst_find.NodeHasKey = founded_node['NodeHasKey']
        bst_find.ToLeft = founded_node['ToLeft']

        return bst_find

    def AddKeyValue(self, key, val):
        # добавляем ключ-значение в дерево

        if self.Root is None:
            bst_node = BSTNode(key, val, None)
            self.Root = bst_node
            return True

        bst_node = self.FindNodeByKey(key)

        if bst_node.NodeHasKey is True:
            return False  # если ключ уже есть

        if bst_node.ToLeft is True:
            bst_node.Node.LeftChild = BSTNode(key, val, bst_node.Node)
        else:
            bst_node.Node.RightChild = BSTNode(key, val, bst_node.Node)

        return True

    def recursive_find_max_min(self, max=False, parent=None):
        if parent is None:
            parent = self.Root

        if max is False:
            if parent.LeftChild is not None:
                return self.recursive_find_max_min(max, parent.LeftChild)
        else:
            if parent.RightChild is not None:
                return self.recursive_find_max_min(max, parent.RightChild)

        return parent

    def FinMinMax(self, FromNode, FindMax):
        # ищем максимальный/минимальный ключ в поддереве
        # возвращается объект типа BSTNode
        founded_node = self.recursive_find_max_min(FindMax, FromNode)
        return founded_node

    def DeleteNodeByKey(self, key):
        # удаляем узел по ключу
        bst_node_delete = self.FindNodeByKey(key)

        if bst_node_delete.NodeHasKey is False:
            return False  # если узел не найден

        # Deleted node has no children
        if bst_node_delete.Node.LeftChild is None and bst_node_delete.Node.RightChild is None:
            if bst_node_delete.Node is self.Root:
                self.Root = None
                return True
            if bst_node_delete.Node.NodeKey < bst_node_delete.Node.Parent.NodeKey:
                bst_node_delete.Node.Parent.LeftChild = None
            else:
                bst_node_delete.Node.Parent.RightChild = None
            return True

        # Deleted node has only one cnild
        if bst_node_delete.Node.LeftChild is None or bst_node_delete.Node.RightChild is None:
            if bst_node_delete.Node.LeftChild is None:
                bst_node_to_connect = bst_node_delete.Node.RightChild
            else:
                bst_node_to_connect = bst_node_delete.Node.LeftChild

            if bst_node_delete.Node is self.Root:
                self.Root = bst_node_to_connect
                self.Root.Parent = None
                return True

            if bst_node_delete.Node.NodeKey < bst_node_delete.Node.Parent.NodeKey:
                bst_node_delete.Node.Parent.LeftChild = bst_node_to_connect
            else:
                bst_node_delete.Node.Parent.RightChild = bst_node_to_connect

            bst_node_to_connect.Parent = bst_node_delete.Node.Parent
            return True

        # Deleted node has both (left and right) nodes
        bst_node_to_change = self.FinMinMax(
            bst_node_delete.Node.RightChild, False)

        try:
            if bst_node_delete.Node.NodeKey < bst_node_delete.Node.Parent.NodeKey:
                bst_node_delete.Node.Parent.LeftChild = bst_node_to_change
            else:
                bst_node_delete.Node.Parent.RightChild = bst_node_to_change
        except Exception:
            # if we delete root node
            self.Root = bst_node_to_change

        bst_node_to_change.LeftChild = bst_node_delete.Node.LeftChild
        bst_node_to_change.LeftChild.Parent = bst_node_to_change

        if bst_node_delete.Node.RightChild is not bst_node_to_change:
            if bst_node_to_change.RightChild is None:
                bst_node_to_change.Parent.LeftChild = None
            else:
                bst_node_to_change.Parent.LeftChild = bst_node_to_change.RightChild

            bst_node_to_change.RightChild = bst_node_delete.Node.RightChild
            bst_node_delete.Node.RightChild.Parent = bst_node_to_change

        bst_node_to_change.Parent = bst_node_delete.Node.Parent
        return True

    def recursive_nodes_count(self, parent=None):
        nodes = 0
        if parent is None:
            nodes = nodes + 1
            parent = self.Root
        else:
            nodes = nodes + 1

        if parent.LeftChild is not None:
            nodes = nodes + self.recursive_nodes_count(parent.LeftChild)
        if parent.RightChild is not None:
            nodes = nodes + self.recursive_nodes_count(parent.RightChild)

        return nodes

    def Count(self):
        if self.Root is None:
            return 0
        # количество узлов в дереве
        return self.recursive_nodes_count()

    def wide_all_nodes(self, parents=None):
        nodes = []

        if parents is None:
            if self.Root is None:
                return ()
            nodes.append(self.Root)
            parents = [self.Root]

        next_parents = []

        for parent in parents:
            if parent.LeftChild is not None:
                next_parents.append(parent.LeftChild)
            if parent.RightChild is not None:
                next_parents.append(parent.RightChild)

        nodes.extend(next_parents)

        if len(next_parents) > 0:
            nodes.extend(self.wide_all_nodes(next_parents))

        return nodes

    def preorder_traversal(self, parent=None):
        nodes = []

        if parent is None:
            if self.Root is None:
                return []
            parent = self.Root

        nodes.append(parent)

        if parent.LeftChild is not None:
            nodes.extend(self.preorder_traversal(parent.LeftChild))

        if parent.RightChild is not None:
            nodes.extend(self.preorder_traversal(parent.RightChild))

        return nodes

    def inorder_traversal(self, parent=None):
        nodes = []

        if parent is None:
            if self.Root is None:
                return []
            parent = self.Root

        if parent.LeftChild is not None:
            nodes.extend(self.inorder_traversal(parent.LeftChild))

        nodes.append(parent)

        if parent.RightChild is not None:
            nodes.extend(self.inorder_traversal(parent.RightChild))

        return nodes

    def postorder_traversal(self, parent=None):
        nodes = []

        if parent is None:
            if self.Root is None:
                return []
            parent = self.Root

        if parent.LeftChild is not None:
            nodes.extend(self.postorder_traversal(parent.LeftChild))

        if parent.RightChild is not None:
            nodes.extend(self.postorder_traversal(parent.RightChild))

        nodes.append(parent)

        return nodes

    def WideAllNodes(self):
        nodes = self.wide_all_nodes()
        return tuple(nodes)

    def DeepAllNodes(self, order=2):
        traversal_map = {
            0: self.inorder_traversal,
            1: self.postorder_traversal,
            2: self.preorder_traversal
        }
        nodes = traversal_map[order]()
        return tuple(nodes)
