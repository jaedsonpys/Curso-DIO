import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket criado com sucesso')

host = 'localhost'
port = 3000

# faz a ligação entre cliente e servidor através do host e porta
sock.bind((host, port))

while True:
    # aguarda dados a serem recebidos
    data, address = sock.recvfrom(4096)

    if data is not None:
        # enviando uma mensagem para o mesmo cliente
        # que estabeleceu uma conexão
        print(f'Cliente: {data}')
        print(f'Address: {address}')
        sock.sendto(data, address)