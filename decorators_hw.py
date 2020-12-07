# Task 1
from functools import wraps


def logger(func):
    @wraps(func)
    def print_code(*args):
        _args = ', '.join([str(arg) for arg in args])
        return f'{func.__name__} called with {_args}'
    return print_code


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


print(add(1, 2))
print(square_all(1, 2, 3, 4, 5))


# Task 2
def stop_words(words: list):
    def wrapper(f):
        def rename_stop_word(*args):
            func_string = "".join(f(*args)).split()
            for word in words:
                if word in func_string:
                    func_string[func_string.index(word)] = '*'
            return " ".join(func_string)
        return rename_stop_word
    return wrapper


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str):
    return f"{name} drinks pepsi in his brand new BMW !"


print(create_slogan('Steve'))
assert create_slogan("Steve") == "Steve drinks * in his brand new * !"


# Task 3
def arg_rules(type_: type, max_length: int, contains: list):
    def wrapper(f):
        def string_actions(*args):
            print()
            _args = ' '.join([str(arg) for arg in args])
            func_string = " ".join(f(*args).split())

            if not isinstance(*args, type_):
                print(f'You entered not String type of the argument. Your type is: {type(*args)}')
                return False

            elif len(_args) >= max_length:
                print(f'Length of the entered word - {_args} is more than max-length - {max_length}')
                return False

            for contain_symbol in contains:
                if contain_symbol in _args:
                    return func_string
                else:
                    print(f'Your name - {_args} contains forbidden symbols')
                    return False

        return string_actions

    return wrapper


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan(123) is False
assert create_slogan('Nikita') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

