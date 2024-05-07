import pandas as pd


data = {"x": [1, 2, 3], "y": [3, 7, 11], "z": [False, True, False]}

df = pd.DataFrame(data)
# print(df)

# vai retornar true para todos os valores False
m = df["z"] == False


ef = df[m]


ff = ef[["x", "y"]]

print(ff)


#    x   y
# 0   1   3
# 2   3   11
