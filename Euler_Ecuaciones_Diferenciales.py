# Alexis Mendoza Valencia
# Estudiante Tecnológico de Monterrey, campus guadalajara

# Metodo Euler Ecuaciones Diferenciales

"""
El metodo es sencillo. Buscamos el valor de y evaluada en
xi. Para ello, tenemos un valor inicial y(x0) = a.

Tenemos varias condiciones iniciales:
    Ecuacion diferencial
    Valores para x0, y(x0) y xi.
    n = numero de puntos
    h = (|x0-xi| / n-1)

Despejamos y' de la ecuacion diferencial y usamos la formula
Yn = Yn-1 + h* Y'(Xn-1, Yn-1)
Es decir, el valor actual de y utiliza el valor anterior de Y
mas h multiplicado por Y' evaluada en X y Y anteriores.

Vamos al codigo con un ejemplo
"""

# Ecuacion diferencial: y' - 2xy = 0
# y' = 2xy
# y(1) = 1
# Find y(1.5)

def y_prime(x, y):
    return 2*x*y


def metodo_euler(function_f, x0, y0, x_limit, h):
    y = 0
    limit = (int)((x_limit - x0) / h)
    for i in range(limit):
        y = y0 + h*(function_f(x0, y0))
        y0 = y
        x0 += h
    return y


print("Caso 1: h = 0.1")
result = metodo_euler(y_prime, 1, 1, 1.5, 0.1)
print("Resultado:", result)


print("\nCaso 2: h = 0.05")
result = metodo_euler(y_prime, 1, 1, 1.5, 0.05)
print("Resultado:", result)
