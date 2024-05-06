import torch

# Criando um tensor de zeros com tamanho 3x3
tensor_zeros = torch.zeros(3, 3)
print("Tensor de zeros:")
print(tensor_zeros)

# Criando um tensor aleatório com tamanho 2x2
tensor_aleatorio = torch.rand(2, 2)
print("\nTensor aleatório:")
print(tensor_aleatorio)

# Operações com tensores
x = torch.tensor(3.0)
y = torch.tensor(4.0)
soma = x + y
print("\nSoma dos tensores x e y:", soma)

# Multiplicação de tensores
produto = x * y
print("Produto dos tensores x e y:", produto)
