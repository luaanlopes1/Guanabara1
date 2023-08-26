#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade: 
# se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# se já passou do tempo do alistamento

# Seu programa também devera mostrar o tempo que falta ou que passou do prazo.

# Ano de nascimento 
# Formular para dizer se tem 18 anos
# condicionais para saber o tempo de alistamento

import datetime


data_atual = datetime.datetime.now()
ano = data_atual.date()

idade = int(input('Digite o seu ano de nascimento: '))
data = ano.year - idade


if data < 18:
    print('Você ainda irá se alistar ao serviço militar. Você tem {} anos. Ainda restam {} anos para seu alistamento.'.format(data, (18-data)))
elif data == 18:
    print('Você já se encontra apto para o alistamento! Você já tem {} anos.'.format(data))
else:
    print('Você já passou do prazo para alistamento. Hoje você tem {} anos e você demorou {} anos para procurar o serviço militar.'
          .format(data, (data-18)))