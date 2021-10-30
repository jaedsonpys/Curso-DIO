# Gerador de senha

import random
import string

length = 16
letters = string.ascii_letters + string.digits + '@!#$&*%'

password = ''.join(random.choice(letters) for i in range(length))
print(password)