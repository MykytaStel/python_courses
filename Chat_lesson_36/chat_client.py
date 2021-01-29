import socket
import threading

HOST = '10.10.1.64'
PORT = 9091


class ConnectionHandler(threading.Thread):
    def __init__(self, connection: socket.socket):
        super().__init__()
        self.connection = connection

    def run(self, *args, **kwargs):
        while 1:
            data = s.recv(1024)
            if not data:
                break
            print(f'\nEncrypted message: {data.decode()}')


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        ConnectionHandler(s).start()
        while True:
            s.send(str(dict(
                user_name='Nikita',
                message=input('Enter your message:  '),
                recipient=input('Recipient: ')
            )).encode())
    except Exception as e:
        raise e
