"""
La Cruz Roja cuenta con n ambulancias, de las cuáles conoce la ubicación de cada una. En un momento dado llegan
p pedidos de ambulancias para socorrer personas. Debido a diferentes reglas que tienen, una ambulancia no debe
trasladarse más de k kilómetros. Se quiere saber si se puede hacer una asignación de ambulancias a los pedidos,
asignando cada una a como máximo 1 pedido. Implementar un algoritmo que resuelva este problema, utilizando redes
de flujo. Indicar y justificar la complejidad del algoritmo implementado para el problema planteado.
"""

from grafo import Grafo

SUPER_FUENTE = "super_fuente"
SUPER_SUMIDERO = "super_sumidero"

"""
Complejidad:

O(a + p)

Cantidad vertices: a + p

Cantidad aristas:
Peor caso a * p
"""

def crear_red(ambulancias, pedidos, k):
    red = Grafo(es_dirigido = True)

    red.agregar_vertice(SUPER_FUENTE)
    red.agregar_vertice(SUPER_SUMIDERO)

    for pedido in pedidos:
        red.agregar_vertice(pedido)
        red.agregar_arista(pedido, SUPER_SUMIDERO, 1)

    for ambulancia in ambulancias:
        red.agregar_vertice(ambulancia)
        red.agregar_arista(SUPER_FUENTE, ambulancia, 1)
        for pedido in pedidos:
            if distancia(ambulancia, pedido) <= k:
                red.agregar_arista(ambulancia, pedido, 1)
    
    return red

"""
Complejidad:
ford fulkerson: O (V * E ^ 2) == O ((a + p) * (a * p) ^ 2)

"""

def asignar_ambulancias_a_pedidos(ambulancias, pedidos, k):
    red = crear_red(ambulancias, pedidos, k)
    flujo = ford_fulkerson(red, SUPER_FUENTE, SUPER_SUMIDERO)

    caminos = []
    hay_caminos: True
    while hay_caminos:
        camino = []
        camino.append(SUPER_FUENTE)
        v = SUPER_FUENTE
        while v != SUPER_SUMIDERO:
            for w in red.adyacentes(v):
                if flujo[v][w] == 1:
                    flujo[v][w] = 0
                    v = w
                    camino.append(v)
                    break
            hay_caminos = False
            break
        caminos.append(camino)
    return caminos
