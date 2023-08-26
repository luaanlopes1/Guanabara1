# faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0. Com uma pausa de 1 segundo entre eles...

from time import sleep

t = int(input('Digite o temporizador que você precisa para iniciar os fogos de artificios: '))

for i in range(t,0, -1):
    print('A contagém {}...'.format(i))
    sleep(1)

print(' ! FIM !')

