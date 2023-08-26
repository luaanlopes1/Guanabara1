# faça um programa que calcule a soma entre todos os numeros impares que sao multiplos de tres e que se encontram no intervalo de 1 até 500.


s = 0

for i in range(1,501, 2):
    if i % 3 == 0:
       s = s + i

print(s)
    