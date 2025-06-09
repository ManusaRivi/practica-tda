def validador_subset_sum(solucion, W, elems):

    if sum(solucion) != W:
        return False
    
    if len(solucion) > len(elems):
        return False
    
    for i in solucion:
        if i not in elems:
            return False

    return True
