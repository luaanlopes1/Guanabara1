# crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.

import random

num = ()
num = random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10)


print(num)
print(f'O menor valor da tupla é: {min(num)}')
print(f'O maximo valor da tupla é: {max(num)}')

