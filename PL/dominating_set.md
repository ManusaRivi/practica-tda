Yi = variable boolena, 1 si incluyo el vertice, 0 si no
Vi = valor del vertice i (cte)

min sum(Yi * Vi)

Dominating set: Cada vertice o esta en el set, o al menos un adyacente esta en el set.

Yi + sum(Yk) >= 1

Yi = 1 -> sum(Yk) puede ser 0. (no hay restriccion)
Yi = 0 -> sum(Yk) >= 1

1 + sum(Yk) >= 1 ---> sum(Yk) >= 0 ---> puedo incluir todos los adyacentes que quiera.
0 + sum(Yk) >= 1 ---> sum(Yk) >= 1 ---> necesito al menos uno para cubrir mi vertice.
