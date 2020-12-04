# Task 1
#
# Method overloading.
class Animal:
    def talk(self):
        return 'SOME INDISTINCT CHATTER'


class Dog(Animal):
    def talk(self):
        return 'WOOF WOOF'


class Cat(Animal):
    def talk(self):
        return 'MEW MEW'


cat = Cat()
dog = Dog()


def enter_sound():
    return input('Please, enter new sound =>')


def generic_func(inst):
    setattr(inst, 'talk', enter_sound)


print(generic_func(cat))
print(cat.talk())

# Task 2 - Library


class Library:
    BOOK_SHELF = 0

    def __init__(self, name="Library"):
        self.name = name
        self.books = []
        self.authors = []

    def __str__(self):
        return f'{self.name}, {self.books}, {self.authors}'

    def __repr__(self):
        return f'Library("{self.name}, {self.books}, {self.authors})"'

    def new_book(self, name: str, year: int, author: 'Author'):
        book = Book(name, year, author)
        self.books.append(book)
        self.authors.append(author)
        Library.BOOK_SHELF += 1

        return book

    def group_by_author(self, author: 'Author'):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year: int):
        return [book for book in self.books if book.year == year]


class Book:
    def __init__(self, name, year, author: 'Author'):
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        return f'{self.name}, {self.year}, {self.author}'

    def __repr__(self):
        return f'Book("{self.name}, {self.year}, {self.author}")\n'


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday

    def __str__(self):
        return f'{self.name}, {self.country}, {self.birthday}'

    def __repr__(self):
        return f'Author("{self.name}, {self.country}, {self.birthday}"'

    def __eq__(self, other):
        if isinstance(other, Author):
            return Exception('Nit')
        return self.name == other.name and \
            self.country == other.country and \
            self.birthday == other.birthday


author_1 = Author("H.P. Lovecraft", "USA", "20.08.1890")
author_2 = Author("Frank Herbert", "USA", "08.10.1920")
lib = Library()
lib.new_book("The Call of Cthulhu", 1928, author_1)
lib.new_book("The Dunwich Horror", 1929, author_1)
lib.new_book("The Cats of Ulthar", 1920, author_1)
lib.new_book("Dune", 1965, author_2)
lib.new_book("Dune Messiah", 1969, author_2)
print(f'All your books - {lib.books}')
print(f'Books grouped by author: {lib.group_by_author(author_2)}')
print(f'All books by year: {lib.group_by_year(1928)}')
print(f'Your entire Library: {lib}')
print(f'There are {Library.BOOK_SHELF} book(s) in your book shelf')

# Task 3 - Fraction


class Fraction:
    def __init__(self, fraction):
        if isinstance(fraction, str):
            raise Exception("Not a number")
        self.fraction = fraction

    def __str__(self):
        return f"Fraction {self.fraction}"

    def __repr__(self):
        return f'Fraction({self.fraction})'

    def __add__(self, other):
        if isinstance(other, str):
            raise Exception("fraction value is required")
        return self.fraction + other.fraction

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __sub__(self, other):
        if not isinstance(other, str):
            return self.fraction - other.fraction
        else:
            raise ValueError("float value is required")

    def __truediv__(self, other):
        if not isinstance(other, str):
            return self.fraction / other.fraction
        else:
            raise ValueError("float value is required")

    def __mul__(self, other):
        if not isinstance(other, str):
            return self.fraction * other.fraction
        else:
            raise ValueError("float value is required")


x = Fraction(3/2)
y = Fraction(1/4)
print(x * y)
print(x - y)
print(x / y)

# / TODO UNDERSTAND HOW TO IMPLEMENT THIS: assert x + y == Fraction(3/4)
