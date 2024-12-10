# Recipe API

## Description
The Recipe API is a RESTful service built with Flask that allows you to manage menus. 
It includes operations for creating, retrieving, updating, and deleting menus in a MySQL database.

## Installation
```cmd```
pip install -r requirements.txt

Configuration
Environment variables needed:

- MYSQL_HOST: Database host (localhost)
- MYSQL_USER: MySQL username (root)
- MYSQL_PASSWORD: MySQL password (root)
- MYSQL_DB: Database name (recipe)

## API Endpoints

| Endpoint              | Method | Description                   |
|-----------------------|--------|-------------------------------|
| `/menus`              | GET    | Get all menus                 |
| `/menus`              | POST   | Create a new menu             |
| `/menus/<int:menu_id>`| GET    | Get a specific menu by ID     |
| `/menus/<int:menu_id>`| PUT    | Update a specific menu by ID  |
| `/menus/<int:menu_id>`| DELETE | Delete a specific menu by ID  |

Testing
To run tests, ensure you have pytest installed and execute the following command:
pytest


Git Commit Guidelines

```bash```
Use conventional commits:

feat: add user authentication
fix: resolve the database connection issue
docs: update API documentation
test: add user registration tests


