# Alexis Mendoza Valencia
# Estudiante Tecnológico de Monterrey, campus guadalajara

# Metodo grafico

"""
Nota: Para este método en especial, recomiendo utilizar
      una pagina web llamada Cocalc para correr el metodo.
      Al menos es la pagina que yo utilice, pues ya tiene
      incluidas las librerias necesarias: numpy y mathplotlib.
      La liga es: cocalc.com
"""

import numpy as np
import matplotlib.pyplot as plt

"""
Descripcion: El método consiste en graficar una funcion con
             el fin de encontrar una aproximación al valor
             deseado, generalmente cero.
             Es impreciso porque utilizamos nuestra vista de
             la grafica para ver el resultado. Sirve SOLO
             para tener una aproximacion y nada mas.
             
             Utilizaremos un ejemplo para describirlo.
             
Ejemplo: Función: 2x^2 - 5x + 3

        Nos debe quedar una grafica aproximadamente asi:
        
        Y
        |
     3.0|   \
        |    \
     2.0|     \
        |     l\
     1.0|     l \             /
        |     l  \           /
     0.0|_____l___\_________/______ X
        |     l   l --___-- l
    -1.0|     l   l    l    l
        |     l   l    l    l
            0.25  1   1.2  1.5
        
        
        nota: las "l" conectan los valores en X
              con sus respectivas Y
              
        Y viendo la gráfica podemos decir que los puntos
        en X donde Y = 0 son X = 1 y X = 1.5.
        
        Ahora vamos a ver el código
"""

# Primero definiremos nuestra funcion
def funcion_cuadratica(x):
    return 2*x**2 - 5*x + 3


# Vamos con el metodo directamente
def metodo_grafico(funcion, valor_menor, valor_mayor):
    """
    :param funcion: La funcion que deseamos graficar sin
                    parentesis. Solo su nombre.
    :param valor_menor: Valor mas pequeño de X a graficar
    :param valor_mayor: Valor mas grande de X a graficar.
    :return: nothing
    """

    # Nos vamos a auxiliar de numpy para crear un arreglo
    # lleno de 100 valores de X entre el valor mas pequeño
    # y el mas grande de nuestro intervalo.
    valores_X = np.linspace(valor_menor, valor_mayor, 100)

    # Si quieres ver como queda este arreglo, solo descomenta
    # la siguiente linea
    # print(valores_X)

    # Creamos el arreglo de valores de Y solo con ceros
    valores_Y = np.zeros(100)

    for i in range(len(valores_X)):
        valores_Y[i] = funcion_cuadratica(valores_X[i])

    # Y mostramos la grafica
    plt.plot(valores_X, valores_Y)
    plt.grid()
    plt.show()


# Ahora imprimimos el ejemplo
print("Ejemplo 1")

# El cero y el dos son valores completamente arbitrarios.
metodo_grafico(funcion_cuadratica, 0, 2)


"""
Ahora vamos por un segundo ejemplo, igual de sencillo.
Tenemos una funcion cubica:
    x^3 - pi*X^2 + 20x + 50
"""
import math

def funcion_cubica(x):
    return x**3 - math.pi*x**2 + 20*x + 50


print("Ejemplo 2")
metodo_grafico(funcion_cubica, -10, 10)
