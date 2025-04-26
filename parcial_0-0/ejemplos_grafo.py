import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from grafo import Grafo

"""
Grafo ciclico de 4 vertices.

1 -> 2 -> 3 -> 4 - > 1
"""

grafo1 = Grafo()

grafo1.agregar_vertice(1)
grafo1.agregar_vertice(2)
grafo1.agregar_vertice(3)
grafo1.agregar_vertice(4)

grafo1.agregar_arista(1, 2)
grafo1.agregar_arista(2, 3)
grafo1.agregar_arista(3, 4)
grafo1.agregar_arista(4, 1)

"""
Grafo con ciclo de 3 vertices.
"""

grafo2 = Grafo()

for i in range(1, 8):
    grafo2.agregar_vertice(i)

grafo2.agregar_arista(1, 2)
grafo2.agregar_arista(2, 3)
grafo2.agregar_arista(3, 4)
grafo2.agregar_arista(4, 5)
grafo2.agregar_arista(3, 6)
grafo2.agregar_arista(4, 6)
grafo2.agregar_arista(6, 7)

"""
Grafo con ciclo de 5 vertices.
"""

grafo3 = Grafo()

for i in range(1, 11):
    grafo3.agregar_vertice(i)

grafo3.agregar_arista(1, 2)
grafo3.agregar_arista(2, 3)
grafo3.agregar_arista(3, 4)
grafo3.agregar_arista(3, 5)
grafo3.agregar_arista(5, 6)
grafo3.agregar_arista(5, 7)
grafo3.agregar_arista(5, 9)
grafo3.agregar_arista(2, 8)
grafo3.agregar_arista(8, 9)
grafo3.agregar_arista(9, 10)
