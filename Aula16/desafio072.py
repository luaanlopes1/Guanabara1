# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.

# Seu programa deverá ler um número pelo teclado ( entre 0 e 20) e mostra-lo por extenso.

# criando a tupla por extenso
tupla = ('zero','um','dois','tres','quatro','cinco'
         ,'seis','sete','oito','nove','dez')

# criando a variavel para digitar o numero



while True:
    num = int(input('Qual o seu número? Digite um número de 1 a 10. '))
    if 0 <= num <= 10:
        break
    print('Tente novamente.')

print(f'Você digitou o número {tupla[num]}')


    




    

