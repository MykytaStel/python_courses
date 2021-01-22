import socket
from ceasar import cesar

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Socket successfully created")
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print('data', data)
            if not data:
                break

            new_data = cesar(data)
            print('hello', new_data)
            conn.sendall(bytes(new_data, encoding='utf-8'))
