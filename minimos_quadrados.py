import numpy as np

from eliminacao_gauss import eliminacao_gauss

def minimos_quadrados(x, y, grau):
    n = len(x)
    
    if grau < 0 or grau >= n:
        raise ValueError("O grau do polinômio deve estar entre 0 e", n-1)
    
    A = np.zeros((grau + 1, grau + 1))
    b = np.zeros(grau + 1)
    
    # Monta a matriz A e o vetor b do sistema linear
    for i in range(grau + 1):
        for j in range(grau + 1):
            A[i][j] = np.sum(x ** (i + j))
        b[i] = np.sum(y * (x ** i))
    
    # Resolve o sistema linear usando a eliminação de Gauss
    coeficientes = eliminacao_gauss(A, b)
    
    return coeficientes

# Função para calcular o valor do polinômio para um determinado x
def calcular_polinomio(coeficientes, x):
    grau = len(coeficientes) - 1
    resultado = 0.0
    
    for i in range(grau + 1):
        resultado += coeficientes[i] * (x ** i)
    
    return resultado

# Exemplo de uso
# Dados de entrada
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([1.0, 3.0, 2.0, 5.0, 4.0])
grau = 2  # Grau do polinômio de aproximação

# Calcula os coeficientes do polinômio de mínimos quadrados
coeficientes = minimos_quadrados(x, y, grau)

# Imprime os coeficientes
print("Coeficientes do polinômio de mínimos quadrados:", coeficientes)

# Calcula o valor do polinômio para um ponto específico
x_interp = 2.5
valor_interp = calcular_polinomio(coeficientes, x_interp)

print("Valor interpolado em x =", x_interp, ":", valor_interp)
