#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#O nome com todas as letras maisculas
#O nome com todas minusculas
#Quantas letras ao todo ( sem considerar espaços)
#Quantas lestras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome em maisculas é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome)-nome.count(' ')))

separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))




