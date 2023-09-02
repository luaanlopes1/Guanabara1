# crie um prgraoa que leia a idade e o sexo de varias pessoas.
# a cada pessoa cadastrada o programa devera perguntar se o usuario quer ou nao continuar.
# no final, mostre: 

# quantas pessoas tem mais de 18 anos
# quantos homens foram cadstrados
# quantas mulheres tem menos de 20 anos

contador_idade = 0
contador_sexo_F = 0
contador_sexo_M = 0
contador_sexo_fem = 0

while True:
    # criando a idade e o sexo das pessoas dentro do laço de repetição While

    idade = int(input('Qual sua idade? '))
    sexo = input('Qual o seu sexo? [M/F] ').upper()

    if idade > 18:
        contador_idade +=1

    if sexo == 'M':
        contador_sexo_M += 1

    if sexo == 'F':
        contador_sexo_F += 1

    if idade < 20 and sexo == 'F':
        contador_sexo_fem += 1

    # gostaria de continuar?

    continuar = input('Você gostaria de continuar cadastrando? [S/N] ').upper()
    if continuar == 'N':
        break

print (f'São exatas {contador_idade} pessoas acima de 18 anos.')
print(f'São exatos {contador_sexo_M} Homens cadastrado no sistema.')
if contador_sexo_fem > 1:
    print(f'Ao todo foram cadastradas {contador_sexo_fem} mulhere(s) com idade inferior a 20 anos')
else:
    print('Não foram cadastradas mulheres com idade inferior a 20 anos.')

