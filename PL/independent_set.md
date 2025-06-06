Yi -> booleano si meto o no el vertice

max sum(Yi)

Yi + Sum(Yk) <= 1 + M (1 - Yi)

M ~= todos los vertices

Yi == 1:
1 + sum(Yk) <= 1 + M * 0 <= 1

sum(Yk) <= 0 ---> No incluyo ningun adyacente

Yi == 0:

0 + sum(Yk) <= 1 + M(1) ~= M ---> Puedo incluir todos los adyacentes que yo quiera.
