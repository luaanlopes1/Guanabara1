# faça um programa que mostre a tabuada de vários números um de cada vez para cada valor digitado pelo usuario. O programa sera interrompido quando o numero solicitado for negativo!! 

num = 0

i = 0

while num != 999:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    for i in range (1,11):
        print(f'{num} X {i} = {num*i}')

print('Fim')
    
