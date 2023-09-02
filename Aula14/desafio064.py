# Crie um prgraoam que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuario digitar o valor 999 que é a condição de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles. Desconsiderando o flag!


soma = 0
num = 0

while num != 999:

    num = int(input('Digite vários valores para somar! Caso queira sair digite 999: '))
    if num == 999:
        break
    soma = soma + num

print('Os valores digitados são de: {}'.format(soma))