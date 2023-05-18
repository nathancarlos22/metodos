from math import *

def f(x):
    return x**5 - (10/9)*x**3 + (5/21)*x

a = 0.8
b = 1
epsilon = 0.0001 

def bissecao(f, b, a, epsilon):

    if f(a)*f(b) > 0:   
        return "Não há raiz no intervalo"

    i = 0
    x=0
    while abs(b - a) > epsilon:
        x = (a + b)/2

        if f(x) == 0:
            break
        
        if f(a)*f(x) < 0:        
            b = x
        else:
            a = x

        i += 1
        print(f"Iteração: {i}\n\nx{i} = {x}\n\nf(x{i}) = {f(x)}\n\n|b{i} - a{i-1}| = {abs(b - a)}\n\n")
        print(f"a = {a} e b = {b}\n\n")
    return x

print("-----------------------------------------------------")
print("\nBisseção:\n")
bissecao = bissecao(f, b, a, epsilon)