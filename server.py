'''
Servicio Web que escucha en el puerto 12345
y tiene dos endpoints
una que guarda la cadena que se le envia como parámetro en un fichero
y otro que devuelve el número de veces de una cadena aparece al menos una vez
en cada una de las lineas del fichero, ignorando mayúsculas y tildes

@autor: Jorge Sánchez-Alor

'''

# ***IMPORTS*** #
# Empleamos la biblioteca FLASK para implementar el servicio web
from flask import Flask
from flask import request
from flask import make_response
from flask import jsonify
# Hacemos uso de la biblioteca unicodedata para tratar las tildes y caracteres epeciales
import unicodedata
# Para hacer uso de argumentos
import sys
import argparse

# *** VARIABLES *** #
# Nombre del fichero de persistencia
FILENAME = "cadenas.txt" #Fichero por defecto
# Host
HOST = "127.0.0.1"
# Puerto
PORT = 12345 #Puerto por defecto

# La aplicación a partir de la clase Flask
app = Flask(__name__)

# *** METODOS *** #
# Comprobación de argumentos
def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-f", '--file', type=str, help="nombre del fichero de persistencia", required=False, default=FILENAME)
    parser.add_argument("-p", '--port', type=int, help="numero de puerto de escucha", required=False, default=PORT)
    parser.add_argument("-t", '--test', action='store_true', help="Levanta un servidor para los tests", required=False)
    args = parser.parse_args()
    if(args.test):
        args.port = 23456
        args.file = "tests/test.txt"
        print("Ejecutando el servidor de tests")

    print("Escuchando en puerto: ", args.port)
    return args.file, args.port


# Comprobación existencia del fichero de persistencia
def check_file(fichero):
    try:
        with open(fichero, "x") as f: #Si el fichero existe lanza una excepcion
            print("Creando fichero de persistencia: " + fichero)
            return 0

    except FileExistsError:
        print("Encontrado fichero de persistencia...")
        print("Cargando datos de " + fichero)
        return 1


# Con @app.route() marcamos el comportamiento que llevará a cabo nuestra aplicación
# Endpoint Home Page
@app.route("/")
def home():
    return "<h1>Servicio Web para Cadenas</h1><br>"


# El endpoint "almacena"
'''
El endpoint recibe la cadena como parámetro y la guarda en una nueva línea del fichero FILENAME
El nombre del parámetro es 'string'
la petición tiene el formato /almacena?string
Devuelve: 
    * una respuesta HTML 200 OK con un json en el cuerpo indicando que el mensaje se ha creado correctamente
    * una respuesta HTML 400 BAD REQUEST con un json en el cuerpo si la petición no es correcta
'''


@app.route("/almacena", methods=['POST'])
def almacenar():
    if request.method == 'POST':
        if 'string' in request.args:
            cadena = request.args.get('string')
            with open(FILENAME, "a+") as f:
                f.write(cadena + '\n')
            data = {'code': 'SUCCESS', 'message': cadena + ' ADDED'}
            return make_response(jsonify(data), 200)
        else:
            data = {'code': 'BAD REQUEST', 'message': 'No se ha encontrado el parámetro "string"'}
            return make_response(jsonify(data), 400)


# El endpoint "consulta"
'''
El endpoint recibe la cadena como parámetro y comprueba el número de veces que aparece dentro del fichero
FILENAME
El nombre del parámetro es 'string'
Devuelve:
Devuelve: 
    * una respuesta HTML 200 OK con un json en el cuerpo indicando el número de veces que se ha encontrado la palabra
    * una respuesta HTML 400 BAD REQUEST con un json en el cuerpo si la petición no es correctauna respuesta
'''


@app.route("/consulta", methods=['GET'])
def consultar():
    if request.method == 'GET':
        if 'string' in request.args:
            cadena = request.args.get('string')
            if " " not in cadena:
                with open(FILENAME, "r") as f:
                    contador = 0
                    for linea in f:
                        '''
                        Usamos unicodedata.normalize() para eliminar las tildes
                        con la opcion NFKD para que lo descomponga en caracteres simples + símbolos aditivos
                        lo codificamos a ASCII teniendo en cuenta sólo los caracteres simples (encode('ASCII','ignore'),
                        y lo convertimos de nuevo en cadena (decode('ASCII'))
                        Por último, usamos el método casefold() para ignorar mayúsculas
                        '''
                        cadena_aux = unicodedata.normalize('NFKD', cadena).encode('ASCII', 'ignore').decode(
                            'ASCII').casefold()
                        linea_aux = unicodedata.normalize('NFKD', linea).encode('ASCII', 'ignore').decode(
                            'ASCII').casefold()
                        if cadena_aux in linea_aux:
                            contador = contador + 1
                data = {'code': 'SUCCESS', 'Lineas en las que aparece': contador}
                return make_response(jsonify(data), 200)
            else:
                data = {'code': 'BAD REQUEST', 'message': 'El parámetro debe ser una única palabra'}
                return make_response(jsonify(data), 400)
        else:
            data = {'code': 'BAD REQUEST', 'message': 'No se ha encontrado el parámetro string'}
            return make_response(jsonify(data), 400)


# Para que se inicie la aplicación al ejecutar el script
# (Esto se excluye del test porque
# check_file() tiene su propio test
# main() tiene también su propio test
# y app.run() depende de Flask)
if __name__ == "__main__": #pragma: no cover
    file, port = main()
    FILENAME = file
    PORT = port
    check_file(file)
    app.run(host=HOST, port=port)
