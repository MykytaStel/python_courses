# Task 1 - Write a Python program to detect the number of local variables declared in a function.
def local_var_num_detect(*args, **kwargs):
    b = 2
    c = 3

    return len(locals())


local_var_num_detect(1, 2, 3, 4, 5, 6, 7)

print(local_var_num_detect.__code__.co_nlocals)


# Task 2- Write a Python program to access a function inside a function

def simple_function():
    msg = 'I am going into inner and call back'

    def inner_function():
        print(msg)

    inner_function()


simple_function()

# Task 3


def choose_func(nums: list, func1, func2):
    if all(num > 0 for num in nums):
        return func1(nums)
    else:
        return func2(nums)


nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
