# faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Ex: Digite um numero: 1834
# unidade :4
# dezena: 3
# centena: 8
# milhar: 1

num = int(input('Digite um número entre 0 e 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Centena: {}'.format(d))
print('Dezena: {}'.format(c))
print('Milhar: {}'.format(m))