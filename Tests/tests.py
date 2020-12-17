import unittest
import os
from Phonebook.Person import Person


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person('Vasya', 'Pupkin', '+38099', 'Kyiv')

    def test_get_full_name(self):
        self

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
