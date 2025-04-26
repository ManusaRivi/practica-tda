import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from grafo import Grafo

grafo = Grafo()

for i in range(1, 8):
    grafo.agregar_vertice(i)

grafo.agregar_arista(1, 2)
grafo.agregar_arista(1, 3)
grafo.agregar_arista(2, 4)
grafo.agregar_arista(2, 5)
grafo.agregar_arista(3, 6)
grafo.agregar_arista(6, 7)
