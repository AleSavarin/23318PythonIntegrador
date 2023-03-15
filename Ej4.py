'''
Ejercicio 4 - Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada 
palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función 
que reciba el diccionario generado con la función anterior y devuelva una tupla con la 
palabra más repetida y su frecuencia. 
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
    print(f'En la cadena \"{cadena}\" se tienen las siguientes palabras con su cantidad:')
    for palabra in diccionario:
        print(f'{palabra}, {diccionario[palabra]}')

    # Imprimo la palabra que más veces se repite y cuantas veces se repite
    print(max(diccionario, key=diccionario.get), diccionario[max(diccionario, key=diccionario.get)])

cadena = "Los peces también nadan"
diccionario = palabras_cantidad(cadena)
imprimir_resultados(diccionario, cadena)


cadena2 = "María Chocena su choza chozaba y un chozador que por ahí pasaba le dijo, María Chocena tu chozas tu choza o chozas la ajena, no chozo mi choza ni chozo la ajena, yo chozo la choza de María Chocena"
diccionario2 = palabras_cantidad(cadena2)
imprimir_resultados(diccionario2, cadena2)