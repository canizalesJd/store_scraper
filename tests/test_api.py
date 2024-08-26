import pytest
from flask import Flask
from api.main import app 

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_books(client):
    response = client.get('/books')
    assert response.status_code == 200
    assert response.is_json

def test_get_books_by_category(client):
    response = client.get('/books/mystery')
    assert response.status_code == 200
    assert response.is_json
    assert len(response.json) > 0

    # Test a non-existent category
    response = client.get('/books/nonexistent_category')
    assert response.status_code == 404

def test_search_books(client):
    # Assuming there are books with the word 'python' in the title
    response = client.get('/search?q=Space')
    assert response.status_code == 200
    assert response.is_json
    assert len(response.json) > 0

    # Test search with no results
    response = client.get('/search?q=nonexistent')
    assert response.status_code == 404

    # Test search with no query parameter
    response = client.get('/search')
    assert response.status_code == 400
