'''
Ejercicio 5 - Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una 
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero 
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el 
ejercicio tanto de manera iterativa como recursiva. 
'''
# Resolución en modo ITERATIVO
# Iterativo significa ir "iterando" hasta lograr la solución
def get_int():
    while True:
        try:
            num = int(input("Ingrese un número entero: "))
            return num
        except ValueError:
            print("El valor ingresado no es un número entero. Intente nuevamente.")      

print(f'Método ITERATIVO: El número ingresado es {get_int()}')



# Resolución en modo RECURSIVO
# Recursivo significa que la función se llama a sí misma hasta encontrar la solución
# Es un poco más complejo de implementar pero es mucho más limpio, ver que la "recursividad" se aplica sólo si falla
# por lo cual es más eficiente este código.
def get_int():
    try:
        num = int(input("Ingrese un número entero: "))
        return num
    except ValueError:
        print("El valor ingresado no es un número entero. Intente nuevamente.")
        return get_int()
    
print(f'Método RECURSIVO: El número ingresado es {get_int()}')