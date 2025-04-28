"""
Implementar un algoritmo que dado un grafo no dirigido y conexo, un vértice v y otro w, determine la cantidad
máxima de caminos disjuntos, y cómo son, que conectan a v con w. Indicar y justificar la complejidad del algoritmo
implementado.

Caminos disjuntos: dos caminos son disjuntos si no tienen vertices en comun.

Complejidad:
Pasa por todos los vertices O(v) y por cada vertice verifica sus adyacentes O(e).
=> O(v + e)
"""

from ejemplos_grafo import grafo0, grafo1, grafo2, grafo4

def cantidad_caminos(grafo, vertices, actual, w, visitados, solucion_parcial, soluciones):
    visitados.add(actual)
    solucion_parcial.append(actual)
    
    if len(visitados) == len(vertices):
        return soluciones
    
    for ady in grafo.adyacentes(actual):
        if ady == w:
            soluciones.append(solucion_parcial[:])
            return soluciones
        if not ady in visitados:
            soluciones = cantidad_caminos(grafo, vertices, ady, w, visitados, solucion_parcial, soluciones)
    
    visitados.remove(actual)
    solucion_parcial.pop()

    return soluciones

def caminos(grafo, v, w):
    vertices = grafo.obtener_vertices()
    caminos = cantidad_caminos(grafo, vertices, v, w, set(), [], [])
    return len(caminos)

print(caminos(grafo1, 1, 4))

print(caminos(grafo2, 4, 3))

print(caminos(grafo4, 1, 5))
