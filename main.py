import pandas as pd

caminho = "likes.csv"

dataframe = pd.read_csv(caminho)

print(dataframe)

# pegando a coluna User_id e inserindo em uma lista
listUser_id = dataframe["user_id"].tolist()

print(listUser_id)

# normalizando dados inseridos na lista

menor = min(listUser_id)
maior = max(listUser_id)
normalizacao = []
for valor in listUser_id:
    valor_indx = (listUser_id[valor] - menor)/(maior - menor)
    normalizacao.append(valor_indx)
print(f'normalizacao = {normalizacao}')
