import math

peso = int(input('Digite qual o seu peso: '))
altura = int(input('Digite qual sua altura: '))
resultado = peso/((altura*altura)/10000)
resposta = round(resultado)

print('O reu resultado é: '.format(resposta))