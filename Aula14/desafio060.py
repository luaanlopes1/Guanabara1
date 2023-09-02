# faça um porgrama que leia um numero qualquer e motre o seu fatorial ! Ex: 5! = 5x4x3x2x1 = 120






num = int(input('Digite um número para calcular seu Fatorial: '))
c = num
f = 1
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
    
print('O Fatorial de {} é: {}'.format(num, f))






