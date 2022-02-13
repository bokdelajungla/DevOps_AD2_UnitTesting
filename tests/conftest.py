# test/conftest.py
import pytest

def pytest_addoption(parser):
    parser.addoption("--file", action="store", help="nombre del fichero de persistencia")
    parser.addoption("--port", action="store", help="numero de puerto de escucha")

@pytest.fixture
def params(request):
    params = {}
    params['file'] = request.config.getoption('--file')
    params['port'] = request.config.getoption('--port')
    if params['file'] is None or params['file'] is None:
        pytest.skip()
    return params
