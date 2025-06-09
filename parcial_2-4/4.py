def validador_fila_alumnos(alumnos, amistades, solucion):
    fila = set()
    for i in range(len(solucion) - 1):
        fila.add(solucion[i])
        if solucion[i] in amistades[solucion[i+1]] or solucion[i+1] in amistades[solucion[i]]:
            return False
    fila.add(solucion[-1])
    if len(fila) != len(alumnos):
        return False
    return True