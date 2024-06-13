# Listas contendo os dados de ID, quantidade e preço de cada item
id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]

# Inicializa a tabela com o cabeçalho (id, quantidade, preco, total)
tabela = [('id', 'quantidade', 'preco', 'total')]

# Adiciona à tabela os dados de cada item, incluindo o cálculo do total (quantidade * preco)
tabela += [(id[i], quantidade[i], preco[i], quantidade[i] * preco[i]) for i in range(len(id))]

# Imprime a tabela completa
print(tabela)
