# Hacemos uso de la biblioteca unicodedata para tratar las tildes y caracteres epeciales
import unicodedata

# Método misma cadena
def cadena(cadena):
    '''
        Usamos unicodedata.normalize() para eliminar las tildes
        con la opcion NFKD para que lo descomponga en caracteres simples + símbolos aditivos
        lo codificamos a ASCII teniendo en cuenta sólo los caracteres simples (encode('ASCII','ignore'),
        y lo convertimos de nuevo en cadena (decode('ASCII'))
        Por último, usamos el método casefold() para ignorar mayúsculas
    '''
    return unicodedata.normalize('NFKD', cadena).encode('ASCII', 'ignore').decode('ASCII').casefold()

# Test unitarios misma cadena
def test_cadena():
    assert cadena('Hola') == 'hola'
    assert cadena('HOLA') == 'hola'
    assert cadena('Holá') == 'hola'
    assert cadena('HOLÁ') == 'hola' 
