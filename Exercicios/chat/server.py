import socket 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

address = ('localhost', 3000)
sock.bind(address)

def receive_message():
    while True:
        data, client = sock.recvfrom(8024)

        if client is not None:
            pass