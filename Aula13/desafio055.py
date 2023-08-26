# faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso informados.


# para criar um input para ler 5 informações, podemos usar o loop for.
# foi criado uma lista para adicinar os valores do input acima

lista = []

for i in range(1,6):
    lista.append(int(input('{} - Digite o peso de cinco pessoas: '.format(i))))

print('O menor peso é de {} kgs e o maior peso é de {}kgs.'.format(min(lista), max(lista)))



    

