i = 0
s = 0

while i != 999:
    i = int(input('Digite um número: '))
    if i == 999:
        break
    s += i


#print('A soma vale {}'.format(s))

print(f'A soma vale {s}')