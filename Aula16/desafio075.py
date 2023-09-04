#crie um progrmaa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:

# Quantas vezes apareceu o valor 9
# Em que posição foi digitado o primeiro valor
# Quais foram os números pares




    
num = (int(input('Digite um valor: ')),
        int(input('Digite outro valor: ')),
        int(input('Digite mais um valor: ')),
        int(input('Digite o ultimo valor: ')))

# quantas vezes apareceu valor 9    
print(f'O número 9 apareceu {num.count(9)} vezes.')


# em que posição foi digitado o primeiro valor 3
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)+1}º posição')
else:
    print('O valor 3 não foi digitado.')

print('Os pares digitados foram:', end='')
# quais foram os números pares.

for n in num:
    if n % 2 == 0:
        print(n, end=' ')


