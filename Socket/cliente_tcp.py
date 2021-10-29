import socket

# a biblioteca fornece acesso a algumas variáveis e funções do interpretador
import sys 

def main():
    # tentar uma conexão TCP/IP
    try:
        # socket.AF_INET informa que vamos utilizar o IP
        # o SOCK_STREAM informa que utilizaremos o TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print('Erro na conexão:', err)

        # fecha o programa
        sys.exit()

    print('Socket criado com sucesso')

    host = str(input('Digite um host ou IP: ')).strip()
    port = str(input('Digite a porta: ')).strip()

    try:
        # define um tempo limite de conexão
        sock.settimeout(2)

        # conecta ao host e a porta
        sock.connect((host, int(port)))
    except socket.error as err:
        print('Impossível ao conectar ao host selecionado')
        print(f'[error] {host} - {port}')
        
        sys.exit()
    else:
        print('Cliente TCP conectado com sucesso!')
        print(f'[sucess] {host} - {port}')

        # fecha a conexão após 2 segundos
        sock.shutdown(2)

if __name__ == '__main__':
    main()