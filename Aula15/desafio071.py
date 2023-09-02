# crie um prgraoa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao ususario qual sera o valor a ser sacado. ( numero inteiro)

# O programa vai informar quantas cédulas de cada valor serão entregues.

#OBS: Considere que o caixa possui céduas de R$50, R$20, R$10 e R$1

import math

cinquenta = vinte = dez = um = 0
saldo = 0
# perguntar qual o valor a ser sacado
while True:
    saque = int(input('Qual o valor do seu saque? Temos cédulas de R$50,00 - R$20,00 - R$10,00 - R$1,00. '))
    if saque >= 1:
        cinquenta = math.floor(saque/50)
        saldo = saque % 50
        if saldo >= 20:
            vinte = math.floor(saldo/20)
            saldo = saque % 20   
        if saldo >=10:
            dez = math.floor(saldo/10)
            saldo = saque % 10    
        if saldo >=1:
            um = math.floor(saldo/1)
            break
        
print(f'Você vai sacar R${saque}.\n')
if cinquenta >= 1:
    print(f'Você vai sair {cinquenta} notas de R$50,00')
if vinte >= 1:
    print(f'Você vai sair {vinte} notas de R$20,00')
if dez >= 1:
    print(f'Você vai sair {dez} notas de R$10,00')
if um >= 1:
    print(f'Você vai sair {um} notas de R$1,00')


            
