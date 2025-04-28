"""
Implementar un algoritmo que, por programación dinámica, resuelva el problema de la mochila con una variante:
ahora se puede poner una cantidad ilimitada de un mismo elemento (es decir, se puede repetir), siempre y cuando
aún haya lugar. Por ejemplo, si yo tengo un elemento de tamaño 3 y una mochila de tamaño 10, yo podría guardar
3 veces dicho elemento, si así lo quisiera (también menos cantidad). Escribir y describir la ecuación de recurrencia
de la solución, y la complejidad del algoritmo implementado. Implementar o explicar (la que prefieran) cómo sería el
algoritmo de reconstrucción de la solución, indicando su complejidad.

Problema de la mochila "tradicional":
    Dado el item i:
        Si no lo agrego, considero los items i - 1, con el mismo peso disponible.
        Si lo agrego, considero los items i - 1 habiendo ocupado el peso y ganado el valor de i.

    OPT(n, W) = max(OPT(n - 1, W), v[n] + OPT(n - 1, W - p[n]))
    Donde W es la capacidad de la mochila actual, v[n] es el valor del item n, y p[n] es el peso del item n.

Ahora, veamos que cambia con la variante: puedo repetir un elemento varias veces.
=> Si agrego un elemento, puedo volver a considerarlo en futuras iteraciones.

Debo modificar el caso en que agregue el elemento, en lugar de referirme al optimo sin ese elemento, refiero al optimo con la
misma coleccion de elementos:
    OPT(n, W) = max(OPT(n - 1, W), v[n] + OPT(n, W - p[n]))
                        ^                     ^
                        si no lo uso,         si lo uso, lo vuelvo a contemplar
                        no lo contemplo.      pero con capacidad reducida.
Complejidad:
    Peor caso: paso por cada elemento una vez. Ese while va a iterar por cada elemento.
    Dentro del while, todas las operaciones son O(1).
    Fuera del while tambien. Por ende la complejidad temporal del algoritmo es O(n).
    Espacio: creo arreglo solucion, a lo sumo tiene n elementos => O(n).
"""

def reconstruir(elementos, capacidad, pesos, valores, opt):
    capacidad_disponible = capacidad
    elemento_actual = len(elementos)
    solucion = []
    while elemento_actual > 0:
        peso_actual = pesos[elemento_actual - 1]
        valor_actual = valores[elemento_actual - 1]
        if opt[elemento_actual][capacidad_disponible] == valor_actual + opt[elemento_actual][capacidad_disponible - peso_actual]:
            solucion.insert(0, elemento_actual)
            capacidad_disponible -= peso_actual
        else:
            elemento_actual -= 1
    return solucion
