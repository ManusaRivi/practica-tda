def validador_k_ciclo(grafo, k, solucion):
    visitados = set()
    inicio = solucion[0]
    v = inicio
    fin = False
    while not fin:
        visitados.add(v)
        for w in grafo.adyacentes(v):
            if w == inicio:
                fin = True
                break
            v = w
            grafo.eliminar_arista(v, w)
            break
        return False
    
    if len(visitados) > k:
        return False
    
    return True
