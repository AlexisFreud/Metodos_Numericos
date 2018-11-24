# Alexis Mendoza Valencia
# Estudiante Tecnológico de Monterrey, campus guadalajara

# Método de falsa posición.
import math

"""
Descripción: Escencialmente es igual al método de la bisección.
             Puedes verlo aquí https://github.com/AlexisFreud/Metodos_Numericos/blob/master/Método_bisección.py

             Veamos la siguiente grafica.

             +Y
             |           /
             |          /
       f(Xb)-|         · B
             |        /|
             |       / |
             |      /  |
        -X___|_____·_C_|__________+X
             |    /    |
             |   /     |
             |  /      |
       f(Xa)-| ·-A-----| (f(Xa),Xb)
             |/
             | Xa  Xc  Xb
             -Y

             Cada punto se compone de coordenadas X & Y.
             El punto A tiene Xa, f(Xa).
             El punto B tiene Xb, f(Xb).
             El punto C tiene Xc, f(Xc).

             Lo que buscamos es el punto donde f(x) = 0,
             es decir, el punto (Xc,f(Xc)). Sabemos que
             f(Xc) = 0, por lo que debemos encontrar Xc.

             Y para eso utilizaremos esta fórmula
             Xc = Xa + (F(Xa)*(Xb-Xa)) / (F(Xb)-F(Xa))
"""

# Para dar un ejemplo tomaremos la función que utilizamos
# en el método de la bisección. Lo único relevante es la fórmula
# Puedes ver el ejercicio en la liga:
# https://github.com/AlexisFreud/Metodos_Numericos/blob/master/Método_bisección.py

# f(x) = (masa*gravedad / k) * (1 - e^( (-masa*k) / tiempo)) ) - velocidad
def funcion_paracaidas(k):
    # k sería nuestro valor de x.
    # Definiremos aqui nuestros valores.
    masa = 68.1
    vel = 40
    gravedad = 9.81
    tiempo = 10

    return ((masa * gravedad) / k) * (1 - math.exp((-masa * k) / tiempo)) - vel


def metodo_falsa_posicion(Xa, Xb, funcion, error, limite):
    """
    :param Xa: Valor inferior de x
    :param Xb: Valor superior de x
    :param error: Error del resultado de la función.
    :param limite: Límite de iteraciones.
    """
    for i in range(limite):
        Fxa = funcion(Xa)
        Fxb = funcion(Xb)
        if Fxa * Fxb > 0:
            print("No hay raiz en este rango")
            break;
        Xc = Xa - (Fxa * (Xb - Xa)) / (Fxb - Fxa)
        Fxc = funcion(Xc)
        if (Fxc * Fxb) > 0:
            Xb = Xc
        else:
            Xa = Xc

        if abs(Fxc) < error:
            break
    return Xc


# Probemos la funcion.
print("----Prueba 1----")
Xa = 10
Xb = 20
error = 0.0001
limite = 100
resultado = metodo_falsa_posicion(Xa, Xb,
                                  funcion_paracaidas,
                                  error, limite)
print("Resultado:", resultado)

# Si evaluamos la funcion en el resultado
# deberiamos obtener un número cercano a 0
resultado_funcion = funcion_paracaidas(resultado)
print("Resultado de función evaluada:", resultado_funcion)


# Probemos, igual que en los métodos anteriores,
# calcular la raiz cuadrada de 2.
def raiz_dos(x):
    return x**2 - 2


print("\n----Prueba 2----")
Xa = 0
Xb = 2
resultado = metodo_falsa_posicion(Xa, Xb,
                                  raiz_dos, error,
                                  limite)
print("Resultado:", resultado)
# Evaluamos la funcion y deberia darnos un número
# cercano a 0.
resultado_funcion = raiz_dos(resultado)
print("Resultado de función evaluada:", resultado_funcion)
