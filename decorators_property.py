from functools import wraps


# Task - 1


class Email:
    def __init__(self, email):
        self.email = email
        self.validate()

    def validate(self):
        if '.' and '@' in self.email and self.email[0] != '@':
            return self.email
        else:
            print('Please enter valid email')
            return False


new_email = Email('hello@world.com')
print(new_email.validate())
assert new_email.validate()


# Task - 2


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    def __str__(self):
        return self.name

    def add_workers(self, worker: 'Worker'):
        self.workers.append(worker)


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = boss
        self.full_worker_info = self.get_worker_info

    def __repr__(self):
        return self.name

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, boss: Boss):
        if isinstance(boss, Boss):
            self._boss = boss
            boss.add_workers(self)

    @property
    def get_worker_info(self):
        return {self.id: {self.name: self.company}}


boss1 = Boss(0, 'Petya', 'Soft')
worker1 = Worker(1, "Vasya", "Soft", boss1)
worker2 = Worker(2, "Jojo", "Serve", boss1)
worker1.boss = boss1

print(worker1.boss)
print(boss1.workers)

# Task - 3


class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def transform_to_int(*args):
            try:
                return int(*args)
            except Exception as e:
                print(f'Enter something that equivalent with number. {e}')
                return False

        return transform_to_int

    @staticmethod
    def to_str(func):
        @wraps(func)
        def transform_to_str(*args):
            try:
                return str(*args)
            except Exception as e:
                print(f'Enter something that equivalent with string. {e}')
                return False

        return transform_to_str

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def transform_to_bool(*args):
            try:
                return bool(*args)
            except Exception as e:
                print(f'Enter something that equivalent with bool. {e}')
                return False

        return transform_to_bool

    @staticmethod
    def to_float(func):
        @wraps(func)
        def transform_to_float(*args):
            try:
                return float(*args)
            except Exception as e:
                print(f'Enter something that equivalent with float. {e}')
                return False

        return transform_to_float


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_str
def do_to_string(arg):
    return arg


@TypeDecorators.to_bool
def do_something(string: str):
    return string


@TypeDecorators.to_float
def do_to_float(string: str):
    return string


assert do_nothing('25') == 25
assert do_to_string(25) == '25'
assert do_something('123')
assert do_to_float('2.5') == 2.5
