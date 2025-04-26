"""
Un set dominante (Dominating Set) de un grafo G es un subconjunto D de vértices de G, tal que todo vértice de G pertenece
a D o es adyacente a un vértice en D. El problema de decisión del set dominante implica, dado un grafo G y un número k,
determinar si existe un set dominante de a lo sumo tamaño k.


Sea G un grafo dirigido “camino” (las aristas son de la forma (vi, vi−1)). Cada vertice tiene un valor (positivo).
Implementar un algoritmo que, utilizando programación dinámica, obtenga el Dominating Set de suma mínima
dentro de un grafo de dichas características. Dar la ecuación de recurrencia correspondiente al problema. Indicar
y justificar la complejidad del algoritmo implementado. Indicar y justificar la complejidad espacial del algoritmo
implementado, y si hay una optimización que permita consumir menos espacio.

A <- B <- C <- D <- E

Para que vi esté dominado alguien entre {vi, vi+1} debe estar en el conjunto.
El último vértice siempre debe estar en el conjunto porque nadie puede dominarlo más que él mismo.

"""

def camino_set(valores):
    n = len(valores)
    if n == 0:
        return 0
    if n == 1:
        return valores[0]
    if n == 2:
        return valores[1]

    opt = [float('inf')] * n
    opt[0] = valores[0]
    opt[1] = valores[1] 

    for i in range(2, n):
        if i == n-1:
            opt[i] = opt[i-2] + valores[i]
        else:
            opt[i] = min(
                opt[i-2] + valores[i],
                opt[i-1] + valores[i-1]
            )

    return opt[n-1]


grafo = [5, 10, 12, 4, 12]

print(camino_set(grafo))