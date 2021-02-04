from typing import List


# Task 1
def bubble_sort(array: List[int]):
    arr_len = len(array)

    for i in range(arr_len - 1):
        token = 0

        for j in range(arr_len - 1):

            if array[j] > array[j + 1]:
                tmp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = tmp
                token = 1

        if token == 0:
            break

    return array


# Task 2
def merge_sort(array: List[int]):
    array_len = len(array)

    if array_len > 1:

        arr_mid = array_len // 2

        left_part = array[:arr_mid]
        right_part = array[arr_mid:]

        merge_sort(left_part)
        merge_sort(right_part)

        left_part_len = len(left_part)
        right_part_len = len(right_part)

        i = j = k = 0

        while i < left_part_len and j < right_part_len:
            if left_part[i] < right_part[j]:
                array[k] = left_part[i]
                i += 1
            else:
                array[k] = right_part[j]
                j += 1
            k += 1

        while i < left_part_len:
            array[k] = left_part[i]
            i += 1
            k += 1

        while j < right_part_len:
            array[k] = right_part[j]
            j += 1
            k += 1

    return array


if __name__ == '__main__':
    arr_numbers = [109, 21, 1, 2, 5, 9]
    print(f'Merge sort: {merge_sort(arr_numbers)} \
            Bubble_sort: {bubble_sort(arr_numbers)}', sep="\n")
