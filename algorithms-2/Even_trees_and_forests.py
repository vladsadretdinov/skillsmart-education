class SimpleTreeNode:
    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:
    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def recursive_traversal_delete(self, f_node, parent):
        if parent is None:
            parent = self.Root
        for index, node in enumerate(parent.Children):
            if node is f_node:
                del parent.Children[index]
                return
            if len(node.Children) > 0:
                self.recursive_traversal_delete(f_node, node)

    def recursive_traversal_get(self, parent):
        nodes = []
        if parent is None:
            nodes.append(self.Root)
            parent = self.Root
        for node in parent.Children:
            nodes.append(node)
            if len(node.Children) > 0:
                nodes.extend(self.recursive_traversal_get(node))
        return nodes

    def AddChild(self, ParentNode, NewChild):
        # ваш код добавления нового дочернего узла существующему ParentNode
        ParentNode.Children.append(NewChild)

    def DeleteNode(self, NodeToDelete):
        # ваш код удаления существующего узла NodeToDelete (некорневой)
        self.recursive_traversal_delete(NodeToDelete, None)

    def GetAllNodes(self):
        # ваш код выдачи всех узлов дерева в определённом порядке
        return self.recursive_traversal_get(None)

    def FindNodesByValue(self, val):
        # ваш код поиска узлов по значению
        all_nodes = self.GetAllNodes()
        filtered_nodes = [x for x in all_nodes if x.NodeValue == val]
        return filtered_nodes

    def MoveNode(self, OriginalNode, NewParent):
        # ваш код перемещения узла вместе с его поддеревом --
        # в качестве дочернего для узла NewParent
        self.DeleteNode(OriginalNode)
        self.AddChild(NewParent, OriginalNode)

    def Count(self):
        # количество всех узлов в дереве
        all_nodes = self.GetAllNodes()
        return len(all_nodes)

    def LeafCount(self):
        # количество листьев в дереве
        all_nodes = self.GetAllNodes()
        leaf_nodes = [x for x in all_nodes if len(x.Children) == 0]
        return len(leaf_nodes)

    def set_levels(self, parent=None, level=0):
        if parent is None:
            self.Root.level = level
            parent = self.Root
        for node in parent.Children:
            node.level = level + 1
            if len(node.Children) > 0:
                self.set_levels(node, level + 1)
        return None

    def _even_trees(self, parent=None):
        result = []
        if parent is None:
            parent = self.Root
        for node in parent.Children:
            length = len(self.recursive_traversal_get(node)) + 1
            if length % 2 == 0:
                result.extend([parent, node])
                if length > 2:
                    for sub_node in node.Children:
                        result.extend(self._even_trees(sub_node))
            elif length > 2:
                for sub_node in node.Children:
                    if len(sub_node.Children) > 0:
                        result.extend([node, sub_node])
                    result.extend(self._even_trees(sub_node))
        return result

    def EvenTrees(self):
        return self._even_trees(None)
