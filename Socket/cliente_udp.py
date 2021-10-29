import socket

# socket.AF_INET informa que vamos utilizar o IP
# o SOCK_DGRAM informa que utilizaremos o UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Cliente socket criado com sucesso')

host = 'localhost'
port = 3000
message = 'Hello, friend.'

try:
    # definindo tempo limite
    sock.settimeout(5)
    sock.sendto(message.encode(), (host, port))

    # recebendo dados de 4096 bytes do servidor
    data, server = sock.recvfrom(4096)

    # decodificando os dados
    data = data.decode()

    print('Resposta:', data)
except socket.error as err:
    print('Não foi possível estabelecer uma conexão')
    exit()
else:
    print('Socket conectado com sucesso!')
    print(f'{host} - {port}')

    # fecha a conexão após 2 segundos
    sock.close()