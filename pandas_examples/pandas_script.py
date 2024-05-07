import pandas as pd

# Criando uma Series

s = pd.Series([1, 3, 5, 7, 9])
# print(s)
# Criando um DataFrame
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
# print("------------------------------------------")
# print(df)


# # Lendo dados de um arquivo CSV
dados = pd.read_csv("dados.csv")


# # Filtrando dados
dados_filtrados = dados[dados["idade"] > 18]

print(dados_filtrados)


# # Agrupando dados
grupo = dados.groupby("idade").size()

print(grupo)

# pegando apenas colunas específicas

dados_novos = dados_filtrados[["nome", "curso"]]

print(dados_novos)
