# faça um programa que jogue par ou impar com o computador. O jogo so sera interrompido quando o jogador PERDER. Mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.


# começar perguntando se é par ou impar.

# vamos jogar par ou ímpar]
import random



i = 0
resto = 0
num = 0
lista = [0,1,2,3,4,5,6,7,8,9,10]
while True:
    
    num = int(input('Digite um valor: '))
    computador = random.choice(lista)
    soma = num + computador

    op = input('Par ou Impar? [P/I] ').upper()
    if op == 'P':
        resto = (soma%2) == 0
        if resto == True:
            print(f'Você jogou {num} e o computador {computador}. Total deu {soma} DEU PAR! ')
            print('Você venceu!')
            print('Vamos jogar novamente....')
            i += 1
        else: 
            print(f'Você jogou {num} e o computador {computador}. Total deu {soma} DEU IMPAR! ')
            print('Você perdeu!!')
            break

    if op == 'I':

        resto = (soma%2) == 0
        if resto == False:
            print(f'Você jogou {num} e o computador {computador}. Total deu {soma} DEU IMPAR! ')
            print('Você ganhou!!!')
            print('Vamos jogar novamente....')
            i += 1            
        else:            
            print(f'Você jogou {num} e o computador {computador}. Total deu {soma} DEU PAR! ')
            print('Você perdeu!!')
            break

print(f'GAME OVER! Você ganhou um total de {i} vezes. ')
            



