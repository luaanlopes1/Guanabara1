# desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.



c = 0

for i in range(1, 7):

    num = int(input('{} - Digite algum número: '.format(i)))
    if num % 2 == 0:
        c += num

print(c)
