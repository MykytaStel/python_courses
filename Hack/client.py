import requests
from dataclasses import dataclass
import json


@dataclass
class User:
    username: str
    message: str

    def as_dict(self):
        return dict(
            username=self.username,
            message=self.message,
        )


URL = 'http://127.0.0.1:5000/index'
user_name_input = input('Enter your name: ')

while 1:
    user = User(
        username=user_name_input,
        message=input("Enter your message: "),
    )

    requests.post(URL, bytes(json.dumps(user.as_dict()), encoding='UTF-8'))
