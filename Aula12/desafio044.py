# Elabore um programa para calcular o valor a ser pago por um produto considerando o seu preco normal e condicao de pagamento
# a vista e dinheiro/cheque: 10% de desconto
# a vista no cartao: 5% desconto
# em ate 2x no cartão: preco normal
# 3x ou mais no cartão: 20% de juros.


produto = int(input('Digite o valor da sua compra: '))



print('DIGITE A FORMA DE PAGAMENTO ABAIXO!')
op1 = int(input('[1] - Escolha a opção para pagamento a vista ou débito.\n[2] - Escolha a opção para pagamento no crédito 1x.\n[3] - Escolha a opção para parcelamento em 2x.\n[4] - Escolha a opção para parcelamento em mais de 3x.\n Escolha a opção de pagamento: '))


    

if op1 == 1:
    print('Você escolheu a forma de pagamento a vista. Você tem um desconto de 10%. Valor a ser pago é de R${}'.format(produto-(produto*0.1)))

elif op1 == 2:
    print('Você escolheu a forma de pagamento no crédito em 1x. Você acaba de ter um desconto de 5%. O valor a ser pago é de R${}'.format(produto-(produto*0.05)))

