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


def add_brackets(expression: str, sign: str, left_indent: int = 1):
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

    return add_brackets(f"{left_side}{sign}{right_side}", sign, left_indent + 1)


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


def main(expression: str):
    new_expression = expression.replace(" ", "")
    new_expression = add_brackets(new_expression, "/")
    new_expression = add_brackets(new_expression, "*")
    new_expression = add_brackets(new_expression, "-")
    new_expression = add_brackets(new_expression, "+")

    list_of_tokens = []
    possible_number = ""
    for char in new_expression:
        if char in range(0, 9):
            possible_number = possible_number + char
        elif possible_number != "":
            list_of_tokens.append(ANode(int(possible_number)))
            possible_number = ""
        else:
            list_of_tokens.append(ANode(char))

    return list_of_tokens


if __name__ == "__main__":
    print(main("1-1+1+1"))
    print(main("((7+3)*(5-2))"))
    print(main("7+3*5-2"))
    print(main("10+5-16+1"))
    print(main("3+5-5+3"))
    print(main("7+3/25*(5-2)"))
    print(main("(5-2)"))
