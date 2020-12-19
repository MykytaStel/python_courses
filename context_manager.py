# Task 1
from contextlib import contextmanager
import pytest


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
        pass
    finally:
        print('FINALLY')
        if file:
            file.close()



# text_file = 'my-file.txt'
# @pytest.fixture
# def file_lines():
#     with file_opener(text_file) as f:
#         yield f.readlines()
#     f.close()
#
#
# def test_has_lines(file_lines):
#     print(file_lines)
#     assert len(file_lines) >= 1
#
#
# def test_is_result_str(self):
#     assert isinstance(self.result, str)

simple_dict = {
        "name": "Petro",
        "last_name": "Petro",
        "age": '32'
    }


def simple_function(file_obj: dict) -> str:
    return '2'


simple_function(simple_dict)