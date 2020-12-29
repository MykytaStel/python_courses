# Task 1
def binary_search(lst: list, start, end, val):
    lst.sort()
    mid = (start + end) // 2

    if end >= start:
        if arr[mid] == val:
            return mid

        elif lst[mid] > val:
            return binary_search(lst, start, mid + 1, val)
        else:
            return binary_search(lst, mid - 1, end, val)
    else:
        return False


arr = [2, 3, 4, 10, 40]
x = 10

result = binary_search(arr, 0, len(arr), x)
# print(result)


# Task 2
def fibonacci_search(search_array, val):
    fib_2, fib_1 = 0, 1

    while fib_2 + fib_1 < len(arr):
        fib_2, fib_1 = fib_1, fib_2 + fib_1

    offset = 0

    while fib_1 > 0:

        if search_array[offset + fib_2] == val:
            return offset + fib_2

        if search_array[offset + fib_2] < val:
            offset += fib_2

        fib_2, fib_1 = fib_1 - fib_2, fib_2

    return -1


array = [2, 3, 4, 10, 42]
x = 11

print('result of search is ->', fibonacci_search(array, x))

# Task 3
# Implement __len__ and __contains__ methods


class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                next_slot = self.re_hash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.re_hash(next_slot, len(self.slots))

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    @staticmethod
    def hash_function(key, size):
        return key % size

    @staticmethod
    def re_hash(old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.re_hash(position, len(self.slots))
                if position == start_slot:
                    stop = True

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __len__(self):
        pass

    def __contains__(self, item):
        for data in self.data:
            if item == data:
                return True
        return False


H = HashTable()
H[54] = "cat"
H[26] = "dog"
H[93] = "lion"
H[17] = "tiger"
H[77] = "bird"
H[31] = "cow"
H[44] = "goat"
H[55] = "pig"
H[20] = "chicken"
print(H.slots)
print(H.data)
print(H[20])
print(H[17])
H[20] = "duck"
print(H[20])
print(H[99])
print('duck' in H)
