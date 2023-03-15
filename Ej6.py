'''
Ejercicio 6 - Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los 
siguientes métodos para la clase: 
•  Un constructor, donde los datos pueden estar vacíos. 
•  Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos. 
•  mostrar(): Muestra los datos de la persona. 
•  es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad. 
'''

class Persona():
    def __init__(self, nombre, edad, DNI):      # Haría falta un try/except y validar los datos como en los SETTERS
        self.__nombre = nombre          
        self.__edad = edad              
        self.__DNI = DNI                

    # GETTER del nombre, edad y DNI
    @property               
    def nombre(self):
        return f'Nombre: {self.__nombre}'
    
    @property               
    def edad(self):
        return f'Edad: {self.__edad}'
    
    @property               
    def DNI(self):
        return f'DNI: {self.__DNI}'
    
    # SETTER del nombre, edad, DNI (incluye su validación)
    @nombre.setter
    def nombre(self,nuevo_nombre):
        if len(nuevo_nombre) >= 2:
            self.__nombre = nuevo_nombre
        else:       # ACA FALLA
            print("El nombre debe contener al menos 2 caracteres")
            
    @edad.setter
    def edad(self,nueva_edad):
        try:
            nueva_edad=int(nueva_edad)
            if nueva_edad >= 0 and nueva_edad <=99:
                self.__edad = nueva_edad
            else:
                print("Debe ingresar un valor entero entre 0 y 99")

        except ValueError:
            print('ValueError: Debe ingresar un valor numerico entero')

    @DNI.setter
    def DNI(self,nuevo_DNI):
        try:
            nuevo_DNI=int(nuevo_DNI)
            if nuevo_DNI >= 1000000 and nuevo_DNI <=99999999:      # debe estar entre 1 millon y 100 millones-1
                self.__DNI = nuevo_DNI
            else:
                print("Debe ingresar un valor entero entre 1.000.000 y 99.999.999")

        except ValueError:
            print('ValueError: Debe ingresar un valor numerico entero')

    def __str__(self):
        return(f'Nombre: {self.__nombre}, Edad: {self.__edad}, DNI: {self.__DNI}')

    def mostrar(self):
        print(f'Nombre: {self.__nombre}, Edad: {self.__edad}, DNI: {self.__DNI}')

    def es_mayor_de_edad(self):
        if self.__edad >= 18:
            return True
        else:
            return False

# Pruebas
persona1 = Persona("Alejandro", 42, 12345678)

# Verificar que las propiedades sean realmente privadas - Si no lo reconoce está bien
#persona1.__edad     
#persona1.__nombre
#persona1.__DNI

# Pruebo los GETTERS
print(persona1)

# Pruebo los SETTERS
persona1.nombre = "Carlos"
print(persona1)
persona1.nombre = "C"
print(persona1)

persona1.edad = 25
print(persona1)

persona1.edad = "hola"
print(persona1)

persona1.edad = "10"
print(persona1)

persona1.edad = -8
print(persona1)

persona1.DNI = "1000005"
print(persona1)

persona1.DNI = "100005x"
print(persona1)

persona1.DNI = "5.300.005"
print(persona1)

persona1.DNI = 999000
print(persona1)

# Probar el método mostrar()
print("METODO MOSTRAR")
persona1.mostrar()

# Probar el método es_mayor_de_edad()
print("METODO ES_MAYOR_DE_EDAD")
print(persona1.es_mayor_de_edad())