# crie um programa que leia varios numeros inteiros pelo teclado. No final da execucao, mostre a media entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuario se ele quer ou nao continuar a digitar os valores.


# Primeiro criar um input para ler os números





media = 0
contador = 0
resp = 'S'
maior = 0
menor = 0

while resp in 'Ss':

    num = int(input('Digite valores para calcular sua media: '))
    media += num
    contador += 1

    resp = str(input('Quer Continuar? [S/N]')).upper().strip()[0]
    
print('O valor digitado foi de {} e você digitou {} números! A média é de: {}. '.format(media, contador, (media/contador)))

