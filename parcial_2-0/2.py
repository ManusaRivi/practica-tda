def validador_r_cliques(grafo, R, cliques):
    """
    Valida si el conjunto de cliques es un r-clique en el grafo dado.
    
    :param grafo: Grafo representado como un diccionario de adyacencia.
    :param R: Tamaño del r-clique.
    :param cliques: Lista de cliques a validar.
    :return: True si es un r-clique, False en caso contrario.
    """
    for clique in cliques:
        if len(clique) > R:
            return False
        for i in range(len(clique)):
            for j in range(i + 1, len(clique)):
                if clique[j] not in grafo.adyacentes(clique[i]):
                    return False
    return True