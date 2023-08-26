#Desenvolva um programa que leia o nome, idade e sexo de 4 Pessoas. No final do programa, mostre:
# A media de idade do grupo
# qual é o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos.


somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''



for i in range(1, 3):
    print('----- {}ª PESSOA -----'.format(i))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    somaidade += idade

    if i == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

mediaidade = somaidade / 4

print ('A media de idade do grupo é de {} anos.'.format(mediaidade))
print ('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))


