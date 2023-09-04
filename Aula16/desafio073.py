times = ('Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo', 'Fluminense', 'Bragantino', 'Athletico-PR', 'Cuiabá', 'São Paulo', 'Cruzeiro', 'Corinthians', 'Internacional', 'Goiás', 'Bahia', 'Santos', 'Vasco', 'Coritiba', 'América-MG')




# os cinco primeiros colocados usando o fatimaneto :5
print(f'Os cincos primeiros colocados da tabela são: {times[:5]}\n')

# os 4 ultimos colocados da tabela
print(f'Os quatros últimos colocados da tabela são: {times[-4:]}\n')

# lista com os times em ordem alfabetica
print(f'A lista ordenada alfabetica é: {sorted(times)}')

# saber qual posição está o time chapeco


print(f'O time Corinthians está na {times.index("Corinthians")+1} posição.')