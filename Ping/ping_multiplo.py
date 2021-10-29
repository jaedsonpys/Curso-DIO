from os import system

def test_host(host, request_number) -> None:
	print('\nIniciando...\n')
	system(f'ping -c {request_number} {host}')

print('\n\033[47;30m Ping Test \033[m\n')

with open('Ping/list_ping.txt', 'r') as ping_list:
    for p in ping_list.readlines():
        test_host(p, 3)