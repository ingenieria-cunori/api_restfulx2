import pytest
from app import create_app

# Las fixtures son funciones que preparan el terreno para los tests
@pytest.fixture
def app():
    app = create_app('test')
    yield app

@pytest.fixture
def client(app):
    """Crea un cliente de pruebas de Flask"""
    return app.test_client()

def test_convert_success(client):
    """
    Test que verifica la conversión exitosa de un número a letras.
    Nota como 'client' se inyecta automáticamente desde la fixture.
    """
    payload = {'number': 5} # Pytest maneja mejor los dicts
    response = client.post(
        '/convert/to-words',
        json=payload # Flask y Pytest permiten pasar 'json' directamente
    )
    
    data = response.get_json()
    assert response.status_code == 200
    assert data['words'] == 'cinco'

def test_convert_out_of_range(client):
    """Test para verificar que números fuera de rango fallan"""
    payload = {'number': 15}
    response = client.post(
        '/convert/to-words',
        json=payload
    )
    assert response.status_code == 400