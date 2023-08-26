# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo". 

## cidade = input('Digite o nome da sua cidade: ')

#if cidade.find('santo') == -1:
#    print('A sua cidade não contém o nome santo. A sua cidade é: {}'.format(cidade))

#else:
#    print('O nome da sua cidade contém santo e é: {}'.format(cidade)) 


cidade = input('Em que cidade você nasceu? ')
print(cidade[:5].upper() == 'SANTO')