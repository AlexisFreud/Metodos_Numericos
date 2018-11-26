# Alexis Mendoza Valencia
# Estudiante Tecnológico de Monterrey, campus guadalajara

# Metodo Newton Raphson - Una sola variable.

"""
El método de Newton-Raphson es de mis favoritos.
             Es divertido de programar e invloucra un poco
             mas de matematica.

Descripcion: Este metodo busca la convergencia rapida de
             de algun valor. Para esto, utiliza derivadas
             que intersecan con valores mascercanos al
             valor que estamos buscando, generalmente cero.
             Necesitamos entonces dos funciones en este caso:
             La funcion f(x) y la derivada f'(x).

            Lo hacemos de esta forma:
            X = x0 - (f(x0) / f'(x) )

Ejemplo: Tenemos las dos funciones:
            f(x) = 2x^2 - 5x + 3
            f'(x) = 4x - 5

            Vamos al código
"""

def funcion_cuadratica(x):
    return 2*x**2 - 5*x + 3


def derivada_cuadratica(x):
    return 4*x - 5


def NewtonRaphson(funcion, derivada,  x_inicial, num_iteraciones, error):
    """
    La x inicial determinara el numero de iteraciones necesarias
    para alcanzar el resultado.
    :param funcion: Nombre de la funcion a utilizar sin parentesis.
    :param derivada: Nombre de la derivada de la funcion sin parentesis.
    :param x_inicial: Valor con el que empezaremos a iterar.
    :param num_iteraciones: Cantidad limite de iteraciones. No
                            queremos que el metodo corra por siempre.
    :param error: Error que tendra el resultado. Un numero mas
                  pequeño nos dara un valor mas exacto, pero
                  requiere un mayor numero de iteraciones.
    :return: Regresa el valor con el error que alcanzo en el numero de
             iteraciones.
    """

    for i in range(num_iteraciones):
        # Formula NewtonRaphson X = x0 - (f(x0) / f'(x) )
        valor_X = x_inicial - (funcion(x_inicial) / derivada(x_inicial))

        # Funcion evaluada en X
        fx = funcion(valor_X)

        # Termina el metodo si tenemos el resultado con el error deseado.
        if abs(fx) < error:
            break
        else:
            x_inicial = valor_X

    return x_inicial


print("Ejemplo 1")
resultado = NewtonRaphson(funcion_cuadratica, derivada_cuadratica, 2, 100, 0.0001)
print("El resultado es:", resultado)


"""
Vamos a probar con otro ejemplo.
f(x) = 5x^5 - 3x^4 + 8x^3 - x^2 + 2x - 15
f'(x) = 25x^4 - 12x^3 + 24x^2 - 2x + 2
"""

def f(x):
    return 5*x**5 - 3*x**4 + 8*x**3 - x**2 + 20*x - 45


def f_prima(x):
    return 25*x**4 - 12*x**3 + 24*x**2 - 2*x + 20


print("\nEjemplo 2")
resultado = NewtonRaphson(f, f_prima, 0, 100, 0.000000001)
print("El resultado es:", resultado)
