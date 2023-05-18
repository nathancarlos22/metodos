from math import *

def h(x):
    return x**5 -6
def derivada(x):
    return 5*x**4 

x0 = 1
epsilon = 0.001

def metodo_newton(f, df, x0, epsilon):

    i = 0
    while True:
        i += 1
        
        x1 = x0 - (f(x0) / df(x0))

        print(f"Iteração {i}\n\nx_{i} = {x1}\n\n|x{i} - x{i-1}| = {abs(x1 - x0)}\n\n")
        
        if abs(x1 - x0) < epsilon:
            x0=x1
            break
        
        x0=x1
        

    return x1

print("-----------------------------------------------------")
print("\nMétodo de Newton:\n")
newton = metodo_newton(h, derivada, x0, epsilon)