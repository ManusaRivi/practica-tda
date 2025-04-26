"""
Implementar un algoritmo que reciba un grafo no dirigido y un número k, y devuelva un ciclo de tamaño exactamente k
del grafo, si es que existe.
"""

from ejemplos_grafo import grafo1, grafo2, grafo3

def encontrar_ciclo_bt(grafo, k, visitados, vertice_actual, vertice_inicial, solucion):
    visitados.add(vertice_actual)
    solucion.append(vertice_actual)
    
    for ady in grafo.adyacentes(vertice_actual):
        if ady == vertice_inicial and len(solucion) == k:
            return solucion
        if not ady in visitados:
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

print(encontrar_ciclo(grafo1, 4))
print(encontrar_ciclo(grafo2, 3))
print(encontrar_ciclo(grafo3, 5))
