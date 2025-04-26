"""
Implementar un algoritmo greedy que permita obtener el Dominating Set mínimo (es decir, que contenga la menor
cantidad de vértices) para el caso de un árbol (en el contexto de teoría de grafos, no un árbol binario). Indicar y
justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy. Indicar si el
algoritmo siempre da solución óptima. Si lo es, explicar detalladamente, sino dar un contraejemplo.


    A
   /  \
  C    B
  /     \
 D        E


"""

from ejemplos_grafo import grafo

def buscar_hojas(grafo, visitados):
    hojas = set()
    for v in grafo.obtener_vertices():
        if len([ady for ady in grafo.adyacentes(v) if ady not in visitados]) == 1 and v not in visitados:
            hojas.add(v)
    return hojas

def dominating_set_greedy(grafo):
    visitados = set()
    dominados = set()

    while len(visitados) < len(grafo.obtener_vertices()):
        hojas = buscar_hojas(grafo, visitados)

        for hoja in hojas:
            for padre in grafo.adyacentes(hoja):
                if padre not in visitados:
                    dominados.add(padre)
                    for ady in grafo.adyacentes(padre):
                        visitados.add(ady)
                    visitados.add(padre)
                    visitados.add(hoja)

    return dominados


print(dominating_set_greedy(grafo))