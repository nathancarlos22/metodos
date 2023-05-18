import numpy as np

def lagrange_interpolation(x, y, x_interp):
    # Verifica se os tamanhos de x e y são iguais
    if len(x) != len(y):
        raise ValueError("Os tamanhos de x e y devem ser iguais.")
    
    n = len(x)
    result = 0.0
    
    for i in range(n):
        # Calcula o valor do polinômio de Lagrange no ponto x_interp
        term = y[i]
        for j in range(n):
            if j != i:
                # Verifica se x[i] não é igual a x[j] para evitar divisão por zero
                if x[i] == x[j]:
                    raise ValueError("Os valores de x não devem ser iguais.")
                
                term *= (x_interp - x[j]) / (x[i] - x[j])
        
        result += term
    
    return result

# Exemplo de uso
# Dados de entrada
x = np.array([1.0, 2.0, 3.0, 4.0])
y = np.array([1.0, 8.0, 27.0, 64.0])

# Ponto para interpolação
x_interp = 2.5

try:
    # Interpolação
    y_interp = lagrange_interpolation(x, y, x_interp)
    print("Valor interpolado em x =", x_interp, ":", y_interp)
except ValueError as ve:
    print(ve)
