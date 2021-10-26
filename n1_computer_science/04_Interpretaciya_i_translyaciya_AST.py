import re
from collections import Counter


def __left_side_add_brackets(left_side: str):
    counter = Counter(left_side)

    if counter['('] != counter[')']:
        pass
    elif re.match(r"^.*\(\d+$", left_side):
        pass
    elif not left_side.endswith(")"):
        left_side = "".join(list(reversed(left_side)))
        left_side = re.sub(r"(\d+)", r"\1(", left_side, 1)
        left_side = "".join(list(reversed(left_side)))
    else:
        counter = 0
        for index, char in enumerate(reversed(left_side)):
            if char == ")":
                counter = counter + 1
            elif char == "(":
                counter = counter - 1

            if char in ("(", ")"):
                if counter == 0:
                    split_index = len(left_side) - index - 1
                    left_side = left_side[:split_index] + \
                        "(" + left_side[split_index:]
                    break
    return left_side


def __right_side_add_brackets(right_side: str):
    counter = Counter(right_side)

    if counter['('] != counter[')']:
        pass
    elif re.match(r"^\d+\).*$", right_side):
        pass
    elif not right_side.startswith("("):
        right_side = re.sub(r"(\d+)", r"\1)", right_side, 1)
    else:
        counter = 0
        for index, char in enumerate(right_side):
            if char == "(":
                counter = counter + 1
            elif char == ")":
                counter = counter - 1

            if char in ("(", ")"):
                if counter == 0:
                    split_index = index + 1
                    right_side = right_side[:split_index] + \
                        ")" + right_side[split_index:]
                    break
    return right_side


def __add_brackets(expression: str, sign: str, left_indent: int = 1):
    split_expression = expression.split(sign)

    if len(split_expression) == 1:
        return expression

    left_side = sign.join(split_expression[:left_indent])
    split_expression = split_expression[left_indent:]
    right_side = sign.join(split_expression)

    if right_side == "":
        return expression

    left_side = __left_side_add_brackets(left_side)
    right_side = __right_side_add_brackets(right_side)

    return __add_brackets(f"{left_side}{sign}{right_side}", sign, left_indent + 1)


class ANode:
    def __init__(self, token_value):
        self.token_value = token_value

    @property
    def token_type(self):
        if self.token_value in ("(", ")"):
            return "скобка"
        elif self.token_value in ("/", "*", "-", "+"):
            return "операция"
        else:
            return "число"


def __make_token_list(expression: str):
    token_list = []
    possible_number = ""
    for char in expression:
        if char in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            possible_number = possible_number + char
        elif possible_number != "":
            token_list.append(ANode(int(possible_number)))
            token_list.append(ANode(char))
            possible_number = ""
        else:
            token_list.append(ANode(char))

    if possible_number != "":
        token_list.append(ANode(int(possible_number)))

    return token_list


def __make_tree(token_list: list):
    token_list_length = len(token_list)

    if token_list_length == 0:
        tree = SimpleTree(None)
    elif token_list_length == 1:
        root = SimpleTreeNode(token_list[0].token_value, None)
        tree = SimpleTree(root)
    else:
        root = SimpleTreeNode()
        tree = SimpleTree(root)
        tree.AST(token_list, root)

    return tree


class SimpleTreeNode:
    def __init__(self, val=None, parent=None):
        self.NodeValue = val  # значение в узле None как промежуточное значение
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок


class SimpleTree:
    def __init__(self, root=None):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode: SimpleTreeNode, NewChild: SimpleTreeNode, Left=True):
        if Left:
            ParentNode.LeftChild = NewChild
        else:
            ParentNode.RightChild = NewChild
        NewChild.Parent = ParentNode

    def AST(self, tokens_list: list, node: SimpleTreeNode):
        if len(tokens_list) == 0:
            return
        else:
            token = tokens_list.pop(0)
            if node is None:
                node = SimpleTreeNode()

            if token.token_value == "(":
                left_child = SimpleTreeNode()
                self.AddChild(node, left_child, Left=True)
                return self.AST(tokens_list, left_child)
            elif token.token_value == ")":
                return self.AST(tokens_list, node.Parent)
            elif token.token_type == "операция":
                node.NodeValue = token.token_value
                right_child = SimpleTreeNode()
                self.AddChild(node, right_child, Left=False)
                return self.AST(tokens_list, right_child)
            else:
                node.NodeValue = token.token_value
                return self.AST(tokens_list, node.Parent)

    def __inorder_traversal(self, parent=None):
        nodes = []

        if parent is None:
            if self.Root is None:
                return []
            parent = self.Root

        if parent.LeftChild is not None:
            nodes.extend(self.__inorder_traversal(parent.LeftChild))

        nodes.append(parent)

        if parent.RightChild is not None:
            nodes.extend(self.__inorder_traversal(parent.RightChild))

        return nodes

    def print_nodes(self):
        nodes = self.__inorder_traversal()
        print(tuple(x.NodeValue for x in nodes))

    def interpret(self, node=None):
        if node is None:
            node = self.Root

        if node.LeftChild is None and node.RightChild is None:
            node.Description = f"{node.NodeValue}"
            return

        is_left_child_operation = node.LeftChild is not None and node.LeftChild.NodeValue in ("/", "*", "-", "+")
        is_right_child_operation = node.RightChild is not None and node.RightChild.NodeValue in ("/", "*", "-", "+")

        if not is_left_child_operation and not is_right_child_operation:
            result = None
            if node.LeftChild is not None and node.RightChild is not None:
                if node.NodeValue == "*":
                    result = node.LeftChild.NodeValue * node.RightChild.NodeValue
                elif node.NodeValue == "/":
                    result = node.LeftChild.NodeValue / node.RightChild.NodeValue
                elif node.NodeValue == "-":
                    result = node.LeftChild.NodeValue - node.RightChild.NodeValue
                else:
                    result = node.LeftChild.NodeValue + node.RightChild.NodeValue
            else:
                pass

            node.Description = f"({node.LeftChild.NodeValue} {node.NodeValue} {node.RightChild.NodeValue})"
            node.NodeValue = result
            node.LeftChild = None
            node.RightChild = None
            return

        if is_left_child_operation:
            self.interpret(node.LeftChild)
        if is_right_child_operation:
            self.interpret(node.RightChild)

        if node.Parent is not None:
            self.interpret(node.Parent)
        elif node.NodeValue in ("/", "*", "-", "+"):
            self.interpret(node.Parent)


def main(expression: str):
    new_expression = expression.replace(" ", "")
    new_expression = __add_brackets(new_expression, "/")
    new_expression = __add_brackets(new_expression, "*")
    new_expression = __add_brackets(new_expression, "-")
    new_expression = __add_brackets(new_expression, "+")

    token_list = __make_token_list(new_expression)
    tree = __make_tree(token_list)

    return tree


if __name__ == "__main__":
    expressions = [
        "2",
        "12+33",
        "3*5+2",
        "1-1+1+1",
        "((7+3)*(5-2))",
        "7+3*5-2",
        "10+5-16+1",
        "3+5-5+3",
        "7+3/25*(5-2)",
        "(5-2)",
    ]
    for expression in expressions:
        tree = main(expression)
        # tree.print_nodes()
        tree.interpret()
        print(eval(expression) == tree.Root.NodeValue == eval(tree.Root.Description))



