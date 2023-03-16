'''
Ejercicio 7 - Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una 
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es 
opcional. Crear los siguientes métodos para la clase:
•  Un constructor, donde los datos pueden estar vacíos.
•  Los setters y getters para cada uno de los atributos. El atributo no se puede modificar 
directamente, sólo ingresando o retirando dinero.
•  mostrar(): Muestra los datos de la cuenta.
•  ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es 
negativa, no se hará nada.
•  retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números 
rojos.
'''

class Cuenta():
    def __init__(self, titular='', cantidad=0.0):       # Haría falta un try/except y validar los datos como en los SETTERS
        self.__titular = titular
        self.__cantidad = float(cantidad)               


    # GETTERS
    @property               
    def titular(self):
        return self.__titular
    
    @property               
    def cantidad(self):
        return float(self.__cantidad)

    # SETTERS
    # Defino este SETTER para el Ej8
    @cantidad.setter
    def cantidad(self,nueva_cantidad):
        try:
            nueva_cantidad=float(nueva_cantidad)
            if nueva_cantidad >= 0 and nueva_cantidad <= 100000:
                self.__cantidad = nueva_cantidad
            else:
                print("Debe ingresar un valor entre 0 y 100000")

        except ValueError:
            print('ValueError: Debe ingresar un valor numerico')


    # Métodos de INSTANCIA
    def mostrar(self):
        print(f'Titular: {self.__titular}, Cantidad: {self.__cantidad}')

    def ingresar(self, ingreso):
        ingreso=float(ingreso)
        if ingreso >= 0 and ingreso <= 100000:
            self.__cantidad += ingreso
        else:
            print("Debe ingresar un valor positivo entre 0 y 100000")

    def retirar(self, retiro):
        ingreso=float(retiro)
        if retiro >= 0 and retiro <= 100000:
            self.__cantidad -= retiro
        else:
            print("Debe ingresar un valor positivo entre 0 y 100000")

    def __str__(self):
        return(f'Titular: {self.__titular}, Cantidad: {self.__cantidad}')


# Prueba del ejercicio
def main():
    # Pruebo la instanciación
    cuenta1 = Cuenta()
    cuenta2 = Cuenta("Alejandro", 1000)
    cuenta3 = Cuenta("Alejandro")
    print(cuenta1)
    print(cuenta2)
    print(cuenta3)

    # Pruebo el método mostrar()
    cuenta1.mostrar()

    # Pruebo los métodos ingresar y retirar
    print("Ingreso y retiro 1000")
    cuenta3.ingresar(1000)
    cuenta3.mostrar()
    cuenta3.retirar(1000)
    cuenta3.mostrar()

# Utilizo este concepto para poder utilizar este archivo como módulo y que no se ejecuten las pruebas de arriba
if __name__ == "__main__":
    main()
