from binary_trees import BST


class BST_SEARCH(BST):
    def __init__(self, node):
        super(BST_SEARCH, self).__init__(node)

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
