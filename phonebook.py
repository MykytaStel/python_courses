import os
import json


class Phonebook:
    def __init__(self):
        self.phonebook = {}
        self.phonebook_file_name = 'Phonebook.txt'

    def load_all(self):
        self.phonebook.clear()

        if os.path.exists(self.phonebook_file_name):
            file = open(self.phonebook_file_name, 'r')
            for line in file.readlines():
                name, number = line.strip().split()
                self.phonebook[name] = number
        else:
            file = open(self.phonebook_file_name, 'w')

        file.close()

    def add_entry(self):
        self.load_all()

        name = input("ENTER NAME: ")
        number = input("ENTER NUMBER: ")

        new_entry = f"{name} {number}\n"

        file = open(self.phonebook_file_name, 'a')
        file.write(new_entry)
        file.close()

    def read_all(self):
        self.load_all()

        for name, number in self.phonebook.items():
            print(f'{name} {number}')

        if len(self.phonebook) == 0:
            print("PHONEBOOK IS EMPTY")

    def search_entry(self):
        self.load_all()

        search = input("ENTER NAME TO SEARCH FOR: ")

        if search in self.phonebook.keys():
            print(search, self.phonebook[search])
        else:
            print("ENTRY NOT FOUND")
        return

    def delete_entry(self):
        self.load_all()

        entry_to_delete = input("ENTER NAME OF ENTRY TO DELETE: ")

        if entry_to_delete in self.phonebook.keys():
            del self.phonebook[entry_to_delete]

            file = open(self.phonebook_file_name, 'w')

            for name, number in self.phonebook.items():
                string = f"{name}: {number}\n"
                file.write(string)

            file.close()

            print("ENTRY DELETED SUCCESSFULLY")

        else:
            print("ENTRY NOT FOUND")

    @staticmethod
    def exit_program():
        os._exit

    def menu(self):
        print("""\
       -MENU-
1) READ ALL ENTRIES
2) ADD AN ENTRY
3) DELETE AN ENTRY
4) LOOK UP AN ENTRY
5) Exit\n""")

        choice = input("ENTER CHOICE: ")

        choice_menu = {'1': self.read_all,
                       '2': self.add_entry,
                       '3': self.delete_entry,
                       '4': self.search_entry,
                       '5': self.exit_program}

        if choice not in choice_menu.keys():
            print("PLEASE ENTER A VALID CHOICE")
        else:
            choice_menu[choice]()


Book_1 = Phonebook()
Book_1.menu()
