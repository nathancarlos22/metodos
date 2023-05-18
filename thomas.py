import numpy as np

def thomas(A, b):
    # Verifica se os tamanhos de A e b são compatíveis
    n = len(A)
    if n != len(b) or n != len(A[0]):
        raise ValueError("O tamanho da matriz A e o vetor b deve ser compatível.")

    # Verifica se a matriz A é tridiagonal
    for i in range(n):
        for j in range(n):
            if i > j+1 or i < j-1:
                if A[i][j] != 0:
                    raise ValueError("A matriz A deve ser tridiagonal.")

    # Cria os vetores a, b_, c, d e x
    a = np.zeros(n-1)
    b_ = np.zeros(n)
    c = np.zeros(n-1)
    d = np.zeros(n)
    x = np.zeros(n)

    # Inicializa os vetores a, b_, c e d com os coeficientes da matriz A e do vetor b
    for i in range(n):
        if i == 0:
            b_[i] = A[i][i]
            c[i] = A[i][i+1]
            d[i] = b[i]
        elif i == n-1:
            a[i-1] = A[i][i-1]
            b_[i] = A[i][i]
            d[i] = b[i]
        else:
            a[i-1] = A[i][i-1]
            b_[i] = A[i][i]
            c[i] = A[i][i+1]
            d[i] = b[i]

    # Etapa de eliminação
    for i in range(1, n):
        m = a[i-1] / b_[i-1]
        b_[i] -= m * c[i-1]
        d[i] -= m * d[i-1]

    # Etapa de substituição inversa
    x[n-1] = d[n-1] / b_[n-1]
    for i in range(n-2, -1, -1):
        x[i] = (d[i] - c[i] * x[i+1]) / b_[i]

    return x
