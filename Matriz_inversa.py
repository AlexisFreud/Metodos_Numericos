 Alexis Mendoza Valencia
# Estudiante Tecnológico de Monterrey, campus guadalajara

# Introduccion a matrices y matriz inversa

"""
En este programa estan los siguientes temas:
    0. Definicion de matrices
    1. Creacion de matrices
    2. Sumas, restas y multiplicaciones con matrices.
    3. Matriz transpuesta
    4. Determinantes
    5. Matriz adjunta y cofactores
    6. Matriz inversa
"""
"""
0. Definicion: 
            Una matriz es una tabla cuadrada o rectangular de
            datos (llamados elementos) ordenados en filas y columnas,
            donde una fila es cada una de las líneas horizontales de
            la matriz y una columna es cada una de las líneas verticales.
            A una matriz con m filas y n columnas se le denomina matriz m×n.
            Las dimensiones de una matriz siempre se dan con el número de
            filas primero y el número de columnas después.

            Tomado de:
            https://sites.google.com/site/algebralinealmoralescamacho/u2-matrices/2-1-definicion-de-matriz-notacion-y-orden

            Denotaremos una matriz de m*n como Mmxn

            Además, se dice que una matriz es cuadrada si m = n. Es decir,
            tiene el mismo numero de filas y columnas. Se denota Mnxn.
            A veces tambien nombraremos a la posicion en una fila como i y
            la posicion en una columna como j.

            Algunos ejemplos de matrices:

                   [5   2]
            M3x2 = [2   4]
                   [1   1]

            M2X2 = [2   2]
                   [3   4]
                   
            M(1,2) = 2 en las dos matrices anteriores.

1. Creacion de matrices:
            En python, por convencion, las matrices se representan como
            arreglos bidimensionales.
            
            Vamos a crear algunos metodos que nos seran utiles mas adelante.
"""

def crear_matriz(filas, columnas):
    """
    Crea una matriz Mmxn hecha de ceros. m = filas, n = columas.
    """
    matriz = []
    for i in range(filas):
        matriz.append([0] * columnas)
    return matriz


def obtener_dimensiones(matriz):
    """
    Nos regresa una tupla con los valores de (m, n) de la matriz.
    """
    return (len(matriz), len(matriz[0]))


def copiar_matriz(matriz):
    """
    Nos regresa una copia exacta de la matriz.
    """
    filas, columnas = obtener_dimensiones(matriz)
    nueva_matriz = crear_matriz(filas, columnas)

    for i in range(filas):
        for j in range(columnas):
            nueva_matriz[i][j] = matriz[i][j]

    return nueva_matriz


"""
2. Sumas restas y multiplicaciones con matrices
    Cuando hablamos de matrices, las operaciones fundamentales
    cambian. Funcionan de la misma manera que operaciones con
    vectores. Sin embargo, cabe resaltar que la division no
    esta definida, aunque mas adelante veremos algo similar,
    que es la multiplicacion por la matriz inversa.
    
    Si queremos sumar o restar dos o mas matrices debemos
    tomar en cuenta que estas deben tener las mismas dimensiones
    mxn.
    
    ¿Como se suman?
    Muy sencillo. Tenemos dos matrices, A y B. La suma A + B nos
    dara como resultado una tercera matriz a la que llamaremos C.
    A+B = C. Lo unico que hacemos es sumar la posicion (i,j) de A
    con la posicion (i,j) de B. Esto nos da la posicion (i,j) de C..
    
        [2, 3, 4]
    A = [5, 6, 7]
        [8, 9, 2]
        
        [1, 3, 5]
    B = [7, 9, 2]
        [4, 6, 8]
        
          [2+1, 3+3, 4+5]           [ 3,  6,  9]
    A+B = [5+7, 6+9, 7+2]       C = [12, 15,  9]
          [8+4, 9+6, 2+8]           [12, 15, 10]
          
    Para matrices, A+B = B+A. No hay ningun problema con el orden.
    La resta es exactamente igual, solo que restamos en vez de sumar.
    
    En la multiplicacion, sin embargo, esto no funciona asi. El
    orden de los factores altera el producto.
    A*B != B*A.
    
    ¿Como se multiplican?
    Antes que nada, recomiendo ver esta pagina para introducirse al 
    tema. Es dificil escribirlo aqui.
    https://www.matesfacil.com/matrices/resueltos-matrices-producto.html
    
    En realidad hay tres formas de hacer multiplicaciones de matrices.
    Todas llevan al mismo resultado. La mas sencilla en computacion se 
    llama inner-product.
    
    Es importante mencionar que si tenemos Amxn y Bmxn
    An debe ser igual a Bm y el resultado sera una matriz CAmxBn
    
    Ejemplo: A3x2 * B2*3 = C3x3
    
    Un ejemplo de una multiplicacion de matrices que no esta definida es
    A1x3 * B2x1 porque A3 != B2
    
    Por otro lado, B*A si esta definido, porque B1 = A1
    
    Tenemos que A*B = C
    
    El valor C(i,j) = sumatoria(desde k=0 hasta An) A(i,k)*B(k,j)
    
    Es decir:
    
        [2, 3, 4]
    A = [5, 6, 7]
        [8, 9, 2]
        
        [1, 3, 5]
    B = [7, 9, 2]
        [4, 6, 8]
        
          [2*1 + 3*7 + 4*4, 2*3 + 3*9 + 4*6, 2*5 + 3*2 + 4*8]
    A*B = [5*1 + 6*7 + 7*4, 5*3 + 6*9 + 7*6, 5*5 + 6*2 + 7*8]
          [8*1 + 9*7 + 2*4, 8*3 + 9*9 + 2*6, 8*5 + 9*2 + 2*8]
          
        [3+21+16,  6+27+24,  10+6+32]
    C = [5+42+28, 15+54+42, 25+12+56]
        [ 8+63+8, 24+81+12, 40+18+16]
    
    Vamos al codigo.
"""

def suma_matrices(matriz_A, matriz_B):
    Am, An = obtener_dimensiones(matriz_A)
    Bm, Bn = obtener_dimensiones(matriz_B)

    if Am != Bm or An != Bn:
        print("No se puede sumar")
        return []

    matriz_C = crear_matriz(Am, An)

    for i in range(Am):
        for j in range(An):
            matriz_C[i][j] = matriz_A[i][j] + matriz_B[i][j]
    return matriz_C


def resta_matrices(matriz_A, matriz_B):
    Am, An = obtener_dimensiones(matriz_A)
    Bm, Bn = obtener_dimensiones(matriz_B)

    if Am != Bm or An != Bn:
        print("No se puede restar")
        return []

    matriz_C = crear_matriz(Am, An)

    for i in range(Am):
        for j in range(An):
            matriz_C[i][j] = matriz_A[i][j] - matriz_B[i][j]
    return matriz_C


def multiplicacion_matrices(matriz_A, matriz_B):
    Am, An = obtener_dimensiones(matriz_A)
    Bm, Bn = obtener_dimensiones(matriz_B)
    if An != Bm:
        print("Error en las dimensiones")
        return []
    else:
        matriz_C = crear_matriz(Am, Bn)
        for i in range(Am):
            for j in range(Bn):
                for k in range(An):
                    matriz_C[i][j] += matriz_A[i][k] * matriz_B[k][j]

        return matriz_C


"""
3. Matriz transpuesta.
    La matriz transpuesta existe para todas las matrices Mmxn.
    Se trata de una matriz en la cual las filas se hacen columnas
    y las columnas se hacen filas. Se denotara como AT.
    A(i,j) = AT(j,i)
    
    Un ejemplo:
    
        [2, 3, 4]
    A = [5, 6, 7]
        [8, 9, 2]
        
         [2, 5, 8]
    AT = [3, 6, 9]
         [4, 7, 2]3x
    
    Vamos al codigo.
"""

def obtener_transpuesta(matriz_A):
    Am, An = obtener_dimensiones(matriz_A)
    transpuesta = crear_matriz(An, Am)

    for i in range(Am):
        for j in range(An):
            transpuesta[j][i] = matriz_A[i][j]

    return transpuesta


"""
4. Determinantes
    Un sistema de ecuaciones lineales, uno que no tiene cuadrados,
    se compnre de m cantidad de ecuaciones con n cantidad de 
    variables. Por tanto, podemos representar este sistema como
    una matriz.
    
    Por ejemplo:
    2x1 + 3x2 +  x3 = 11
     x1 - 2x2 + 3x3 = 6
   -5x1 -  x2 + 2x3 = -1
   
   Esto se repreenta como una matriz de la forma Ax = b
   A se refiere a los coeficientes, x se refiere a los valores
   de las variables y b es el resultado.
   
   
   Del ejemplo anterior, la matriz Ax = b seria asi
   [ 2  3  1][x1] =  11 
   [ 1 -2  3][x2] =   6
   [-5 -1  2][x3] = - 1
   
    El determinante de una matriz es un numero que nos va a decir si 
    existe una o muchas soluciones al sistema de ecuaciones. Es decir,
    si existen valores de x1, x2, x3 que permitan el correcto 
    resultado para todo el sistema. Se denota det(A).
    
    Solo se puede obtener el determinante de una matriz si esta es
    cuadrada. Es decir, Mnxn. Lo que nos interesa en este caso es que
    el determinante sea diferente de cero. Si det(A) = 0, entonces
    el sistema no tiene solucion definitivamente.
    
    Obtener el determinante es complicado. Vamos a definir la manera
    de calcularo segun la dimension de la matriz.
    
    Matriz 1x1:
        El determinante de la matriz es directamente el valor que hay
        dentro de ella.
        det([5]) = 5
        det([3]) = 3
        
    Matriz 2x2:
        Teniendo que la matriz esta de la forma A = [a, b]
                                                    [c, d]
        det(A) = a*d - b*c.
        det([5, 3] = 5*3 - 2*3 = 15-6 = 9
            [2, 3]
            
    Matriz 3x3:
        Teniendo la matriz de la forma
        
            [a1, a2, a3]
        A = [a4, a5, a6]
            [a7, a8, a9]
            
        El determinante se obtiene al sumar la multiplicacion de las
        diagonales de izquierda a derecha, menos la suma de la multiplicacion
        de las diagonales de derecha a izquierda.
        
        det(A) = (a1*a5*a9 + a2*a6*a7 + a3*a4*a8) - (a3*a5*a7 + a2*a4*a9 + a1*a6*a8)
        
        Ejemplo:
        
            [2, 3, 4]
        det([5, 6, 7]) = 2*6*2 + 3*7*8 + 4*5*9 - 4*6*8 - 3*5*2 - 2*7*9 = 
            [8, 9, 2]    =24+168+180-192-30-324 = 372 - 546 = -174
            
    Matriz nxn, n>3:
        Utilizamos algo llamado matriz adyacente. Esto no es mas que una matriz
        creada por una matriz mas grande. 
        Utilizaremos una matriz de signos para determinar el signo del determinante.
        
        [+, -, +, ..., -]
        [-, +, -, ..., +]
        [+, ., ., ..., -]
        
        Esta matriz solo nos dice que utilicemos tal o cual signo segun su posicion.
        
        Si tenemos la matriz
            
            [ a1,  a2,  a3,  a4]
            [ a5,  a6,  a7,  a8]
        A = [ a9, a10, a11, a12]
            [a13, a14, a15, a16]
            
        Vamos a eliminar una fila y una columna para reducir la matriz.
            
        Una de sus matrices adyacentes, en (1, 1) es
                 [ a6,  a7,  a8]
        ady(A) = [a10, a11, a12]
                 [a14, a15, a16]
        
        El determinante de una matriz nxn entonces es:
        
        det( sumatoria(desde k = 1, hasta n) de:
             -1^j * A(0, k) * determinante(ady(0, k)) )
             
        Creo personalmente que esto se entiende mejor en codigo. Vamos alla.
"""

def obtener_adyacente(matriz, fila, columna):
    m, n = obtener_dimensiones(matriz)
    adyacente = crear_matriz(m - 1, n - 1)

    for i in range(m):
        if i == fila:
            continue
        for j in range(n):
            if j == columna:
                continue
            adyacente_i = i
            if i > fila:
                adyacente_i = i - 1
            adyacente_j = j
            if j > columna:
                adyacente_j = j - 1
            adyacente[adyacente_i][adyacente_j] = matriz[i][j]

    return adyacente


def determinante(matriz):
    m, n = obtener_dimensiones(matriz)
    if m != n:
        print("La matriz no es cuadrada")
        return -1

    if m == 1:
        return matriz[0][0]

    elif m == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    else:
        det = 0
        for k in range(n):
            det += (-1) ** (k) * matriz[0][k] * determinante(obtener_adyacente(matriz, 0, k))

        return det


"""
5. Matriz adjunta
    La matriz adjunta la necesitaremos mas adelante para obtener la matriz inversa.
    Se obtiene a partir de la transpuesta de sus cofactores.
    Sus cofactores no son otra cosa que los determinantes de todas sus matrices adyacentes.
    Se denota adj(A)
    
    Les recomiendo ver esta pagina, donde se explica mejor este tema:
    https://www.varsitytutors.com/hotmath/hotmath_help/spanish/topics/adjoint-of-a-matrix
    
    No hay mucho que decir. Pasemos directo al codigo.
"""

def matriz_adjunta(matriz):
    m, n = obtener_dimensiones(matriz)
    if m != n:
        print("La matriz no es cuadrada")
        return []
    adjunta = crear_matriz(m, n)

    for i in range(m):
        for j in range(n):
            adjunta[i][j] = ((-1) ** (i + j)) * determinante(obtener_adyacente(matriz, i, j))

    return adjunta


"""
6. Matriz inversa
    Todo lo visto anteriormente solo fue para llegar a esta sección: La matriz inversa.
    Es importante definir antes algo llamado matriz Identidad. Esta matriz es una
    matriz nxn compuesta unicamente por 1's y 0's. Los 1's estan en la diagonal y todo lo
    demas es cero. Se denota A^-1
    
    Ejemplo: I3x3
    
        [1, 0, 0]
    I = [0, 1, 0]
        [0, 0, 1]
        
    La matriz inversa se refiere a la matriz de la cual A*A^-1 = I
    Es equivalente a escribir en numeros reales 3*(1/3) = 1 o 3*3^-1 = 1
    Se podria considerar una especie de division rara, aunque no lo es del todo.
    
    Para obtener el inverso de una matriz A, los pasos van asi:
        1. Obtener el det(A).
        2. Obtener A^t.
        3. Obtener adj(A^t)
        4. Multiplicar adj(A^t) por 1/determinante.
    
    Vamos al codigo.
"""

def matriz_inverza(matriz):
    m, n = obtener_dimensiones(matriz)
    if m != n:
        print("La matriz no es cuadrada")
        return []

    detA = determinante(matriz)
    if detA == 0:
        print("La matriz no es invertible")
        return []

    transpuesta = obtener_transpuesta(matriz)
    adjunta = matriz_adjunta(transpuesta)
    invDetA = 1 / detA
    inversa = crear_matriz(m, n)
    for i in range(m):
        for j in range(n):
            inversa[i][j] = invDetA * adjunta[i][j]
    return inversa

"""
Vamos a hacer una prueba entonces
Tenemos la matriz 

        [2, 3, 4]
    A = [5, 6, 7]
        [8, 9, 2]

Vamos a obtener la inversa por programacion y comprobar que 
A * A^-1 = I

Crearemos un ultimo metodo para imprimir la matriz
"""
def imprime_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

print("Ejemplo 1")
A = [[ 4,  3, -3],
     [-2, -1,  2],
     [-1, -1,  1]]
inversa = matriz_inverza(A)
print("Matriz A")
imprime_matriz(A)

print("\nMatriz inversa")
imprime_matriz(inversa)

print("\nMatriz inversa multiplicada por A")
imprime_matriz(multiplicacion_matrices(A, inversa))


# Ahora un segundo ejemplo
A = [[ 1, -2,  5, -3],
     [-1,  0,  0,  1],
     [ 2,  0,  4,  0],
     [-4,  2, -5,  2]]
inversa = matriz_inverza(A)
print("\nEjemplo 2")
print("Matriz A")
imprime_matriz(A)

print("\nMatriz inversa")
imprime_matriz(inversa)

print("\nMatriz inversa multiplicada por A")
imprime_matriz(multiplicacion_matrices(A, inversa))
