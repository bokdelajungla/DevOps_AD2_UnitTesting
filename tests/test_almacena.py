
from server import app

# El endpoint "almacena"
'''
El endpoint recibe la cadena como parámetro y la guarda en una nueva línea del fichero cadenas.txt
El nombre del parámetro es 'string'
la petición tiene el formato /almacena?string
Devuelve: 
    * una respuesta HTML 200 OK con un json en el cuerpo indicando que el mensaje se ha creado correctamente
    * una respuesta HTML 400 BAD REQUEST con un json en el cuerpo si la petición no es correcta
'''
'''
def almacenar():
if request.method == 'POST':
    if 'string' in request.args:
        cadena = request.args.get('string')
        with open("cadenas.txt", "a+") as f:
            f.write(cadena + '\n')
        data = {'code': 'SUCCES', 'message': cadena + ' ADDED'}
        return make_response(jsonify(data), 200)
    else:
        data = {'code': 'BAD REQUEST', 'message': 'No se ha encontrado el parámetro "string"'}
        return make_response(jsonify(data), 400)
'''

def test_almacena_post():
    # Create a test client using the Flask application configured for testing
    with app.test_client() as test_client:
        response = test_client.post('/almacena?string=test')
        assert response.status_code == 200
        assert b"test" in response.data
    return 0

def test_almacena_bad_request_no_string_parameter():
    # Create a test client using the Flask application configured for testing
    with app.test_client() as test_client:
        response = test_client.post('/almacena?bad=test')
        assert response.status_code == 400
        assert b"string" in response.data
    return 0

def test_almacena_get():
    # Create a test client using the Flask application configured for testing
    with app.test_client() as test_client:
        response = test_client.get('/almacena?string=test')
        assert response.status_code == 405
    return 0
