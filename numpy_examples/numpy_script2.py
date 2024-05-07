import numpy as np

# Criando um array unidimensional
arr1d = np.array([1, 2, 3, 4, 5])

# Criando um array bidimensional
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


# Acessando elementos do array
# print(arr1d)
# print(arr2d)


# Alturas das pessoas em centímetros
alturas = [160, 170, 155, 180, 175]

# Convertendo a lista em um array do NumPy
alturas_array = np.array(alturas)

# Calculando a média das alturas
media_alturas = np.mean(alturas_array)


print("A média das alturas é:", media_alturas, "cm")
