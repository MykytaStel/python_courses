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


# Task - 3 Store
# Task 3
#
# Product Store
#
# Write a class Product that has three attributes:
#
# type
# name
# price
# Then create a class ProductStore, which will have some Products and will
# operate with all products in the store. All methods, in case they can’t perform its action,
# should raise ValueError with appropriate error information.
#
# Tips: Use aggregation/composition concepts while implementing the ProductStore class.
# You can also implement additional classes to operate on a certain type of product, etc.
#
# Also, the ProductStore class must have the following methods:
#
# add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
# set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers (type or name).
# The discount must be specified in percentage
# sell_product(product_name, amount) - removes a particular amount of products from the store if available,
# in other case raises an error. It also increments income if the sell_product method succeeds.
# get_income() - returns amount of many earned by ProductStore instance.
# get_all_products() - returns information about all available products in the store.
# get_product_info(product_name) - returns a tuple with product name and amount of items in the store.


class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

    def get_predefined(self):
        return self.price * 0.3


class ProductStore:
    PRODUCTS = []

    def percentage(self, percent, whole):
        return (percent * whole) / 100.0

    def add(self, product, amount):
        products = {product.type: {
            product.name: self.percentage(30, product.price),
            'amount': amount
        }}

        ProductStore.PRODUCTS.append(products)
        print(ProductStore.PRODUCTS)

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
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell('Ramen', 10)


# assert s.get_product_info('Ramen') == ('Ramen', 290)

# Task 4 - Custom exception

class CustomException(Exception):
    def __init__(self, msg):
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
