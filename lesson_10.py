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
    AGE_FACTOR = 7

    def __init__(self, age: int):
        self.age = age

    def human_age(self):
        return self.age * Dog.AGE_FACTOR


dog_to_human = Dog(12)
dog_to_human2 = Dog(10)

print(f'For human it will be: {dog_to_human.human_age()}')


# === TV controller - Task 3 === #
CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    def __init__(self, channels):
        self._channels = channels
        self.channel_index = 0
        self._channels_len = len(channels)

    def first_channel(self):
        self._set_index(0)
        return self._channels[self.channel_index]

    def last_channel(self):
        self._set_index(-1)
        return self._channels[self.channel_index]

    def turn_channel(self, num):
        self._set_index(int(num) - 1)
        return self._channels[self.channel_index]

    def next_channel(self):
        self._set_index(1, '+')
        return self._channels[self.channel_index]

    def previous_channel(self):
        self._set_index(1, '-')
        return self._channels[self.channel_index]

    def is_exist(self, current):
        if isinstance(current, int):
            if int(current) > self._channels_len or 0 > int(current):
                return "NO"
            else:
                return "YES"
        elif isinstance(current, str):
            for channel in self._channels:
                if channel == current:
                    return "YES"
            for channel in self._channels:
                if channel != current:
                    return "NO"

    def current_channel(self):
        return self._channels[self.channel_index]

    def _set_index(self, index, sign=''):
        if sign == '+':
            self.channel_index += int(index)
        elif sign == '-':
            self.channel_index -= int(index)
        else:
            self.channel_index = int(index)


controller = TVController(CHANNELS)

print('1', controller.first_channel())
print('2', controller.last_channel())
print('3', controller.turn_channel(1))
print('4', controller.next_channel())
print('5', controller.previous_channel())
print('6', controller.current_channel())
print('7', controller.is_exist("TV1000"))
