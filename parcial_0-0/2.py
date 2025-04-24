"""
En clase vimos una solución óptima del problema del cambio utilizando programación dinámica. Ahora planteamos un
problema similar: Implementar un algoritmo que dado un set de monedas posibles y una cantidad de cambio a dar,
devuelva la cantidad de formas diferentes que hay para dar dicho cambio. El algoritmo a implementar debe ser
también por programación dinámica. Indicar y justificar la complejidad del algoritmo implementado. Importante: antes
de escribir código, escribir (y describir) la ecuación de recurrencia.

monedas: [1, 2]

1 | 1 | 2 | 3
0 - 1 - 2 - 3

memo[k] = por cada moneda



OPT[moneda][cambio]:
IF moneda > cambio:
    OPT[moneda][cambio] = OPT[moneda-1][cambio]
ELSE:
    OPT[moneda][cambio] = OPT[moneda-1][cambio] + OPT[moneda][cambio - moneda]
"""

def pretty_print(matrix):
    for i in matrix[::-1]:
        print(i)

def memoria(monedas, cambio):
    memo = []
    memo = [[] for _ in range(len(monedas) + 1)]
    memo[0] = [0 for _ in range(cambio + 1)]
    memo[0][0] = 1
    for i in range(1, len(monedas) + 1):
        pesos = [None for _ in range(cambio + 1)]
        memo[i] = pesos

    for i in range(1, len(monedas) + 1):
        for w in range(cambio + 1):
            if w  == 0:
                memo[i][0] = 1
            else:
                if monedas[i - 1] > w:
                    memo[i][w] = memo[i - 1][w]
                else:
                    memo[i][w] = memo[i - 1][w] + memo[i][w-monedas[i - 1]]

    return memo

def formas_de_dar_cambio(monedas, cambio):
    return memoria(monedas, cambio)[-1][-1]

monedas = [1, 3, 5, 6]
cambio = 10

print(formas_de_dar_cambio(monedas, cambio))
