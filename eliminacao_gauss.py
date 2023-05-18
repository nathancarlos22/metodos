import numpy as np

def eliminacao_gauss(A, b):
    # Verifica se os tamanhos de A e b são compatíveis
    n = len(A)
    if n != len(b) or n != len(A[0]):
        raise ValueError("O tamanho da matriz A e o vetor b deve ser compatível.")

    # Verifica se algum elemento da diagonal principal da matriz A é zero
    for i in range(n):
        if A[i][i] == 0:
            raise ValueError("Os elementos da diagonal principal da matriz A não devem ser zero.")

    # Etapa de eliminação
    for i in range(n-1):
        for j in range(i+1, n):
            if A[j][i] != 0:
                fator = A[j][i] / A[i][i]
                A[j][i:] -= fator * A[i][i:]
                b[j] -= fator * b[i]

    # Etapa de substituição inversa
    x = np.zeros(n)
    x[n-1] = b[n-1] / A[n-1][n-1]
    for i in range(n-2, -1, -1):
        x[i] = (b[i] - np.dot(A[i][i+1:], x[i+1:])) / A[i][i]

    return x
