import pytest
from app import app
from unittest.mock import MagicMock

@pytest.fixture
def mock_db(mocker):
    """Mock database connection and cursor."""
    mock_conn = mocker.patch('flask_mysqldb.MySQL.connection')
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
    return mock_cursor

@pytest.fixture

def client():
    """Create a test client for the Flask app."""
    with app.test_client() as client:
        yield client

# MENUS Tests
def test_get_menus_empty(client, mock_db):
    mock_db.fetchall.return_value = []  

    response = client.get('/menus')

    assert response.status_code == 404
    assert b"No menus found" in response.data

def test_get_menus(client, mock_db):
    mock_db.fetchall.return_value = [
        (1, 'Coffee', 'A hot drink made from roasted beans', 'Hot')
    ]

    response = client.get('/menus')

    assert response.status_code == 200
    assert b"Coffee" in response.data
    assert b"A hot drink made from roasted beans" in response.data

def test_post_menu_missing_fields(client):
    response = client.post('/menus', json={})

    assert response.status_code == 400
    assert b"Menu name, description, and type code are required" in response.data

def test_post_menu_success(client, mock_db):
    mock_db.rowcount = 1

    response = client.post('/menus', json={
        'menu_name': 'Latte', 'menu_description': 'A hot milk coffee', 'menu_type_code': 'Hot'
    })

    assert response.status_code == 201
    assert b"Menu created successfully" in response.data

def test_put_menu_missing_fields(client):
    response = client.put('/menus/1', json={})

    assert response.status_code == 400
    assert b"Menu name, description, or type code must be provided" in response.data

def test_put_menu_success(client, mock_db):
    mock_db.rowcount = 1

    response = client.put('/menus/1', json={
        'menu_name': 'Updated Latte', 'menu_description': 'Updated hot milk coffee', 'menu_type_code': 'Hot'
    })

    assert response.status_code == 200
    assert b"Menu updated successfully" in response.data

def test_delete_menu_not_found(client, mock_db):
    mock_db.rowcount = 0

    response = client.delete('/menus/999')

    assert response.status_code == 404
    assert b"Menu not found" in response.data

def test_delete_menu_success(client, mock_db):
    mock_db.rowcount = 1

    response = client.delete('/menus/1')

    assert response.status_code == 200
    assert b"Menu deleted successfully" in response.data

# RECIPES Tests
def test_get_recipes_empty(client, mock_db):
    mock_db.fetchall.return_value = []

    response = client.get('/recipes')

    assert response.status_code == 404
    assert b"No recipes found" in response.data

def test_get_recipes(client, mock_db):
    mock_db.fetchall.return_value = [
        (1, 'Pasta', 'An Italian dish made from wheat and water')
    ]

    response = client.get('/recipes')

    assert response.status_code == 200
    assert b"Pasta" in response.data
    assert b"An Italian dish made from wheat and water" in response.data

def test_post_recipe_missing_fields(client):
    response = client.post('/recipes', json={})

    assert response.status_code == 400
    assert b"Recipe name and description are required" in response.data

def test_post_recipe_success(client, mock_db):
    mock_db.rowcount = 1

    response = client.post('/recipes', json={
        'recipe_name': 'Spaghetti', 'recipe_description': 'A pasta dish with tomato sauce'
    })

    assert response.status_code == 201
    assert b"Recipe created successfully" in response.data

def test_put_recipe_missing_fields(client):
    response = client.put('/recipes/1', json={})

    assert response.status_code == 400
    assert b"Recipe name or description must be provided" in response.data

def test_put_recipe_success(client, mock_db):
    mock_db.rowcount = 1

    response = client.put('/recipes/1', json={
        'recipe_name': 'Updated Spaghetti', 'recipe_description': 'Updated pasta dish with tomato sauce'
    })

    assert response.status_code == 200
    assert b"Recipe updated successfully" in response.data

def test_delete_recipe_not_found(client, mock_db):
    mock_db.rowcount = 0

    response = client.delete('/recipes/999')

    assert response.status_code == 404
    assert b"Recipe not found" in response.data

def test_delete_recipe_success(client, mock_db):
    mock_db.rowcount = 1

    response = client.delete('/recipes/1')

    assert response.status_code == 200
    assert b"Recipe deleted successfully" in response.data


# INGREDIENTS Tests
def test_get_ingredients_empty(client, mock_db):
    mock_db.fetchall.return_value = []  

    response = client.get('/ingredients')

    assert response.status_code == 404
    assert b"No ingredients found" in response.data

def test_get_ingredients(client, mock_db):
    mock_db.fetchall.return_value = [
        (1, 'Sugar', 'Sweetener')
    ]

    response = client.get('/ingredients')

    assert response.status_code == 200
    assert b"Sugar" in response.data
    assert b"Sweetener" in response.data

def test_get_ingredient(client, mock_db):
    mock_db.fetchone.return_value = (1, 'Sugar', 'Sweetener')

    response = client.get('/ingredients/1')

    assert response.status_code == 200
    assert b"Sugar" in response.data
    assert b"Sweetener" in response.data

def test_get_ingredient_not_found(client, mock_db):
    mock_db.fetchone.return_value = None

    response = client.get('/ingredients/999')

    assert response.status_code == 404
    assert b"Ingredient not found" in response.data

def test_post_ingredient_missing_fields(client):
    response = client.post('/ingredients', json={})

    assert response.status_code == 400
    assert b"Ingredient name and type code are required" in response.data

def test_post_ingredient_success(client, mock_db):
    mock_db.rowcount = 1

    response = client.post('/ingredients', json={
        'ingredient_name': 'Salt', 'ingredient_type_code': 'Seasoning'
    })

    assert response.status_code == 201
    assert b"Ingredient created successfully" in response.data

def test_put_ingredient_missing_fields(client):
    response = client.put('/ingredients/1', json={})

    assert response.status_code == 400
    assert b"Ingredient name or type code must be provided" in response.data

def test_put_ingredient_success(client, mock_db):
    mock_db.rowcount = 1

    response = client.put('/ingredients/1', json={
        'ingredient_name': 'Updated Salt', 'ingredient_type_code': 'Seasoning'
    })

    assert response.status_code == 200
    assert b"Ingredient updated successfully" in response.data

def test_delete_ingredient_not_found(client, mock_db):
    mock_db.rowcount = 0

    response = client.delete('/ingredients/999')

    assert response.status_code == 404
    assert b"Ingredient not found" in response.data

def test_delete_ingredient_success(client, mock_db):
    mock_db.rowcount = 1

    response = client.delete('/ingredients/1')

    assert response.status_code == 200
    assert b"Ingredient deleted successfully" in response.data
