#Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escohlido pelo computador.
# O programa devera escrever na tela se o usuario venceu ou perdeu.


import random

numero = int(input('Olá, vamos tentar a sua sorte! Tente adivinhar o número que eu escolhi entre 0 e 5, vamos lá: '))
number = random.randint(0, 5) #sorteio de 0 a 5



if numero == number:
    print('PARABÉNS!! O seu número digitado foi: {} e o número sorteado foi {}'.format(numero,number))
else:
    print('Você erroou! O número sorteado foi {}'.format(number))
