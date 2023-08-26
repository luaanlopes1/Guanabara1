#desenvolva um programa que pergunte a distancia de uma viagem em KM. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km. e R$0,45 para viagens mais longas.

distancia = int(input('Qual a distancia da sua viagem? '))

if distancia <200:
    print('O valor cobrado da passagem é de R$0,50 por km. Logo a sua passagem vai ser {}'.format(distancia*0.50))
else:
    print('O valor cobrado de uma passagem mais longa é de R$0,45 por km. Logo a sua passagem vai ser {}'.format(distancia*0.45))