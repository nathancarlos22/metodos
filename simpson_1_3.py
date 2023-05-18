def simpson_1_3_repetido(x, y):
    # Verifique se os tamanhos de x e y são iguais
    if len(x) != len(y):
        raise ValueError("Os tamanhos de x e y devem ser iguais.")
    
    n = len(x)

    # Verifique se o número de pontos é ímpar e maior ou igual a 3
    if n < 3 or n % 2 != 1:
        raise ValueError("O número de pontos deve ser ímpar e maior ou igual a 3.")

    # Certifique-se de que os x's estão espaçados igualmente
    h = x[1] - x[0]
    for i in range(2, n):
        if x[i] - x[i-1] != h:
            raise ValueError("Os valores de x devem ser igualmente espaçados.")
    
    # Aplica a regra de Simpson 1/3 repetido
    integral = 0.0
    for i in range(0, n-2, 2):
        integral += (h/3) * (y[i] + 4*y[i+1] + y[i+2])
    
    return integral

# Exemplo de uso
# Dados de entrada
x = [0.0, 1.0, 2.0, 3.0, 4.0]
y = [0.0, 1.0, 4.0, 9.0, 16.0]

# Calcula a integral usando o método de Simpson 1/3 repetido
try:
    integral = simpson_1_3_repetido(x, y)
    print("Valor aproximado da integral:", integral)
except ValueError as ve:
    print(ve)
