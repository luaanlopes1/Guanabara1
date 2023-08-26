#crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar

number = int(input('Digite um número e vou te dizer se é PAR ou IMPAR'))

numero = number % 2

if numero == 0:
    print('Seu número é Par')
else:
    print('Seu número é Impar')