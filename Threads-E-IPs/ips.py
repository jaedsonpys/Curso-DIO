# biblioteca para manipulação de IPs
import ipaddress

IP = '192.168.0.0/24'
# endereço = ipaddress.ip_address(IP)

# print(endereço)
# print(endereço + 255)

print('-='*20)

network = ipaddress.ip_network(IP)
print(network)

print('-='*20)

# mostra todos os IPs da rede
for i in network:
    print(i)