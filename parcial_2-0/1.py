"""
Resolver, utilizando backtracking, el problema de la mochila con cantidades mínimas. Este tiene el mismo planteo al
original pero además cuenta con un parámetro K, donde además de las condiciones impuestas para el problema original,
se deben utilizar al menos K elementos. Es decir, el planteo completo es: Dados n elementos de valores v1, v2, ..., vn
con pesos p1, p2, ..., pn, y valores W y K, encontrar el subconjunto de al menos K elementos, cuya suma de valor sea
máxima y cuyo peso no exceda el valor de W.

"""
def mochila_back_aux(n, W, K, pos_actual, sol_parcial, sol_global, peso_actual, valor_actual, mejor_valor):
    if peso_actual > W:
        return []
    
    if pos_actual == len(n):
        if len(sol_parcial) >= K and valor_actual > mejor_valor[0]:
            sol_global.clear()
            sol_global.extend(sol_parcial)
            mejor_valor[0] = valor_actual
        return []
    
    sol_parcial.append(n[pos_actual])

    mochila_back_aux(n, W, K, pos_actual+1, sol_parcial, sol_global, peso_actual + n[pos_actual][1], valor_actual + n[pos_actual][0], mejor_valor)
    
    sol_parcial.pop()
    return mochila_back_aux(n, W, K, pos_actual+1, sol_parcial, sol_global, peso_actual, valor_actual, mejor_valor)

def mochila_back(n, W, K):
    if W == 0 or len(n) == 0:
        return []
    
    sol_global = []
    
    mejor_valor = [-1]

    mochila_back_aux(n, W, K, 0, [], sol_global, 0, 0, mejor_valor)

    return sol_global
