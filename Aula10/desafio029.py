#escreva um programa para ler a velocidade de um carro.

velocidade = int(input('Qual foi a velocidade do carro?'))

multa = (velocidade - 80) * 7



if velocidade > 80:
    print('MULTADO! Você ultrapassou o limite de velocidade, cada km que passou é R$7,00. Você acaba de receber uma multa de R${},00'.format(multa) )
else:
    print('Sua velocidade está abaixo do permitido.')