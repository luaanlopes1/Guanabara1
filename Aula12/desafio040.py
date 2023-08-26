# Criar um programa para ler a media do aluno se foi aprovado ou não


n1 = int(input('Qual a primeira nota do aluno? '))
n2 = int(input('Qual a segunda nota do aluno? '))
media = (n1 + n2) / 2

if media < 5:
    print('O aluno foi reprovado.')

elif media >=5 and media < 7:
    print('O aluno está de recuperação')
else:
    print('O aluno está aprovado! Parabéns')