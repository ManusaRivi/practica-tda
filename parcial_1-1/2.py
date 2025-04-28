"""
Implementar un algoritmo greedy que permita obtener el mínimo del problema del viajante: dado un Grafo pesado G y
un vértice de inicio v, obtener el camino de menor costo que lleve a un viajante desde v hacia cada uno de los vértices
del grafo, pasando por cada uno de ellos una única vez, y volviendo nuevamente al origen. Se puede asumir que el grafo
es completo. Indicar y justificar la complejidad del algoritmo implementado.
¿El algoritmo obtiene siempre la solución óptima? Si es así, justificar detalladamente, sino dar un contraejemplo. Indicar
y justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy.

"""

from ejemplos_grafo import grafo


def viajante_greedy(grafo, v):
    origen = v
    visitados = [v]

    n = len(grafo.obtener_vertices())

    peso_total = 0

    while len(visitados) < n + 1:
        minimo_peso = float('inf')
        arista_minima = None
        for ady in grafo.adyacentes(v):
            if ady == origen and len(visitados) == n:
                minimo_peso = grafo.peso_arista(v, ady)
                arista_minima = origen
                break


            if grafo.peso_arista(v, ady) < minimo_peso and ady not in visitados:
                minimo_peso = grafo.peso_arista(v, ady)
                arista_minima = ady
        
        v = arista_minima
        visitados.append(v)
        peso_total += minimo_peso

    return peso_total


print(viajante_greedy(grafo, 'A'))