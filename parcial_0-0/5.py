"""
El famoso ladrón Francesco Rizzoli (hermano del “árbitro” de la final del 2014), ha decidido hacer un atraco a un
laboratorio farmacéutico. Allí puede robarse diferentes fármacos que se están estudiando (en formato líquido). Tiene un
catálogo del valor de cada fármaco, que puede vender en el mercado negro. De cada fármaco hay una diferente cantidad
disponible (medible en ml). Rizzoli sólo tiene posibilidad en su equipo de llevarse como máximo L ml en fármacos. Lo
bueno es que sabe que puede fraccionar y poner proporciones de los fármacos; y en ese caso lo vendería en su valor
proporcional. Implementar un algoritmo greedy que obtenga los fármacos (y cantidades) que Rizzoli debe robarse para
obtener la máxima ganancia posible (el algoritmo debe ser óptimo, en esta familia no se aceptan los robos a medias).
Justificar por qué el algoritmo propuesto es Greedy. Indicar y justificar la complejidad del algoritmo implementado.

Complejidad:
Sort: O(n log n)
Iterar farmacos: O(n)

Es greedy porque en cada iteracion tomamos la decision greedy de utilizar la maxima cantidad posible del farmaco mas caro.
Luego de usarlo, no lo consideramos mas para el resto de los farmacos, actualizando el estado de la solucion.
"""

def farmacos_greedy(farmacos, L):
    farmacos.sort(key=lambda x: x[0], reverse=True)
    solucion = []
    cantidad_disponible = L
    while cantidad_disponible > 0:
        valor, cantidad = farmacos[0]
        if cantidad >= cantidad_disponible:
            solucion.append((valor, cantidad_disponible))
            break
        
        solucion.append((valor, cantidad))
        cantidad_disponible -= cantidad

        farmacos.pop(0)

    return solucion

farmacos = [(10, 20), (15, 30), (30, 30), (12 ,2), (5, 10)]
L = 15

farmacos2 = [(20, 40), (30, 10), (15, 50)]
L2 = 60

print(farmacos_greedy(farmacos2, L2))
