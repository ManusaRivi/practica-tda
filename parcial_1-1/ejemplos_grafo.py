import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from grafo import Grafo

grafo = Grafo(es_dirigido=False)

# Agregar vértices
for v in ['A', 'B', 'C', 'D']:
    grafo.agregar_vertice(v)

# Agregar aristas con pesos
grafo.agregar_arista('A', 'B', 10)
grafo.agregar_arista('A', 'C', 15)
grafo.agregar_arista('A', 'D', 20)
grafo.agregar_arista('B', 'C', 35)
grafo.agregar_arista('B', 'D', 25)
grafo.agregar_arista('C', 'D', 30)