'''
Ejercicio 2 - Escribir una función que calcule el máximo común divisor entre dos números. 
'''
def minimo_comun_multiplo(a, b):
    if a > b:
        mayor = a
    else:
        mayor = b

    while True:
        if mayor % a == 0 and mayor % b == 0:
            mcm = mayor
            break
        mayor += 1

    return mcm

print(minimo_comun_multiplo(10, 2))


# Método rápido, utilizando la función lcm (least common multiple) del módulo Math
import math

def minimo_comun_multiplo2(a, b):
    return math.lcm(a, b)

print(minimo_comun_multiplo2(10,2))