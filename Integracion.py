# Alexis Mendoza Valencia
# Estudiante Tecnológico de Monterrey, campus guadalajara

# Integracion - Trapecios y Simpson

"""
Existen diferentes maneras de integrar por metodos numericos.
Las que veremos aqui son el método de los trapecios y los
dos metodos de Simpson, 1/3 y 3/8.

Metodo de trapecios:
    Al integrar por metodos numericos buscamos unicamente una
    aproximacion al valor deseado. Imaginemos una curva cualquiera.
    Podemos calcular el area bajo la curva utilizando rectangulos,
    pero esto nos dejaria un error muy grande. En cambio, utilizamos
    trapecios.

    La formula para el area de un trapecio es:
    (BaseMayor + basemenor) * altura / 2

    Volviendo a la curva, nuestra altura, denotada h, sera la base
    de la solucion. Los trapecios estan acomodados de manera vertical,
    asi que nuestra h sera la variacion de x.
    Una h mas pequeña genera un menor error. De hecho, cuando h se hace
    infinitamente pequeña nos da la definicion de la integral.

    Si ponemos varios trapecios juntos nos daremos cuenta de que la Base
    Mayor de un trapecio es la base menor de otro, excepto en las orillas.

           /|
         /| |
       /| | |
      | | | |
      | | | | B
    b | | | |
      |_|_|_|
       h h h

    Tenemos entonces una integral definida desde a hasta b de f(x)dx
    Escogemos una h y decimos que la cantidad de trapecion, n, es:
    n = (|b-a|)/h

    Entonces nuestra formila es:

                        n-1
                         __
                         \
   I = h/2 * (y0 + yn +  /_ 2*Yi  )
                         i=1

   O tambien lo podemos ver como:
   I = (h/2) * (y0 + 2y1 + 2y2 + 2y3 + ... + 2yn-1 + yn)

   Vamos al codigo con un ejemplo
   Integral desde 0 hasta 6 de 3x^2 dx
"""
def integral(x):
    return 3*x**2


def integracion_trapecios(x_inicial, x_final, funcion, h):
    n = (int) (abs(x_final - x_inicial) / h)
    I = funcion(x_inicial) + funcion(x_final)
    for i in range(1, n-1):
        I += 2 * funcion(x_inicial + (h * i))
    I *= (h/2)
    return I


print("El resultado de la integral de 0 a 6 de "
      "3x^2 dx es 6^3 = 216\n")
resultado = integracion_trapecios(0, 6, integral, 0.5)
print("El resultado con el metodo de trapecios es", resultado)

"""
Se vemos el resultado del metodo comparado con el resultado
real parecera que el error es enorme. 
El resultado de la integral por metodos analiticos es
216, mientras que el metodo de trapecios nos da 171.375.
Esto se debe a la h, que es bastante grande.
Si corremos el metodo con una h pequeña, el resultado
se aproximara mas, como en el siguiete caso.
"""

resultado_h_pequeña = integracion_trapecios(0, 6, integral, 0.001)
print("Con una h pequeña el resultado es", resultado_h_pequeña)


"""
Metodo simpson 1/3:
    El metodo ideado por Simpson consiste en tomar conjuntos de 
    estos trapecios que vimos, en grupos de dos trapecios en 
    dos trapecios y hacer una curva que se asemeje mas a la 
    realidad. El metodo es casi el mismo, solo cambian
    los valores de y's impares: y1, y3, y5...
    
    La formula es:
        I = h/3 * (y0 + 4y1 + 2y2 + 4y3 + 2y4 + ... + 4yn-1 + yn)
    Para que funione, la cantidad de y's debe ser impar. Para esto
    hay que escoger con cuidado la h.
    
    Vamos al codigo
"""

def integracion_simpson_13(x_inicial, x_final, funcion, h):
    n = (int)(abs(x_final - x_inicial) / h)
    if n % 2 == 0:
        n += 1
    I = funcion(x_inicial) + funcion(x_final)
    for i in range(1, n - 1):
        if i % 2 == 0:
            I += 2 * funcion(x_inicial + (h * i))
        else:
            I += 4 * funcion(x_inicial + (h * i))
    I *= (h / 3)
    return I


resultado = integracion_simpson_13(0, 6, integral, 0.5)
print("\nEl resultado con el metodo de Simpson 1/3 es", resultado)

"""
Si corremos el programa, nos daremos cuenta que el error es exactamente
cero. El resultado es exacto.
"""


"""
Metodo simpson 3/8:
    Este metodo es igual a Simpson 1/3 con la diferencia de tomar
    grupos de 3 trapecios.

    La formula es:
        I = 3h/8 * (y0 + 3y1 + 3y2 + 2y3 + 3y4 + ... + 3yn-1 + yn)
        
    Para que funione, la cantidad de y's debe ser multiplo de 3. Para esto
    hay que escoger con cuidado la h. Todos los valores multiplos de 
    3, excepto el primer y ultimo valor se multiplican por 2. El resto, 
    con la misma excepcion, se multiplican por 3

    Vamos al codigo
"""


def integracion_simpson_38(x_inicial, x_final, funcion, h):
    n = (int)(abs(x_final - x_inicial) / h)
    while n % 3 != 0:
        n += 1
        print("subio n")
    I = funcion(x_inicial) + funcion(x_final)
    for i in range(1, n - 1):
        if i % 3 == 0:
            I += 2 * funcion(x_inicial + (h * i))
        else:
            I += 3 * funcion(x_inicial + (h * i))
    I *= (3*h / 8)
    return I


resultado = integracion_simpson_38(0, 6, integral, 6/60)
print("\nEl resultado con el metodo de Simpson 3/8 es", resultado)
