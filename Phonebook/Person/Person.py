class Person:
    def __init__(self, first_name: str, last_name: str = None, phone: str = None, city: str = None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.city = city

    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.phone} - {self.city}'

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    @get_full_name.setter
    def get_full_name(self, *args):
        _args = [x for x in args[0]]

        first_name, last_name = _args

        self.first_name = first_name
        self.last_name = last_name


# asd = Person("nik", 'Stel')
#
# asd.get_full_name = 'Vasya', 'Pupkin'
#
# print(asd.get_full_name)