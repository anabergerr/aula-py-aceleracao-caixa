import pandas as pd

# Criando uma Series
s = pd.Series([1, 3, 5, 7, 9])

# Criando um DataFrame
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})


# Lendo dados de um arquivo CSV
dados = pd.read_csv("dados.csv")

# Filtrando dados
dados_filtrados = dados[dados["idade"] > 18]


# Agrupando dados
grupo = dados.groupby("idade").size()

# pegando apenas colunas específicas

dados_novos = dados_filtrados[["idade", "nome"]]
