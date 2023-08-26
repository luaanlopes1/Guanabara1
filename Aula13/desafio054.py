# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maior idade e quantas ja sao maiores.

maior = 0
menor = 0

for i in range(1,7):
    idade = int(input('{} - Digite a idade de 7 pessoas: '.format(i)))
    

    if idade < 21:
        menor += 1
        #print('São {} pessoas de menor idade'.format(menor))
    else:
        maior += 1
    
print('O numero de pessoas de maior idade são {} e de menor idade são de {}'.format(maior,menor))