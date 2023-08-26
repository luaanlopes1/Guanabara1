#Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra "A" , em que posicao ela aparece a primeira vez e em que posicao ela paarece a ultima vez.


frase = input('Digite alguma frase: ').lower()

print('A frase digitada foi: {}'.format(frase))
print('A frase digitada contém {}x a letra "A"! '.format(frase.count('a')))
print('A letra "A" aparece a primeira vez na posição {}'.format(frase.find('a')+1))
print('A ultima letra "A" apareceu na posição {}'.format(frase.rfind('a')+1))