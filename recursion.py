# Task 1
from typing import Union


def to_power(x: Union[int, float], exp: int) -> Union[int, float]:
    if exp == 0:
        return 1
    elif exp < 0:
        raise ValueError('This function works only with exp > 0')

    return x * to_power(x, exp - 1)


print(
    to_power(2, 3),
    to_power(3.5, 2),
    to_power(2, -1),
    sep="\n"
)

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
    is_palindrome('radar'),
    is_palindrome('o')
)


# Task 3

def multiply(a: int, n: int) -> int:
    if n == 0:
        return 0
    elif n < 0:
        raise ValueError('This function works only with positive integers')
    return a + multiply(a, n - 1)


print(
    multiply(2, 4),
    multiply(2, 0),
    multiply(5, 55),
    multiply(2, -4),
    sep="\n"
)

# Task 4


def reverse(input_str: str) -> str:
    if len(input_str) == 0:
        return input_str
    else:
        return reverse(input_str[1:]) + input_str[0]


print(
    reverse("hello"),
    reverse("o")
)

# Task 5


def sum_of_digits(digit_string: str) -> int:
    if digit_string == "":
        return 0

    if not digit_string.isdigit():
        raise ValueError("input string must be digit string")

    return int(digit_string[0]) + sum_of_digits(digit_string[1:])


print(
    sum_of_digits('263'),
    sum_of_digits('test'),
    sum_of_digits(''),
    sep="\n"
    )
