#escreva um programa para aprovar o emprestimo bancario para a comrpa de uma casa. O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.

# calcule o valor da prestacao mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado.!!

# 1º Passo - Perguntar Valor da Casa
# - Salarario do comprador
# - Quantos anos ele pretender pagar
# criar uma condição para calcular a prestação mensal
# criar outra condição caso exceda 30% do salario o emprestimo vai ser negado.

casa = int(input('Qual o valor da casa? '))
salario = int(input('Qual o salário do comprador? '))
anos = int(input('Quantos anos deseja parcelar o financimaneto? '))

prestacao = round(casa / (anos*12), 2)

print('PARABÉNS! Seu emprestimo foi aprovado. O valor da prestação é de R${} por {} anos.'.format(prestacao, anos))

if prestacao > (salario*0.3):
    print('Infelizmente seu emprestimo foi negado. ')