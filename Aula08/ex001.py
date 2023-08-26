peso = int(input('Digite qual o seu peso: '))
altura = int(input('Digite qual sua altura: '))
resultado = peso/((altura*altura)/10000)

print(f'O reu resultado é: {resultado:.2f}')

if resultado < 18.5:
    print('Você está Abaixo do peso')
elif 18.5 <= resultado < 24.9:
    print('Você está com peso Normal')
elif 25 <= resultado < 29.9:
    print('Você está acima do peso')
elif 30 <= resultado < 34.9:
    print('Você está com Obesidade I')
elif 35 <= resultado < 39.9:
    print('Você está com Obesidade II')
else:
    print('Você está com Obesidade III')