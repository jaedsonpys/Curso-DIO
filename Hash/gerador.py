import hashlib
from time import sleep

text_for_hash = str(input('Texto a ser gerado em hash: ')).encode('utf-8')

print('\n ## MENU - ESCOLHA O TIPO DE HASH ## ')
print('''
    [ 1 ] md5
    [ 2 ] sha256
    [ 3 ] sha512
    [ 4 ] sha1
''')

option = input('Sua opção: ').strip()
hash_type = ''

if not option.isnumeric():
    print('Escolha a opção em número e tente novamente.')
elif option == '1':
    hash_result = hashlib.md5(text_for_hash)
    hash_type = 'md5'
elif option == '2':
    hash_result = hashlib.sha256(text_for_hash)
    hash_type = 'sha256'
elif option == '3':
    hash_result = hashlib.sha512(text_for_hash)
    hash_type = 'sha512'
elif option == '4':
    hash_result = hashlib.sha1(text_for_hash)
    hash_type = 'sha1'
else:
    print('Selecione uma opção válida e tente novamente.')

print('-='*20)
print('Resultado:\n')

print(f'Hash: {hash_result.hexdigest()}')
print(f'Tipo de hash: {hash_type}')
