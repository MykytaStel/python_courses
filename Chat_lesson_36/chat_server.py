import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('10.10.1.64', 9090)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

while True:
    print('waiting for a connection')

    connection, client_address = sock.accept()
    print("Client (%s, %s) connected" % client_address)
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        data = connection.recv(1024)
        print('received {!r}'.format(data))
        if data:
            print('sending data back to the client')
            connection.send(data)
        else:
            print('no data from', client_address)
            break

    finally:
        print('connection closed')
        connection.close()
