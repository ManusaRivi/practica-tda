Yi -> booleano, 1 si incluyo, 0 si no.

min sum(Yi)

Vertex cover: Para cada arista, al menos uno de sus extremos esta en el set.

Para todo i:

Yi + sum(Yk) >= 1 + M (1 - Yi)

Yi == 1:
No hace falta que incluya ningun adyacente

1 + sum(Yk) >= 1 + 0

sum(Yk) >= 0

Yi == 0:
Tengo que incluirlos a todos. --> M

0 + sum(Yk) >= 1 + M

sum(Yk) >= M