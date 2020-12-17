from unittest import TestCase
from context_manager import LikeOpen


class TestContextManager(TestCase):
    def test_file_name(self):
        file_name = 'Test.txt'
        file_name_open = LikeOpen(file_name)
        self.assertEqual(file_name, file_name_open.file_name)

    def test_access_method(self):
        pass
