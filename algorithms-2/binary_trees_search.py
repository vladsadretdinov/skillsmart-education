from binary_trees import BSTNode, BSTFind, BST


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

    def WideAllNodes(self):
        nodes = self.wide_all_nodes()
        return tuple(nodes)
