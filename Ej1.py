'''
Ejercicio 1 - Escribir una función que calcule el máximo común divisor entre dos números. 
'''
def maximo_comun_divisor(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

print(maximo_comun_divisor(10, 2))


# Método rápido, utilizando la función gcd (greatest common divisor) del módulo Math
import math

def maximo_comun_divisor2(a, b):
    return math.gcd(a, b)

print(maximo_comun_divisor2(10,2))