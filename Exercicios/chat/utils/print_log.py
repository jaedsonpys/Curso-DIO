# um print formatado

def print_log(message, type):
    if type == 'error':
        print(f'\n[ \033[31merror\033[m ] {message}')
    elif type == 'sucess':
        print(f'\n[ \033[32msucess\033[m ] {message}')