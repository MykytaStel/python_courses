from typing import List, Set, Iterable
# Example 1


def choose_func(nums: Iterable[int], func1, func2) -> List[int]:
    if all(num > 0 for num in nums):
        return func1(nums)
    else:
        return func2(nums)


nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def square_nums(nums: Iterable[int]) -> List[int]:
    return [num ** 2 for num in nums]


def remove_negatives(nums: Iterable[int]) -> List[int]:
    return [num for num in nums if num > 0]


assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]

# Example 2


def example_2() -> None:
    print('I am example - 2')


example_2()

# Example 3


def example_3(names: Set[str]) -> Set[str]:
    print(names)
    return names


new_names = {'vasya', 'petya', 'pu'}
n_names = 3


example_3(new_names)
example_3(n_names)  # type warning
