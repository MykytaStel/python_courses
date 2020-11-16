# === Task - 1 Favorite movie === #


def favorite_movie(movie_name: str):
    # print(f'My favorite movie is named {movie_name}')
    return f'My favorite movie is named {movie_name}'


print(favorite_movie('Die Hard'))

# === Task - 2 Creating a dictionary === #


def make_country(country: str, capital: str):
    new_dict = {country: capital}
    for key, value in new_dict.items():
        print(f'capital of {key} is {value}')
    return new_dict


print(make_country('Ukraine', 'Kyiv'))

# Task -3 A simple calculator #


def subtract_numbers(sub_num):

    initial = 0

    for number in sub_num:
        initial -= number

    return initial


def multiply_numbers(multiply_num):

    initial = 1

    for number in multiply_num:
        initial *= number

    return initial


def calculator(operator: str, *numbers):

    calc_func = {
        '+': sum,
        '-': subtract_numbers,
        '*': multiply_numbers,
    }

    return calc_func[operator](numbers)


print(f'hello: {calculator("-",43, -2, -3)}')
print(f'hello: {calculator("+",43, -2, -3, 4, 5, 6, 7)}')
print(f'hello: {calculator("*",43, -2, -3)}')
