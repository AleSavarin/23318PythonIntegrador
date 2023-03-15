'''
Ejercicio 3 - Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con 
cada palabra que contiene y la cantidad de veces que aparece (cantidad). 
NOTA: Funciona con algunos errores porque no logro quitar del todo los signos de puntuación.
'''
import string       # Para trabajar con los signos de puntuación


def palabras_cantidad(cadena):
    palabras = cadena.split()
    cantidad = {}

    for palabra in palabras:
        palabra.rstrip(string.punctuation)     # Quita signos de puntuación al final
        if palabra in cantidad:
            cantidad[palabra] += 1
        else:
            cantidad[palabra] = 1

    return cantidad

def imprimir_resultados(diccionario, cadena):
    print(f'En la cadena \"{cadena}\" se tienen las siguientes palabras con su frecuencia:')
    for palabra in diccionario:
        print(f'{palabra}, {diccionario[palabra]}')

cadena = "Los peces también nadan"
diccionario = palabras_cantidad(cadena)
imprimir_resultados(diccionario, cadena)


cadena2 = "María Chocena su choza chozaba y un chozador que por ahí pasaba le dijo, María Chocena tu chozas tu choza o chozas la ajena, no chozo mi choza ni chozo la ajena, yo chozo la choza de María Chocena"
diccionario2 = palabras_cantidad(cadena2)
imprimir_resultados(diccionario2, cadena2)