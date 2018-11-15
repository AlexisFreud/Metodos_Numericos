# Alexis Mendoza Valencia
# Estudiante Tecnológico de Monterrey, campus Guadalajara

# Método bisección
# Es importante importar la libreria math
import math

"""
Descripción: El método de la bisección consiste en tomar 
             2 valores en el rango entre el que se encuentra 
             la solucion que buscamos. Después calculamos el
             promedio de los puntos y lo asignamos a uno de
             los puntos, de tal forma que en cada iteración 
             nos acerquemos mas a la solución.
             
Ejemplo:  si queremos encontrar la raiz cuadrada de 4, vamos
          a intentar con valores 0 y 3. 
          Supongamos que la función esta dada por:
          x^2 - 4 = 0
            Valor 1: 0^2 - 4 = -4
            Valor 2: 3^2 - 4 = 5

          Ahora, si sacamos el promedio de estos valores 
          tenemos
            (3 + 0)/2 = 1.5
          1.5^2 - 4 = - 1.75 por lo que nos acercamos a 
          la solucion. Si repetimos esto muchas veces, 
          en algun momento llegaremos al resultado aproximado.

Primero que nada, para este método utilizaremos
un ejemplo para describirlo.

Juan, nuestro heroe, se lanza en paracaidas.
Cuando lleva 10 segundos en vuelo, estos son
sus datos.
masa: 68.1 kg
velocidad: 40 m/s
gravedad: 9.81 m/s^2

 Lo único que nos interesa es calcular la resistencia
que genera el viento sobre el paracaídas.
(Es mas sencillo de lo que parece).

Primero definimos la función que nos calcula un
aproximado de la resistencia del viento. Es una
función compleja. Por esta razón hacemos uso de
un método numérico.

f(k) = (masa*gravedad / k) * (1 - e^( (-masa*k) / tiempo)) ) - velocidad
k es una constante.
e es el numero de euler. En python, math.exp(x)

Entonces la pasamos a código.
"""


def resistencia_viento(k):
    """
    Esta funcion no es propia del método de la biseccion.
    Bien se pude utilizar para calcular f(x) = x^2 o
    cualquier funcion que se desee utilizar.
    """

    # Definiremos aqui nuestros valores.
    masa = 68.1
    vel = 40
    gravedad = 9.81
    tiempo = 10
    return ((masa * gravedad) / k) * (1 - math.exp((-masa * k) / tiempo)) - vel


"""
Ahora si, ya con la función definimos el método
de la bisección.
"""


def biseccion(x1, x2, funcion):
    """
    :param x1: Menor valor en el que creemos esta
                el resultado.
    :param x2: Mayor valor en el que creemos esta
                el resultado.
    :return: El resultado.
    """

    limite = 100
    # El limite lo definimos solo para que nuestra
    # función no corra por siempre.
    error = 0.0001
    # Precisión que tendra nuestra función.
    # Un menor error requiere de más iteraciones.
    # Ej. 0.00001
    for i in range(limite):
        f1 = funcion(x1)  # Funcion evaluada en x1
        f2 = funcion(x2)  # Funcion evaluada en x2
        if f1 * f2 > 0:
            print(i)
            """
            Si los resultados son ambos positivos,
             o ambos negativos debemos escoger otro 
             rago de valores x1 y x2.
            """
            print("No existe raiz en este rango.")
            break

        x_actual = (x1 + x2) / 2
        fx = funcion(x_actual)
        if fx * f1 < 0:
            x2 = x_actual
        else:
            x1 = x_actual
        # Sabemos que llegamos al resultado cuando
        # fx < error
        if abs(fx) < error:
            return x_actual
    # Si no obtuvimos resultado, regresamos alguno de
    # los dos valores anteriores. En este caso x1
    return x1


"""
Las siguientes lineas son solo la prueba del método
anterior. Vamos a utilizar el rango 10 - 25
"""
print("Primer ejemplo")
resultado = biseccion(10, 25, resistencia_viento)
print("El resultado es:", resultado, "\n")

print("Segundo Ejemplo")
"""
Para hacer un segundo ejempo, vamos a calcular
la raiz de dos con este metodo.
Sabemos que sqrt(2) = x
      y que     x^2 = 2
Por lo tanto x^2 - 2 = 0
"""


def raiz_dos(x):
    return x**2 - 2


resultado = biseccion(0, 2, raiz_dos)
print("El resultado es:", resultado)
