"""
Dado un número n, mostrar la cantidad más económica (con menos términos) de escribirlo como una suma de cuadrados,
utilizando programación dinámica. Indicar y justificar la complejidad del algoritmo implementado (cuidado con esto, es
fácil tentarse a dar una cota más alta de lo correcto). Implementar un algoritmo que permita reconstruir la solución.
Aclaración: siempre es posible escribir a n como suma de n términos de la forma 1
2
, por lo que siempre existe solución.

Sin embargo, la expresión 10 = 3^2 + 1^2

es una manera más económica de escribirlo para n = 10, pues sólo tiene dos términos.


n = 1 -> 1^2
n = 2 -> 1^2 + 1^2
n = 3 -> 1^2 + 1^2 + 1^2

n = 4 -> 2^2
n = 5 -> 2^2 + 1^2

n = 6 -> 2^2 + 1^2 + 1^2

n = 7 -> 2^2 + 1^2 + 1^2 + 1^2

n = 8 -> 2^2 + 2^2

n = 9 -> 3^2

n = 10 -> 3^2 + 1^2

opt[i] = min(opt[i - j*j] + 1, opt[i])

"""


def suma_cuadrados(n):
    opt = [float('inf')] * (n + 1)
    opt[0] = 0
    prev = [-1] * (n + 1)

    for i in range(1, n + 1):
        j = 1
        while j*j <= i:
            if opt[i - j*j] + 1 < opt[i]:
                prev[i] = j*j
            opt[i] = min(opt[i], opt[i - j*j] + 1)
            j += 1


    sol = []

    while n > 0:
        sol.append(prev[n])
        n -= prev[n]

    return sol


print(suma_cuadrados(10))