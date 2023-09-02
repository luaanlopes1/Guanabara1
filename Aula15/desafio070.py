#crie um programa que leia o nome e o preço de variso produtos. O programa devera perguntar se o usuario vai continuar no final e mostre:

# qual é o total gasto na compra.
# quantos produtos custam mais de R$1000
# qual é o nome do produto mais barato?


# criar variaveis para ser contador
total = 0
acima = 0
menor = 0
barato = ''
i = 0


# receber o nome e o preço do produto dentro de um laço de repetição

while True:
    produto = input('Qual o produto? ')
    preço = float(input('Qual o preço do produto?'))
    i += 1

    total += preço

    if i == 1 or preço < menor:
        menor = preço
        barato = produto

    if preço > 1000:
        acima += 1
    
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Gostaria de continuar? [S/N] ').upper()
    if continuar == 'N':
        break

print(f'O total gasto nas suas compras foi de R${total}')

if acima == True:
    print(f'Ao todo foram {acima} produtos acima de R$1.000,00 ')
else:
    print('Não teve produtos acima de R$1.000,00')

print(f'O produto mais barato foi {barato} que custa R${menor}')