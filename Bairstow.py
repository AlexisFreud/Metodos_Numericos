# Alexis Mendoza Valencia
# Estudiante Tecnológico de Monterrey, campus guadalajara

# Metodo_Bairstow

"""
Este metodo nos dice que cualquier funcion de de orden n
puede desomponerse en (x^2 + rx + s)(x^n-2 + x^n-3 + ... + x^0)
para obtener sus valores.
"""

#f(x) = x^5 - 3.5x^4 + 2.75x^3 + 2.125x^2 - 3.875x + 1.25
coeficientes = [1.25, -3.875, 2.125, 2.75, -3.5, 1]

def bn(coeficientes):
    return coeficientes[-1];

"""En esta funcion tenemos que:
    a: Lista de coeficientes
    b: bn(a)
    r y s: son valores cualquiera que permiten acercarse al valor final
"""
def bn1(a, b, r):
    return coeficientes[-2]+r*b;

def bi(i, a, r, s, b):
    return a[i] + r*b[0] + s*b[1];

def cn(b):
    return bn(b);
def cn1(b, c, r):
    return bn1(b,c,r);
def ci(i, b, r, s, c):
    return bi(i, b, r, s, c);
r = -1
s = -1
b = []
raices = []
for i in range(100):
    b = []
    b.insert(0, bn(coeficientes))
    b.insert(0, bn1(coeficientes, b[0], r))
    print(b)

    for i in reversed(range(0,4)):
        b.insert(0, bi(i, coeficientes, r, s, b))
    print(b)
    c = []
    c.append(cn(b));
    c.insert(0, cn1(b, c[0], r))
    for i in reversed(range(0,4)):
        c.insert(0, ci(i, b, r, s, c));
    print(c)

    def deltaS(b, c):
        return (-1*b[1]/c[2] + b[0]/c[1]) / (c[3]/c[2] - c[2]/c[1])

    def deltaR(b, c, dS):
        return (-1*b[0]/c[1]) - ((c[2]/c[1])*dS)

    dS = deltaS(b, c)
    dR = deltaR(b, c, dS)

    print("dS = ", dS)
    print("dR = ", dR)

    if(abs(dS) < 0.01 and abs(dR) < 0.01):
        break;
    r += dR
    s += dS
