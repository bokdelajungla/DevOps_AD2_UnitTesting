
from server import app
from flaskr.db import init_db



def test_empty_db(client):
    """Start with a blank database."""

    rv = client.get('/')
    assert b'<h1>Servicio Web para Cadenas</h1><br>' in rv.data

def test_endpoints(client):
    rv = client.post('/almacena/cadena')
    rv = client.post('/consulta/cadena')
    assert b'Lineas en las que aparece: 1' in rv.data

    rv = client.post('/consulta/cadena cadena')
    assert b'El parametro debe ser una unica palabra' in rv.data

    rv = client.post('/otracosa')
    assert b'No se ha encontrado el parametro string' in rv.data

    rv = client.post('/almacena/cadena+CÁDENA+Cádena')
    rv = client.post('/consulta/cadena')
    '''
        Una de las cadenas ya ha sido almacenada antes del primer assert
    '''
    assert b'Lineas en las que aparece: 4' in rv.data