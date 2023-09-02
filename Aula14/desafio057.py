# faça um programa que leia o sexo de uma pessoa, mas so aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.


m = 'M'
f = 'F'

sexo = input('Informe seu sexo: [M/F] ').strip().upper()


while sexo not in 'MmFf':
    sexo = input('Dados incorretos. Por favor, informe seu sexo: ').strip().upper()

print('Sexo {} registrado com sucesso. '.format(sexo))



