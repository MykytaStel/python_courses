from typing import Optional
import operator


class Tree:

    def __init__(self,
                 root: any,
                 left: Optional['Tree'] = None,
                 right: Optional['Tree'] = None):
        self.root = root
        self.left = left
        self.right = right
        self.need_to_reverse_result = False

    def insert_left(self, tree: 'Tree'):
        self.left = tree

    def insert_right(self, tree: 'Tree'):
        self.right = tree

    def __str__(self):
        return f'Tree({self.root}; {self.left}; {self.right} )'


def parse_expr(expression: str) -> Tree:
    tokens = expression.split()
    current_tree: Tree = Tree('')
    stack = [current_tree]

    for token in tokens:
        if token == '(':
            tree = Tree("")
            current_tree.insert_left(tree)
            stack.append(current_tree)
            current_tree = tree
        elif token == ')':
            current_tree = stack.pop()
        elif token in {'-', '+', '*', '/'}:
            current_tree.root = token
            tree = Tree('')
            current_tree.insert_right(tree)
            stack.append(tree)
            current_tree = tree
        else:
            try:
                n = int(token)
            except ValueError:
                raise Exception(f'Not a valid integer: {token}')

            current_tree.root = n
            current_tree = stack.pop()

    return current_tree


def bool_expr(expression: str) -> Tree:
    tokens = expression.split()
    current_tree: Tree = Tree('')
    stack = [current_tree]

    for token in tokens:
        if token == '(':
            tree = Tree("")
            current_tree.insert_left(tree)
            stack.append(current_tree)
            current_tree = tree
        elif token == "not":
            tree.need_to_reverse_result = True
        elif token == ')':
            current_tree = stack.pop()
        elif token in {'and', 'or'}:
            current_tree.root = token
            tree = Tree('')
            current_tree.insert_right(tree)
            stack.append(tree)
            current_tree = tree
        else:
            current_tree.root = token == 'True'
            current_tree = stack.pop()

    return current_tree


def evaluate(tree: Tree):
    operators = {
        '*':  operator.mul,
        '/':  operator.truediv,
        '+':  operator.add,
        '-':  operator.sub,
        'and': operator.and_,
        'or': operator.or_,
        'not': operator.not_,
    }

    if tree.left and tree.right:
        result = operators[tree.root](evaluate(tree.left), evaluate(tree.right))
        if tree.need_to_reverse_result:
            return not result
        return result
    else:
        if tree.need_to_reverse_result:
            return not tree.root
        return tree.root


math_expression = '( ( 1 - 2 ) * 3 )'
bool_expression = '( True or False )'


if __name__ == '__main__':
    tree = parse_expr(math_expression)
    # print(tree)
    new_tree = bool_expr(bool_expression)
    print(f'Result: {evaluate(new_tree)}, {new_tree}')
