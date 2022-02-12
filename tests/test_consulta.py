
from server import app

def test_consulta_get():
    # Create a test client using the Flask application configured for testing
    with app.test_client() as test_client:
        response = test_client.get('/consulta?string=test')
        assert response.status_code == 200
        assert b"Lineas en las que aparece" in response.data
    return 0

def test_consulta_bad_request_no_string_parameter():
    # Create a test client using the Flask application configured for testing
    with app.test_client() as test_client:
        response = test_client.get('/consulta?bad=test')
        assert response.status_code == 400
        assert b"string" in response.data
    return 0

def test_consulta_bad_request_2_words():
    # Create a test client using the Flask application configured for testing
    with app.test_client() as test_client:
        response = test_client.get('/consulta?string=test espacio')
        assert response.status_code == 400
        assert b"palabra" in response.data
    return 0

def test_consulta_bad_request_wrong_method():
    # Create a test client using the Flask application configured for testing
    with app.test_client() as test_client:
        response = test_client.post('/consulta?string=test')
        assert response.status_code == 405
    return 0
