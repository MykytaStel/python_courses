# School - Task - 1
class Person:
    def __init__(self, _name):
        self._name = _name
        self._time = 24
        
    def get_name(self):
        return self._name

    def calc_free_time(self, time: int):
        return self._time - int(time)


class Student(Person):
    def __init__(self, _name, _faculty: str):
        super().__init__(_name)
        self._faculty = _faculty

    def what_i_must_eat(self):
        return f"You are a student - eat knowledge's of your faculty - {self._faculty}"


class Teacher(Person):
    def __init__(self, _name, _works_days: int = 1, _salary: int = 100):
        super().__init__(_name)

        self._salary = _salary
        self._works_days = _works_days

    def calculate_salary(self):
        salary_by_days = self._works_days * self._salary
        return f'this is your salary = {salary_by_days} for {self._works_days} day(s)'


student = Student('Phil', 'Math')
teacher = Teacher('Spencer', 5, 200)

print(teacher.calculate_salary())
print(student.get_name())
print(teacher.get_name())
print(teacher.calc_free_time(12))
print(student.calc_free_time(8))
print(student.what_i_must_eat())

# Math Task - 2


class Mathematician:
    @staticmethod
    def square_nums(nums):
        return [num * num for num in nums]

    @staticmethod
    def remove_positives(nums):
        return [n for n in nums if n < 0]

    @staticmethod
    def filter_leaps(years):
        return [y for y in years if y % 4 == 0 and y % 100 != 0]


m = Mathematician()

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
