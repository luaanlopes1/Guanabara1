#crie um programa que leia 2 valores. e mostre um menu na tela:
#somar
#multiplicar
#3 maior
#novos numeros e 5 sair do programa




n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

op = 0
while op != 5:

    print('''
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA    
    ''' )
    op = int(input('Qual sua opção?\n'))

    if op == 1:
        print('Você selecionou a opção SOMAR. Logo o resultado é: {}'.format(n1+n2))

    elif op == 2:
        print('Você selecionou a opção MULTIPLICAR. Logo o resultado é: {}'.format(n1*n2)) 

    elif op == 3:
        if n1 > n2:
            print('Você selecionou a opção MAIOR e o número maior é: {}'.format(n1))
        else:
            print('Você selecionou a opção MAIOR e o número maior é: {}'.format(n2))

    elif op == 4:
        print('Digite novamente os números:')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    elif op == 5:
        print('Finalizando...')
    
    else:
        print('Opção inválida. Tente novamente!')


print('FIM DO PROGRAM!!')



