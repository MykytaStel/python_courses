import unittest
from Phonebook.Person.Person import Person


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person('Vasya', 'Pupkin', '+38099', 'Kyiv')

    def test_person_first_name(self):
        first_name = "John"
        person = Person(first_name)
        self.assertEqual(first_name, person.first_name)

    def test_person_last_name(self):
        first_name = "John"
        last_name = "Doe"
        person = Person(first_name, last_name)
        self.assertEqual(last_name, person.last_name)

    def test_person_phone(self):
        phone = "+38099"
        person = Person(self.person.first_name, phone)
        if person.phone is None:
            phone = None
        self.assertEqual(phone, person.phone)

    def test_person_city(self):
        city = 'San-Fransisco'
        person = Person(self.person.first_name)
        if person.city is None:
            city = None
        self.assertEqual(city, person.city)

    def test_get_full_name(self):
        first_name = 'John'
        last_name = "Doe"
        full_name = f'{first_name} {last_name}'
        person = Person(first_name, last_name)
        self.assertEqual(full_name, person.get_full_name)

