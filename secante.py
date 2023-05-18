from math import *

def f(x):
    return 4*sin(x) - e**x
    

x0 = 0
x1 = 1
epsilon = 0.000000001

def secante(f, x0, x1, epsilon):
    x2 = f(x1)
    i = 0
    while abs(x2 - x1) > epsilon:
        x1 = x2 
        x2 = x0 - f(x0)*(x1-x0)/(f(x1)-f(x0))
        i += 1
        print(f"Iteração {i}\n\nx_{i} = {x1}\n\n|x{i} - x{i-1}| = {abs(x1 - x0)}\n\n")
    return x2

print("-----------------------------------------------------")
print("\nMétodo da secante:\n")
secante = secante(f, x0, x1, epsilon)