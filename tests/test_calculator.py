import pytest
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage_get(client):
    """Test that the homepage loads correctly"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Calculator' in rv.data

def test_addition(client):
    """Test addition operation"""
    rv = client.post('/', data={
        'num1': '5',
        'num2': '3',
        'operator': 'add'
    })
    assert b'8' in rv.data

def test_subtraction(client):
    """Test subtraction operation"""
    rv = client.post('/', data={
        'num1': '10',
        'num2': '4',
        'operator': 'subtract'
    })
    assert b'6' in rv.data

def test_multiplication(client):
    """Test multiplication operation"""
    rv = client.post('/', data={
        'num1': '6',
        'num2': '7',
        'operator': 'multiply'
    })
    assert b'42' in rv.data

def test_division(client):
    """Test division operation"""
    rv = client.post('/', data={
        'num1': '15',
        'num2': '3',
        'operator': 'divide'
    })
    assert b'5' in rv.data

def test_division_by_zero(client):
    """Test division by zero error handling"""
    rv = client.post('/', data={
        'num1': '10',
        'num2': '0',
        'operator': 'divide'
    })
    assert b'Division by zero is not allowed' in rv.data

def test_invalid_input(client):
    """Test invalid input error handling"""
    rv = client.post('/', data={
        'num1': 'abc',
        'num2': '5',
        'operator': 'add'
    })
    assert b'Please enter valid numbers' in rv.data