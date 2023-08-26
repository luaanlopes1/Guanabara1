# Crie um programa de pedra, papel e tesoura.


# Fazer que o computador gere de 1 a 3 ( sendo elas pedra, papel ou tesoura.)
# Ler a opção do jogador
# gerar resultado de quem ganhou

import random
from time import sleep
lista = ['Pedra', 'Papel', 'Tesoura']

print('Vamos la começar... Pedra, Papel, tesooura!')
sleep(1)

print('Eu já pensei e vc?')
computador = random.choice(lista)
player = input('O que você escolhe? Pedra, Papel ou Tesoura? ')

print('JOO')
sleep(1)
print('KEEN')
sleep(1)
print('POO!')

if player == 'Pedra' and computador == 'Pedra':
    print('O jogo deu empate!')

if player == 'Pedra' and computador == 'Papel':
    print('Você Perdeu! {} vence {}.'.format(computador, player))

if player == 'Pedra' and computador == 'Tesoura':
    print('Você ganhou! {} vence {}.'.format(player, computador))

if player == 'Papel' and computador == 'Papel':
    print('O jogo deu empate!')

if player == 'Papel' and computador == 'Tesoura':
    print('Você Perdeu! {} vence {}.'.format(computador, player))

if player == 'Papel' and computador == 'Pedra':
    print('Você ganhou! {} vence {}.'.format(player, computador))

if player == 'Tesoura' and computador == 'Tesoura':
    print('O jogo deu empate!')

if player == 'Tesoura' and computador == 'Pedra':
    print('Você Perdeu! {} vence {}.'.format(computador, player))

if player == 'Tesoura' and computador == 'Papel':
    print('Você ganhou! {} vence {}.'.format(player, computador))