Implementar un modelo de programación lineal que permita determinar el clique de tamaño máximo dentro de un
grafo. Indicar la cantidad de restricciones generadas en función de la cantidad de vértices y aristas.

clique -> conjunto de vertices donde cualquier par de vertices tiene una arista.

Yi -> 1 si vertice pertenece al max clique, 0 si no.

Variable: S = sum(Yi)
Cte: M -> # vertices en el grafo
Obs: S - M <= 0

objetivo: max S

S: # de vertices en el clique.
Si el vertice esta en el clique, Yi + sum(Yk) = S
Si Yi == 1 --> sum(Yk) >= S - 1

Si Yi == 0 --> no hace falta restriccion.
sum(Yk) >= 0

restricciones:

Para cada par de adyacentes, que pertenecen en el clique, tienen que estar conectados.

Yi + sum(Yk) >= S - M * (1 - Yi)

si Yi == 1:
    1 + sum(Yk) >= S - M * 0 --> 1 + sum(Yk) >= S --> sum(Yk) >= S - 1

si Yi == 0:
    0 + sum(Yk) >= S - M --> sum(Yk) >= S - M
