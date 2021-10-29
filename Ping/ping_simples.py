import os

def test_host(host, request_number) -> None:
	print('\nIniciando...\n')
	os.system(f'ping -c {request_number} {host}')

print('\n\033[47;30m Ping Test \033[m\n')

host = str(input('Digite o HOST: ')).strip()
req_number = int(input('Quantidade de requisições (Ex: 6): '))

test_host(host, req_number)