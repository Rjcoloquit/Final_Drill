import pytest
from app import app
from unittest.mock import patch, MagicMock
from http import HTTPStatus

@pytest.fixture
def app_with_mocked_mysql(mocker):
    mock_mysql = MagicMock()
    mocker.patch("app.mysql", mock_mysql)
    app.config["TESTING"] = True
    return app


@pytest.fixture
def mock_cursor(mocker):
    mock_connection = MagicMock()
    mock_cursor_instance = mock_connection.cursor.return_value.__enter__.return_value
    mocker.patch("app.mysql.connection", mock_connection)
    return mock_cursor_instance


@pytest.fixture
def client(app_with_mocked_mysql):
    """Flask test client fixture with app context."""
    with app_with_mocked_mysql.app_context():
        with app_with_mocked_mysql.test_client() as client:
            yield client


# Test: POST /menus
def test_create_menu(client, mock_cursor):
    data = {"menu_name": "New Menu", "menu_description": "New Description", "menu_type_code": "Type 1"}

    response = client.post("/menus", json=data)
    assert response.status_code == 201
    assert response.json == {"message": "Menu created successfully"}
    mock_cursor.execute.assert_called_once_with(
        "INSERT INTO Menus (menu_name, menu_description, menu_type_code) VALUES (%s, %s, %s)",
        (data["menu_name"], data["menu_description"], data["menu_type_code"]),
    )


# Test: POST /menus with missing fields
def test_create_menu_missing_fields(client):
    data = {"menu_name": "Incomplete Menu"}
    response = client.post("/menus", json=data)
    assert response.status_code == 400
    assert response.json == {"error": "Bad Request", "message": "Missing required fields"}


# Test: GET /
def test_welcome(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json == {"message": "Welcome to the Recipe API!"}


# Test: GET /menus
def test_get_menus(client, mock_cursor):
    mock_cursor.fetchall.return_value = [
        (1, "Menu 1", "Description 1", "Type 1"),
        (2, "Menu 2", "Description 2", "Type 2"),
    ]

    response = client.get("/menus")
    assert response.status_code == 200
    assert response.json == [
        {"menu_id": 1, "menu_name": "Menu 1", "menu_description": "Description 1", "menu_type_code": "Type 1"},
        {"menu_id": 2, "menu_name": "Menu 2", "menu_description": "Description 2", "menu_type_code": "Type 2"},
    ]


# Test: GET /menus/<id>
def test_get_menu_by_id(client, mock_cursor):
    mock_cursor.fetchone.return_value = (1, "Menu 1", "Description 1", "Type 1")

    response = client.get("/menus/1")
    assert response.status_code == 200
    assert response.json == {
        "menu_id": 1,
        "menu_name": "Menu 1",
        "menu_description": "Description 1",
        "menu_type_code": "Type 1",
    }


def test_get_menu_by_id_not_found(client, mock_cursor):
    mock_cursor.fetchone.return_value = None

    response = client.get("/menus/999")
    assert response.status_code == 404
    assert response.json == {"error": "Not Found", "message": "Menu not found"}


# Test: PUT /menus/<id>
    def test_update_menu(client, mock_cursor):
        mock_cursor.fetchone.return_value = (2, "Menu 2", "Description 2", "Type 2")

        data = {"menu_name": "Updated Menu"}
        response = client.put("/menus/2", json=data)
        assert response.status_code == 200
        assert response.json == {"message": "Menu updated successfully"}
        mock_cursor.execute.assert_called_once_with(
            "UPDATE Menus SET menu_name = %s, menu_description = %s, menu_type_code = %s WHERE menu_id = %s",
            ("Updated Menu", "Description 2", "Type 2", 2),
        )


def test_update_menu_not_found(client, mock_cursor):
    mock_cursor.fetchone.return_value = None

    data = {"menu_name": "Updated Menu"}
    response = client.put("/menus/999", json=data)
    assert response.status_code == 404
    assert response.json == {"error": "Not Found", "message": "Menu not found"}


# Test: DELETE /menus/<id>
def test_delete_menu(client, mock_cursor):
    mock_cursor.fetchone.return_value = (5, "Menu 5", "Description 5", "Type 5")
    response = client.delete("/menus/5")
    assert response.status_code == 204  # Ensure the response code is 204 No Content
    mock_cursor.execute.assert_any_call("SELECT * FROM Menus WHERE menu_id = %s", (5,))
    mock_cursor.execute.assert_any_call("DELETE FROM Menus WHERE menu_id = %s", (5,))

# Test: DELETE /menus/<id> - Item not found
def test_delete_menu_not_found(client, mock_cursor):
    mock_cursor.fetchone.return_value = None
    response = client.delete("/menus/999")
    assert response.status_code == 404  # Ensure 404 is expected
    assert response.json == {"error": "Not Found", "message": "Menu not found"}

