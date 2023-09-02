#crie um programa que que leia vários numeros inteiros pelo teclado. O prgorama só vai parar quando o usuario digitar o valor 999.
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles. Desconsiderando a flag.



soma = 0
num = 0
contador = 0

while num != 999:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    contador += 1
    soma += num

print(f'A soma dos {contador} valores foi de {soma}. ')

