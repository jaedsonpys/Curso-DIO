# Gerador de senha

import random
import string

length = 64
letters = string.ascii_letters + string.digits + '@!#$&*%'

password = ''.join(random.choice(letters) for i in range(length))
print(password)