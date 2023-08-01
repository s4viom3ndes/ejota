import pandas as pd

caminho = "likes.csv"

dataframe = pd.read_csv(caminho)

print(dataframe)

# pegando a coluna User_id e inserindo em uma lista
listUser_id = dataframe["user_id"].tolist()

print(listUser_id)

# normalizando dados inseridos na lista

# calculando a media
soma = 0

soma = sum(listUser_id)
print(soma)
media = soma/len(listUser_id)
print(media)

menor = min(listUser_id)
maior = max(listUser_id)

normalizacao = (listUser_id(1) - menor)/(maior - menor)
print(f'normalizacao = {normalizacao}')
