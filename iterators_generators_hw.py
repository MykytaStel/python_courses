# Task 1


def with_index(iterable, start=0):
    for i in range(len(iterable)):
        yield start+i, iterable[i]


grocery = ['bread', 'milk', 'butter']
enumerateGrocery = with_index(grocery, 10)

print(list(enumerateGrocery))

# Task 2


def in_range(start, end, step=1):

    if not end:
        start, end = 0, start

    while True:
        if step > 0 and start >= end:
            break
        elif step < 0 and start <= end:
            break
        elif step == 0:
            return

        yield start

        start += step


list_num = in_range(2, -10, 0)

for num in list_num:
    print('num', num)

# Task 3

something = [0, 1, 2, 3, 4, 5, 6, 7]

