# Task 1
from contextlib import contextmanager


class LikeOpen:

    def __init__(self, file_name, access_method='r'):
        self.file_name = file_name
        self.access_method = access_method

    def __enter__(self):
        self._file = open(self.file_name, self.access_method)
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()

#  Task 3

# Create pytest fixture,
# which uses your implementation of the context manager to return a file object,
# which could be used inside your function.


@contextmanager
def file_opener(file_name, access_method='r'):
    file = None
    try:
        file = open(file_name, access_method)
        yield file
    except Exception as e:
        print(f'Error - {e}')
    finally:
        print('FINALLY')
        if file:
            file.close()
