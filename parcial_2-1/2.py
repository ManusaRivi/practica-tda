"""
Tati empezó a trabajar en un laboratorio químico, donde trabaja con compuestos que se vaporizan o subliman muy
rápidamente, por lo que suelen estar almacenados en congeladores. ¿El problema? Su predecesora, Nerea, tenía un
único trabajo y lo hizo mal: en vez de almacenar todos los compuestos en un único congelador, guardó cada compuesto
en un congelador por separado.
La empresa no puede sostener un costo tan elevado, y deben deshacerse de todos los congeladores (salvo 1). Esto se
resuelve tan simple como pasar todos los compuestos a un único congelador, pero desde el momento que uno de estos se
abre, se empieza a perder contenido de los compuestos que lleva dentro porque se vuelven gas, y desean minimizar las
pérdidas que esto produzca. Lo que se puede hacer es, en una unidad de tiempo, abrir dos congeladores A y B, y mover
todo lo que haya en el congelador A al B. Se perderá en el medio el equivalente de lo que pierde cada componente por
unidad de tiempo (dato conocido para cada uno). Se puede seleccionar cualquier par de congeladores para hacer lo
antes mencionado. Ejemplo: si tengo el congelador A con el compuesto c1 que pierde 5 por unidad de tiempo, y el
congelador B con el compuesto c2 que pierde 3 por unidad de tiempo, mover lo del congelado A al B nos implica una
pérdida de 5 + 3 = 8. Si ahora movemos lo que hay en el congelador B al congelador C (que tiene los componentes c3,
c4 y c5 con pérdidas de 7, 4 y 1 respectivamente), el costo de ese movimiento será 5 + 3 + 7 + 4 + 1 = 20, lo cual se
suma, obviamente, a cualquier otra pérdida anterior antes incurrida.
Implementar un algoritmo greedy que obtenga el mínimo de pérdida que se puede lograr para terminar con un único
congelador. A fines del parcial no es necesario indicar cómo es este proceso, sólo el valor final. Indicar y justificar la
complejidad del algoritmo. Justificar por qué el algoritmo implementado es, en efecto, un algoritmo greedy. ¿Es el
algoritmo implementado óptimo? Si es, dar una breve explicación, si no lo es dar un contraejemplo.

Solucion propuesta: Ordenar congeladores de menor perdida a mayor. Tomar los dos congeladores de perdida minima y combinarlos.
De esa forma, para un traspaso puntual, minimizamos la perdida, sin pensar a futuro -> paso greedy.

Arreglo perdidas: para el congelador i, su perdida es perdidas[i].

Complejidad:
Dentro del while, tenemos un sort -> O(n log n)
el resto es todo O(1).
Ese while en cada iteracion, quita un elemento de perdidas. Va quitando hasta que quede solo 1 -> O(n)
Por lo tanto, el algoritmo es O(n * n log n) = O(n^2 log n).

Si fuese un min-heap, no tenemos que hacer el sort, pero el append cuesta O(log n).
Por lo tanto, la complejidad seria O(n log n).

Optimalidad:
Supongamos que hay una solucion O = {o1, o2, ..., on} de n traspasos. (o_k es la perdida del traspaso numero k)
Nuestra solucion greedy digamos que es S = {s1, s2, ..., sn}.
Ambas tienen que tener misma cantidad de traspasos.

Asumimos que O es optima. Es decir, sum(o1, o2, ..., on) < sum(s1, s2, ..., sn)

Observamos el caso de nuestro algoritmo greedy: en casa situacion, toma el traspaso de perdida minima.
Para k = 1, s1 < o1.
Es evidente que por hipotesis de induccion, tenemos que s_i < o_i para todo i > {1, ..., n}
Por lo tanto, sum(s1, s2, ..., sn) <= sum(o1, o2, ..., on), creando una contradiccion con lo previamente asumido.

=> S es siempre una solucion optima.
"""

def traspasar_compuestos(perdidas):
    perdida_total = 0
    while len(perdidas) > 1:
        perdidas.sort()
        perdida1 = perdidas[0]
        perdida2 = perdidas[1]
        perdidas.pop(0)
        perdidas.pop(0)
        perdidas.append(perdida1 + perdida2)
        perdida_total += perdida1 + perdida2
    return perdida_total

perdidas1 = [10, 4, 3, 5]
print(traspasar_compuestos(perdidas1))
