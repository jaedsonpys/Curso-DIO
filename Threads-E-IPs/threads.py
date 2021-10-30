from threading import Thread
from time import sleep

def car(vel, pilot):
    traject = 0

    while traject <= 100:
        traject += vel
        sleep(.2)
        print(f'Piloto: {pilot}')
        print(f'Km: {traject}\n')


# criando as threads:
# 
# target: função a ser executada
# args: argumentos que vão na função
t_car1 = Thread(target=car, args=[1, 'João'])
t_car2 = Thread(target=car, args=[1.2, 'Lucas'])

# inicia o processo
t_car1.start()
t_car2.start()