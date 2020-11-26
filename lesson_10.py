# === A Person class - Task 1 === #

class Person:
    def __init__(self, firstname: str, lastname: str, age: int):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        return f'Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old'


new_person = Person('Nikita', 'Nikita', 27)

print(new_person.talk())


# === Doggy age - Task 2 === #

class Dog:
    age_factor = 7

    def __init__(self, age: int):
        self.age = age

    def human_age(self):
        return self.age * Dog.age_factor


dog_to_human = Dog(12)
dog_to_human2 = Dog(10)

print(f'For human it will be: {dog_to_human.human_age()}')


# === TV controller - Task 3 === #
class TVController:
    CHANNELS = ["BBC", "Discovery", "TV1000"]
