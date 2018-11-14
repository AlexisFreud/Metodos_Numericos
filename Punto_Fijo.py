# Alexis Mendoza Valencia
# Estudiante Tecnológico de Monterrey, campus Guadalajara

# Método de punto fijo o punto flotante
"""
Descripción: 1. El método consiste en despejar un valor de x  de
                una ecuación. Esta x la llamaremos x_despejada. En la ecuación
                debe quedar otra x a la que llamaremos x_actual. Esto, debido
                a que este valor estara cambiando.
             2. Elegimos un valor cualquiera de x_actual y lo sustituimos en
                la función. El resultado será el valor de x_despejada.
             3. Repetimos el proceso hasta que x_actual = x_despejada.

Ejemplo: Tenemos la ecuación 2x^2 - 5x + 3 = 0.
         Despejamos una x. No es necesario depejar más.
         -5x = -3 - 2x^2
         x_despejada = (2(x_actual)^2 + 3) / 5

         ¡Vamos a programar!
"""


# Primero necesitamos un método que nos regrese la funcion evaluada.
def funcion_cuadratica(x_actual):
    return (2 * x_actual**2 + 3) / 5


def punto_fijo(x_actual, funcion, limite, error):
    """
    Vamos a definir dos cosas: error y limite de iteraciones.
    Error: Máximo error que tendra nuestra función.
    Límite: Limite de iteraciones. No queremos que nuestro método
            corra por siempre.
    """
    for i in range(limite):
        x_despejada = funcion(x_actual)
        if abs(x_despejada - x_actual) < error:
            break
        x_actual = x_despejada
    return x_despejada


# Prueba del método
resultado = punto_fijo(0, funcion_cuadratica, 100, 0.0001)
print("Resultado:", resultado)
