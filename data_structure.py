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

    def pop(self):
        items = []
        while not self.is_empty():
            items.append(self.items.pop())
        for item in items:
            self.push(item)
        return items


new_stack = Stack([1, 2, 3, 4, 5])

print(new_stack.pop())

