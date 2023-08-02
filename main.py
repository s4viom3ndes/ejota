import pandas as pd

caminho = "likes.csv"

dataframe = pd.read_csv(caminho)

print(dataframe)

# pegando a coluna User_id e inserindo em uma lista
listUser_id = dataframe["user_id"].tolist()
print(type(listUser_id))
print(listUser_id)

# normalizando dados inseridos na lista

menor = min(listUser_id)
maior = max(listUser_id)
print(menor)
print(maior)
normalizacao = []
#
tam = len(listUser_id)
cont = 0
#
for valor in listUser_id:

    list_indx = (listUser_id[cont] - menor)/(maior-menor)
    cont = cont + 1
    normalizacao.append(list_indx)

print(f'normalizacao = {normalizacao}')

# deletando coluna

dataframe.pop('photo_id')
print(dataframe)

#  Criando coluna

dataframe['Dados'] = 'NGM SEGURA B)'
dataframe['valor'] = 12
dataframe['qtd de produtos'] = 2
dataframe['valor/produtos'] = dataframe['valor'] / dataframe['qtd de produtos']
dataframe['bool'] = False
print(dataframe)
if dataframe['bool'].bool() == False:

    dataframe['bool'] = 'sim'


print(dataframe)
