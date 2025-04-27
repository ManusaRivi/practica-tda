"""
Implementar un algoritmo potencia(b, n) que nos devuelva el resultado de b^ n en tiempo O(log n). Justificar
adecuadamente la complejidad del algoritmo implementado. Ayuda: recordar propiedades matemáticas de la potencia.
Por ejemplo, que a a^h * a^k = a^(h+k)

complejidad = O(log n)
Teorema Maestro ->  C = 0, log_b(a) = 0 -> B = 2 Y A = 1 
"""

def potencia(b, n):
    if n == 0:
        return 1
    if n == 1:
        return b
    if n == 2:
        return b * b
    
    mitad = potencia(b, n//2)

    if n % 2 == 0:
        return mitad * mitad
    else:
        return b * mitad * mitad


print(potencia(2, 4))