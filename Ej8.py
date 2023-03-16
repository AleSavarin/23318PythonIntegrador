'''
Ejercicio 8 - Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase 
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, 
además del titular y la cantidad se debe guardar una bonificación que estará expresada en 
tanto por ciento. Crear los siguientes métodos para la clase:
•  Un constructor.
•  Los setters y getters para el nuevo atributo.
•  En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo 
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es 
mayor de edad pero menor de 25 años y falso en caso contrario.
•  Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
•  El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la 
cuenta. 


NOTA: No permito instanciar la clase si no está entre los 18 y 25 años, pero los que ya instancié pueder ir cumpliendo años hasta
pasar los 25, en ese caso se hacen "inválidos". Para ello agregué el método, cumple_anios() para simular esta situación.
También hay validaciones para que cuando el titular no sea válido que no tenga bonificación.

'''

from Ej7 import Cuenta

class CuentaJoven(Cuenta):
    def __init__(self, titular='', cantidad=0.0, bonificacion=0, edad=18):     # Haría falta un try/except y validar los datos como en los SETTERS
        if edad < 18 or edad > 25:
            raise ValueError("La edad debe estar entre 18 y 25 años")
        
        super().__init__(titular, cantidad)
        #self.__cantidad = float(cantidad)                            # Tuve que agregar esta línea porque no me lo reconocía.
        self.__bonificacion = int(bonificacion)                      # Tener cuidado que es un porcentaje expresado con un int
        self.__edad = int(edad)
    
    # GETTERS
    @property               
    def bonificacion(self):
        return f'Bonificación: {self.__bonificacion}'
    
    @property       
    def edad(self):
        return f'Edad: {self.__edad}'
    
    # SETTERS
    @bonificacion.setter
    def bonificacion(self, nueva_bonificacion):
        try:
            nueva_bonificacion=int(nueva_bonificacion)
            if (self.__edad >=18 and self.__edad <= 25):
                if (nueva_bonificacion >= 0 and nueva_bonificacion <=100):              # La bonificación debe estar entre 0 y 100%
                    self.__bonificacion = nueva_bonificacion
                else:
                    print("Debe ingresar un valor entero entre 0 y 100")
            else:
                self.__bonificacion = 0
                print("No se cumplen los requisitos de edad para la bonificación")

        except ValueError:
            print('ValueError: Debe ingresar un valor numerico entero')

    # No coloco un Setter para la edad, porque tengo algo similar a un Setter que es el método cumple_anios() 

    # Sobreescritura de los métodos mostrar(), ingresar() y retirar() - Polimorfismo
    def mostrar(self):
        print(f'CUENTA JOVEN, {super().__str__()}, Edad: {self.__edad}, Bonificación: {self.__bonificacion}')        
        #print(f'CUENTA JOVEN, Titular: {self.titular}, Cantidad: {self.__cantidad}, Edad: {self.__edad}, Bonificación: {self.__bonificacion}')

    # Es titular válido
    def es_titular_valido(self):
        if self.__edad >= 18 and self.__edad <=25:
            return True
        else:
            return False
    
    def cumple_anios(self):
        self.__edad += 1

    def ingresar(self, ingreso):
        ingreso=float(ingreso)
        if (ingreso >= 0 and ingreso <= 100000):
            self._cantidad += ingreso                # No puedo cambiarlo!
        else:
            print("Debe ingresar un valor positivo entre 0 y 100000")


    def retirar(self, retiro):
        retiro=float(retiro)
        if self.es_titular_valido():
            if (retiro >= 0 and retiro <= 100000):
                self._cantidad -= retiro              # Tampoco me funciona
                pass              
            else:
                print("Debe ingresar un valor positivo entre 0 y 100000")
        else:
            print("El titular no es válido. No puede retirar dinero")

def main():

    # Pruebo instanciar objetos
    joven1 = CuentaJoven("Pedro", 2300, 50, 25)
    joven1.mostrar()
    joven1.bonificacion = 25
    joven1.ingresar(1000)
    joven1.mostrar()
    joven1.retirar(1000)
    joven1.mostrar()

    joven1.cumple_anios()
    joven1.mostrar()
    joven1.bonificacion = 25
    joven1.mostrar()
    joven1.ingresar(1000)
    joven1.mostrar()
    joven1.retirar(1000)
    joven1.mostrar()


# Para que sólo se ejecute si estoy en este mismo archivo y no cuando lo utilice como módulo
if __name__ == '__main__':
    main()