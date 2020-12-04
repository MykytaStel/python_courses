# School - Task - 1
class Person:
    def __init__(self, name: str):
        self.name = name
        self._time = 24

    def get_name(self):
        return self.name

    def calc_free_time(self, time: int):
        return self._time - int(time)


class Student(Person):
    def __init__(self, name: str, faculty: str):
        super().__init__(name)
        self.faculty = faculty

    def what_i_must_eat(self):
        return f"You are a student - eat knowledge's of your faculty - {self.faculty}"


class Teacher(Person):
    def __init__(self, name, works_days: int = 1, salary: int = 100):
        super().__init__(name)

        self._salary = salary
        self._works_days = works_days

    def calculate_salary(self):
        salary_by_days = self._works_days * self._salary
        return salary_by_days


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


# Task - 3 Store

class Product:
    def __init__(self, type: str, name: str, price):
        self.type = type
        self.name = name
        self.price = price

    def get_predefined_price(self):
        return self.price * 0.3


class ProductStore:
    def __init__(self):
        self.products = []

    def percentage(self, percent, whole):
        return (percent * whole) / 100.0

    def add(self, product, amount):
        products = {product.type: {
            product.name: product.price + self.percentage(30, product.price),
            'amount': amount
        }}

        self.products.append(products)

    def set_discount(self, identifier, percent, identifier_type='name'):
        pass

    def sell(self, product_name, amount):
        pass

    def get_income(self):
        pass

    def get_all_products(self):
        pass

    def get_product_info(self, product_name):
        pass


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
p3 = Product('Sport', 'Ball', 200)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.add(p3, 12)
s.sell('Ramen', 10)

print(s.products)
# assert s.get_product_info('Ramen') == ('Ramen', 290)

# Task 4 - Custom exception


class CustomException(Exception):
    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


def logger(msg):
    f = open("logs.txt", "a+")
    f.write(f'{msg}\n')
    f.close()


try:
    raise CustomException('Oi it is broken')
except CustomException as e:
    logger(e.msg)
