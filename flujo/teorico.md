Indicar si las siguientes afirmaciones sobre Redes de Flujo son verdaderas o falsas, justificando detalladamente.

a. Si aumentamos la capacidad de todas las aristas por una constante K, implicará que el flujo máximo aumente en
[K × min (grado_salida[fuente], grado_entrada[sumidero])] unidades.

Verdadero, porque de la fuente puede salir a lo sumo K * grado_salida[fuente] mas de flujo que antes,
y al sumidero puede entrar a lo sumo K * grado_entrada[sumidero] mas de flujo que antes.

El menor de esos dos numeros va a ser el que limite la cantidad de flujo adicional que atraviese la red, porque una vez calculada la red residual, el flujo que sale de la fuente debe ser igual al flujo que entra al sumidero. Por lo tanto, si la fuente aumentase
un valor F, y el sumidero aumenta un valor G, entonces si F < G, el flujo resultante va a sumarse F. O viceversa, si G < F, el flujo
crecera G.

OBS: Si hay superfuente, tomar los grados de salida de los adyacentes a la super fuente. (O despreciar la super fuente y tomar el sumidero, porque la fuente tiene capacidad de salida infinita)

b. En el caso del flujo máximo de la red, aumentarle la capacidad a una arista cuya capacidad no fue consumida no
tienen ningún efecto sobre el flujo máximo.

Si su capacidad no fue consumida, es porque no se usa en ningun camino s -> t. Por lo tanto, aumentarle la capacidad NO aumenta el flujo, porque va a seguir no siendo utilizada para ir de s a t.


c. Eliminar una arista al azar del grafo puede no afectar el flujo máximo, pero si eliminamos una arista que es parte
del corte mínimo, entonces obligatoriamente sí afectará al flujo máximo.

Es cierto que eliminar una arista al azar del grafo puede no afectar el flujo max, por ej. eliminando una que no se use en ningun camino s -> t. Ahora bien, puede pasar que una de estas aristas este en el corte minimo.

Las aristas que forman parte del corte minimo pueden ser de dos tipos:

    - Aristas saturadas en flujo (no sobra nada)

    - Aristas no usadas

Por lo tanto, si retiramos del corte minimo una arista del segundo tipo, no afectamos el flujo maximo.

