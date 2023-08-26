#escreva um programa que leia dois numero inteiros e compare-os mostrando na tela uma mensagem:
# o primeiro valor é maior
# o segundo valor é maior
# - não existe valor maior. Os 2 são iguais.


n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print('O número {} é maior do que o {}.'.format(n1, n2))
elif n2 > n1:
    print('O número {} é maior do que o {}.'.format(n2,n1))
else:
    print('Não existe valor maior. Os dois são iguais!! ')

print('____'*10,)
print('FIM...')
