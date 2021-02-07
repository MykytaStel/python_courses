from flask import Flask, request, render_template
from datetime import datetime
from dataclasses import dataclass
import json

app = Flask(__name__, template_folder="htmls")
HOST = '127.0.0.1'
PORT = '5000'


class Message:
    def __init__(self, username, message):
        self.time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        self.username = username
        self.message = message

    @classmethod
    def parse_res(cls, data):
        res = json.loads(data)
        return cls(username=res["username"], message=res["message"])

    def __repr__(self):
        return f'time: "{self.time}", username: "{self.username}" message: "{self.message}"'


@dataclass
class DataBase:
    data = []

    def append_db(self, apnd_data):
        self.data.append(apnd_data)


app.db = DataBase()


@app.route('/index', methods=['POST'])
def index():
    result = request.data.decode()
    obj = Message.parse_res(result)
    app.db.append_db(obj)
    print(app.db.data)
    return request.data.decode(), 200


@app.route('/render')
def render_method():
    return render_template('render.html', data=app.db.data)


def not_found(*args, **kwargs):
    print(args, kwargs)
    return 'Error', 404


app.register_error_handler(404, not_found)

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
