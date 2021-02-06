import operator
from Binary_tree import BinaryTree
from typing import Generic, TypeVar, List
T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()  # LIFO

    def __repr__(self) -> str:
        return repr(self._container)


def build_parse_tree(data) -> BinaryTree:
    tmp_list = []
    num = ''

    new_stack = Stack()
    new_tree = BinaryTree('')
    new_stack.push(new_tree)
    current_tree = new_tree

    for char in data:
        if char not in ['(', '+', '-', '*', '/', ')']:
            if num == '':
                num = char
            else:
                num = num + char
        else:
            if num != '':
                tmp_list.append(num)
            tmp_list.append(char)
            num = ''

    for token in tmp_list:
        if token == '(':
            current_tree.insert_left('')
            new_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif token in ['+', '-', '*', '/', 'and', 'or']:
            current_tree.set_root_val(token)
            current_tree.insert_right('')
            new_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif token == ')':
            current_tree = new_stack.pop()
        else:
            try:
                n = float(token)
            except ValueError:
                raise Exception(f'Not a valid integer: {token}')

            current_tree.set_root_val(n)
            parent = new_stack.pop()
            current_tree = parent

    return new_tree


def evaluate(parse_tree):
    operates = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    left_c = parse_tree.get_left_child()
    right_c = parse_tree.get_right_child()

    if left_c and right_c:
        fn = operates[parse_tree.get_root_val()]
        return fn(evaluate(left_c), evaluate(right_c))
    else:
        return parse_tree.get_root_val()


def print_exp(tree: BinaryTree) -> str:
    s_val = ""
    if tree:
        s_val = '(' + print_exp(tree.get_left_child())
        s_val = s_val + str(tree.get_root_val())
        s_val = s_val + print_exp(tree.get_right_child())+')'
    return s_val


if __name__ == "__main__":
    # pt: BinaryTree = build_parse_tree("((10+5)*3)")
    rt: BinaryTree = build_parse_tree("(True or False) and False")
    # print(evaluate(pt))
    print(evaluate(rt))
    # pt.pre_order()
    # print()
    # pt.post_order()
    # print()
    # pt.in_order()
    # print("__")
    # print(print_exp(pt))
