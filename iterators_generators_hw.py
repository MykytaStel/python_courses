# Task 1
# Create your own implementation of a built-in function enumerate,
# named `with_index`, which takes two parameters: `iterable` and `start`, default is 0.
# Tips: see the documentation for the enumerate function

def with_index(iterable, start=0):
    for i in range(len(iterable)):
        yield start+i, iterable[i]


grocery = ['bread', 'milk', 'butter']
enumerateGrocery = with_index(grocery, 10)

# print(list(enumerateGrocery))

# Task 2
#
# Create your own implementation of a built-in function range, named in_range(),
# which takes three parameters: `start`, `end`, and optional step.
# Tips: See the documentation for `range` function


# def in_range(start, end, step=1):
#     if start > end:
#         raise StopIteration
#
#     for start in range(end):
#         yield start + step


def in_range(start, end, step=1):

    if end is None:
        stop = start + 0
        start = 0

    if step is None:
        step = 1

    while True:
        if step > 0 and start >= end:
            break
        elif step < 0 and start <= end:
            break
        yield start
        start = start + step


list_num = in_range(0, 100)

for num in list_num:
    print(num)

# Task 3
#
# Create your own implementation of an iterable,
# which could be used inside for-in loop. Also,
# add logic for retrieving elements using square brackets syntax.

