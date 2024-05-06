import scipy.optimize as opt


# Definindo uma função de exemplo
def funcao_exemplo(x):
    return x**2 + 3 * x + 2


# Encontrando o mínimo da função usando o método 'minimize'
resultado = opt.minimize(funcao_exemplo, x0=0)

print("Mínimo da função:", resultado.x)
