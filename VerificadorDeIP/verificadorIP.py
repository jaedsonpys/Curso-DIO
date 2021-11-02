import json
import requests

req = requests.get('https://ipinfo.io/json')
info_ip = json.loads(req.content.decode())

print('\n\033[31m## NUNCA COMPARTILHE SEU ENDEREÇO IP! ##\033[m\n')

print(f'Seu IP: {info_ip["ip"]}')
print(f'Hostname: {info_ip["hostname"]}')
print(f'Cidade: {info_ip["city"]}')
print(f'País: {info_ip["country"]}')