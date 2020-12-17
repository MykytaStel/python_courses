# Task 1


class LikeOpen:

    def __init__(self, file_name, access_method='r'):
        self.file_name = file_name
        self.access_method = access_method

    def __enter__(self):
        self._file = open(self.file_name, self.access_method)
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()

# Task 2

