# Hacemos uso de la biblioteca unicodedata para tratar las tildes y caracteres epeciales
import unicodedata

# Comprobamos que el fichero de persistencia existe y si no lo creamos
file = open("cadenas.txt", 'w')
file.close()

def almacenar(cadena):
    with open("cadenas.txt", "a+") as f:
        f.write(cadena + '\n')

def consultar(cadena):
    with open("cadenas.txt", "r") as f:
        contador = 0
        for linea in f:
            '''
                Usamos unicodedata.normalize() para eliminar las tildes
                con la opcion NFKD para que lo descomponga en caracteres simples + símbolos aditivos
                lo codificamos a ASCII teniendo en cuenta sólo los caracteres simples (encode('ASCII','ignore'),
                y lo convertimos de nuevo en cadena (decode('ASCII'))
                Por último, usamos el método casefold() para ignorar mayúsculas
            '''
            cadenaAux = unicodedata.normalize('NFKD', cadena).encode('ASCII', 'ignore').decode('ASCII').casefold()
            lineaAux = unicodedata.normalize('NFKD', linea).encode('ASCII', 'ignore').decode('ASCII').casefold()
            if cadenaAux in lineaAux:
                contador = contador + 1
        return contador

def almacenarConsultar(cadAlm, cadCons):
    almacenar(cadAlm)
    return consultar(cadCons)

def test_ficheros():
    assert almacenarConsultar('Hola', 'Hola') == 1
    assert almacenarConsultar('Holá y Adios', 'Hola') == 2
    assert almacenarConsultar('hola HOLA Hóla', 'Hola') == 5
    assert almacenarConsultar('hola HOLA Hóla', 'Adios') == 1