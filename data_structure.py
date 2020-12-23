# Task 1

class Stack:
    def __init__(self, new_list: list = None):
        if not new_list:
            new_list = []
        self.items = new_list

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    # For Task 3
    def get_from_stack(self, e):
        if e in self.items:
            # I don't understand, do we need to return value or pop it from a list ?
            # self.items.pop(self.items.index(e)) # <- If pop it from a list
            return e
        else:
            raise ValueError(f'There is no such value in a stack')

    def pop(self):
        items = []
        while not self.is_empty():
            items.append(self.items.pop())
        for item in items:
            self.push(item)
        return items


new_stack = Stack([1, 2, 3, 4, 5])

print(new_stack.pop())

# Task 2


def brackets_balanced(seq):
    stack = []

    for char in seq:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False

            current_char = stack.pop()

            if current_char == '(':
                if char != ")":
                    return False

            if current_char == '{':
                if char != "}":
                    return False

            if current_char == '[':
                if char != "]":
                    return False

    return 'Balanced'


print(brackets_balanced('()'))
print(brackets_balanced('({)'))


# Task 3
class Queue:
    def __init__(self, new_items: list = None):
        if not new_items:
            new_items = []
        self.items = new_items

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def get_from_stack(self, e):
        if e in self.items:
            # I don't understand, do we need to return value or pop it from a list ?
            # self.items.pop(self.items.index(e)) # <- If pop it from a list
            return e
        else:
            raise ValueError(f'There is no such value in a stack')

    def dequeue(self):
        return self.items.pop()


stack_for_3_task = Stack(['e', '@', 2, 4])
queue = Queue(['1', 2, 3, 'j'])

print(stack_for_3_task.get_from_stack(2))
print(queue.get_from_stack(3))
