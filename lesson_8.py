# === Task - 1 === #

def oops():
    simple_list = [0, 1, 2]
    return simple_list[4]


def get_error():
    try:
        oops()
    except IndexError:
        raise Exception("An IndexError occurred.")


def get_error_2():
    try:
        oops()
    except KeyError:
        raise Exception("An IndexError occurred.")


print(get_error())
print(get_error_2())


# === Task 2 === #


def two_numbers_func():
    a = input('Please input first number: ')
    b = input('Please input second number:')

    try:
        int(a) ** 2 / int(b)
    except ValueError:
        raise Exception("This is not a number")
    else:
        try:
            int(a) ** 2 / int(b)
        except ZeroDivisionError:
            raise Exception('Your second argument is zero, this function cant divide by zero')

    return int(a) ** 2 / int(b)


print(two_numbers_func())
