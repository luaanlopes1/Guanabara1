
import random



nome1 = input('Quuem é o primeiro aluno?')
nome2 = input('Quem é o segundo aluno?')
nome3 = input('Quem é o terceiro aluno?')
nome4 = input('Quem é o quarto aluno?')

lista = [nome1, nome2, nome3, nome4]


escolhido = random.choice(lista)

print('Os nomes são: {}'.format(escolhido))
