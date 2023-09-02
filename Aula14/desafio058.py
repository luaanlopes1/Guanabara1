# melhore o jogo do desafio 028 ande o computador vai 'pensar' em um numero entre 0 e 10. Só que agora o jogador vai adicnhar ate acertar. Mostrando no final quantos palpites foram necessários para vencer.

import random

numero = int(input('Olá, vamos tentar a sua sorte! Tente adivinhar o número que eu escolhi entre 0 e 10, vamos lá: '))
number = random.randint(0, 10) #sorteio de 0 a 10
p = 0

while number != numero:
    p += 1

    numero = int(input(('Você errou, tente novamente: ')))
    

print('Você acertou, parabéns! Você conseguiu com {} tentativas. '.format(p))


