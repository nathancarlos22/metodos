from math import *

def g(x): 
    return x - 2*sin(x) + 0.5*e**x

x0 = 0.5
epsilon = 0.000000001 


def ponto_fixo(f, x0, epsilon):
    x1 = f(x0)
    i = 0
    while abs(x1 - x0) > epsilon:
        x0 = x1
        x1 = f(x0)
        i += 1
        print(f"Iteração {i}\n\nx_{i} = {x1}\n\n|x{i} - x{i-1}| = {abs(x1 - x0)}\n\n")
    return x1 



print("-----------------------------------------------------")
print("\nMétodo do ponto fixo:\n")
ponto_fixo = ponto_fixo(g, x0, epsilon)