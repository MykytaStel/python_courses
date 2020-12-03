# Task 1
#
# Method overloading.
from types import MethodType
from abc import ABC


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


def enter_sound(self):
    return input('Please, enter new sound =>')


def generic_func(inst):
    inst.talk = MethodType(enter_sound, inst)


print(generic_func(cat))
print(cat.talk())

# Task 2 - Library


class Author:
    def __init__(self, name, country, birthday, books=[]):
        self.name = name
        self.country = country
        self.country = birthday
        self.books = books

    def __str__(self):
        pass

    def __repr__(self):
        pass


class Library(ABC):
    def __init__(self, name, books= [], authors= []):
        self.name = name
        self.books = books
        self.authors = authors

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def read(self) -> str:
        raise NotImplementedError

    def new_book(self, name: str, year: int, author: Author):
        pass

    def group_by_author(self, author: Author):
        pass

    def group_by_year(self, year: int):
        pass


class Book:
    EXISTING_BOOKS = {}

    def __init__(self, name, year, author: Author):
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        pass

    def __repr__(self):
        pass



