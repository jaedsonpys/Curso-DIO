# Comparador de hash

import hashlib

# abrindo arquivos
arq1 = open('Hash/arquivo1.txt', 'rb')
arq2 = open('Hash/arquivo2.txt', 'rb')

# definindo o algoritmo a ser usado
hash1 = hashlib.new('md5')
hash2 = hashlib.new('md5')

# gerando o hash
hash1.update(arq1.read())
hash2.update(arq2.read())

# o digest resume os dados definidos pelo hash.update()
# hexdigest mostra o hash em hexadecimal
if hash1.digest() != hash2.digest():
    print('Hash não são iguais')
    print(hash1.hexdigest())
    print(hash2.hexdigest())
else:
    print('Hash são iguais!')
    print(hash1.hexdigest())
    print(hash2.hexdigest())

# fechando arquivos
arq1.close()
arq2.close()