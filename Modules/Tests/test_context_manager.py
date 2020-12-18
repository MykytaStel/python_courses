from unittest import TestCase
from context_manager import LikeOpen
import os


class TestContextManager(TestCase):
    text_file = 'my-file.txts'

    def setUp(self) -> None:
        self._open = LikeOpen(self.text_file, 'r')

    def test_file_name(self):
        self.assertEqual(self.text_file, self._open.file_name)

    def test_access_method(self):
        access_method = 'r'
        self.assertEqual(access_method, self._open.access_method)

    def test_enter_method(self):
        with self.assertRaises(ValueError):
            with self._open as f:
                f.readlines()
