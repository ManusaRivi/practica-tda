"""
Implementar un algoritmo que reciba un grafo no dirigido y un número k, y devuelva un ciclo de tamaño exactamente k
del grafo, si es que existe.

1 <- 2 -> 3
Condicion implicita por como esta implementado el TDA Grafo: k > 2
"""

from ejemplos_grafo import grafo1, grafo2, grafo3, grafo0

def encontrar_ciclo_bt(grafo, k, visitados, vertice_actual, vertice_inicial, solucion):
    visitados.add(vertice_actual)
    solucion.append(vertice_actual)
    
    if len(solucion) > k:
        return []
    
    for ady in grafo.adyacentes(vertice_actual):
        if ady == vertice_inicial and len(solucion) == k:
            return solucion
        if not ady in visitados:
            if vertice_actual == vertice_inicial:
                grafo.borrar_arista(vertice_actual, ady)
            camino = encontrar_ciclo_bt(grafo, k, visitados, ady, vertice_inicial, solucion)
            if camino:
                return camino
            
    visitados.remove(vertice_actual)
    solucion.pop()
    
    return []

def encontrar_ciclo(grafo, k):
    vertices = grafo.obtener_vertices()
    for v in vertices:
        solucion = encontrar_ciclo_bt(grafo, k, set(), v, v, [])
        if solucion:
            return solucion
    return []

print(encontrar_ciclo(grafo1, 2))
print(encontrar_ciclo(grafo2, 3))
print(encontrar_ciclo(grafo3, 5))
print(encontrar_ciclo(grafo0, 2))