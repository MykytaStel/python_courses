from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    def __init__(self, data):
        self._payload = data
        self._prev = None
        self._next = None

    def get_data(self):
        return self._payload

    def get_next(self):
        return self._next

    def set_data(self, data):
        self._payload = data

    def set_next(self, new_next):
        self._next = new_next

    def __str__(self):
        return f'{self._payload}'

class TwoWayLinkedList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return bool(self.start_node)

    def append(self, item):
        new_node = Node(item)
        current = self._head

        if current:
            while not current.get_next():
                current = current.get_next()
            current.set_next(new_node)
        else:
            self._head = new_node

    def insert(self, node: Node, index=-1):
        new_node = Node(node)

        if index == -1:
            self.append(new_node)
            return

        if self._head is None:
            self._head = new_node
            new_node._next = self._head
            self._head._prev = new_node
            return

    def __repr__(self):
        representation = "<TwoWayLinkedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()

    # def delete(self, node: Node):
    #     """
    #     remove node from the linkedList
    #     need to work for O(1)
    #     """
    #     raise NotImplemented()


new_l = TwoWayLinkedList()
new_l.insert(2, 0)
