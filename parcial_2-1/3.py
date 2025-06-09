def validador_mesas(invitados, vinculos, k, solucion):
    invitados_solucion = set()

    if len(solucion) != k:
        return False
    
    for mesa in solucion:
        for invitado in mesa:
            if invitado not in invitados:
                return False
            
            invitados_solucion.add(invitado)

            for inv in mesa:
                if inv == invitado:
                    continue
                if not ((invitado, inv) in vinculos or (inv, invitado) in vinculos):
                    return False

    if len(invitados_solucion) != len(invitados):
        return False
            
    return True

"""
Esto corre en O(k * n^2 * v) donde k es el número de mesas, n es el número de invitados y v es el número de vínculos.
"""
