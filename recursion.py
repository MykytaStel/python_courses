# Task 1
from typing import Optional


def to_power(x: Optional[int, float], exp: int) -> Optional[int, float]:
    if exp == 0:
        return 1
    # >>> to_power(2, 3) == 8
    # True
    #
    # >>> to_power(3.5, 2) == 12.25
    # True
    #
    # >>> to_power(2, -1)
    # ValueError: This function works only with exp > 0.
    # """
    # pass


# Task 2


def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if len(looking_str) <= 1:
        return True
    if index == len(looking_str) // 2:
        return True

    return looking_str[index] == looking_str[-(index + 1)] and \
        is_palindrome(looking_str, index + 1)


print(
    is_palindrome('mom'),
    is_palindrome('sassas'),
    is_palindrome('o')
)


# Task 3

def mult(a: int, n: int) -> int:
    """
    This function works only with positive integers

    >>> mult(2, 4) == 8
    True

    >>> mult(2, 0) == 0
    True

    >>> mult(2, -4)
    ValueError("This function works only with postive integers")
    """


# Task 4


def reverse(input_str: str) -> str:
    """
    Function returns reversed input string
    >>> reverse("hello") == "olleh"
    True
    >>> reverse("o") == "o"
    True
    """


# Task 5


def sum_of_digits(digit_string: str) -> int:
    """
    >>> sum_of_digits('26') == 8
    True

    >>> sum_of_digits('test')
    ValueError("input string must be digit string")
    """
