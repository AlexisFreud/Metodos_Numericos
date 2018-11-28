# Alexis Mendoza Valencia
# Estudiante Tecnológico de Monterrey, campus guadalajara

# Metodo para ecuaciones diferenciales de orden superior

"""
Se trata de casos donde no tenemos y', sino y'' o incluso y'''
Lo que hacemos es una sustitucion. U = y', por lo que U' = Y''
y podemos entonces utilizar el metodo de Euler, pero con una
variable adicional.
Ejemplo:
    y'' - y' - 2xCosy - 3x = 0
    U = y'
    U' - U - 2xCosy - 3x = 0
    U' = U + 2xCosy + 3x
    U = 2xCosy + 3x - U'
    U0 = 1
    Y0 = 1
    

Vamos al codigo
"""
import math


def u_prime(x, y, u):
    return u + 2*x*math.cos(y) + 3*x


def metodo_euler_OS(function_f, x0, y0, x_limit, h):
    y = 0
    limit = (int)((x_limit - x0) / h)
    for i in range(limit):
        y = y0 + h*(function_f(x0, y0))
        y0 = y
        x0 += h
    return y


print("Caso 1: h = 0.1")
result = metodo_euler_OS(u_prime, 1, 1, 1.5, 0.1)
print("Resultado:", result)


print("\nCaso 2: h = 0.05")
result = metodo_euler_OS(u_prime, 1, 1, 1.5, 0.05)
print("Resultado:", result)
