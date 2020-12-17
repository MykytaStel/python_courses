from pytest import fixture
from unittest import TestCase
from Phonebook.phonebook import Phonebook


class TestPhoneBook(TestCase):
    phonebook_name = 'Phonebook.txt'

    @classmethod
    def setUpClass(cls) -> None:
        cls.simple_phonebook = Phonebook(cls.phonebook_name, auto_create=True)
        cls.test_person = {
            "first_name": "name2",
            "last_name": "name2",
            "phone": "name2",
            "city": "name2",
        }

    def test_phonebook_name(self):
        self.assertEqual()

