import socket
from utils.print_log import print_log

user_name = None

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('localhost', 3000)

def send_message(message: str) -> bool:
    try:
        sock.sendto(message.encode(), address)
    except socket.error as err:
        print_log('Impossível estabelecer uma conexão com o endereço', 'error')
        return False
    else:
        # aguardando resposta eco do servidor
        while True:
            data, server = sock.recvfrom(8024)

            if server is not None:
                print(f'\nVocê: {data.decode()}')
                break


def start():
    global user_name

    if not user_name:
        print('\033[47;30m #### Chat - Bem vindo! #### \033[m\n')
        user_name = str(input('Seu nome de usuário: ')).strip()

    message = str(input('Digite sua mensagem: ')).strip()
    send_message(message)

start()