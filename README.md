# Recipe API

## Description
The Recipe API is a RESTful service built with Flask that allows you to manage menus. 
It includes operations for creating, retrieving, updating, and deleting menus in a MySQL database.

## Installation
```cmd```
pip install -r requirements.txt

Configuration
To configure the database:
1. Upload the ```recipe``` MySQL database to your server or local machine.
2. Update the database configuration in the Flask app with your database connection details.

- ```MYSQL_HOST```: Database host (localhost)
- ```MYSQL_USER```: MySQL username (root)
- ```MYSQL_PASSWORD```: MySQL password (root)
- ```MYSQL_DB```: Database name (recipe)

## API Endpoints

| Endpoint              | Method | Description                   |
|-----------------------|--------|-------------------------------|
| `/menus`              | GET    | Get all menus                 |
| `/menus`              | POST   | Create a new menu             |
| `/menus/<int:menu_id>`| GET    | Get a specific menu by ID     |
| `/menus/<int:menu_id>`| PUT    | Update a specific menu by ID  |
| `/menus/<int:menu_id>`| DELETE | Delete a specific menu by ID  |
|`/recipes`|GET|Get all recipes|
|`/recipes`|POST|Create a new recipe|
|`/recipes/<int:recipe_id>`|GET|Get a specific recipe by ID|
|`/recipes/<int:recipe_id>`|PUT|Update a specific recipe by ID|
|`/recipes/<int:recipe_id>`|DELETE|Delete a specific recipe by ID|
|`/ingredients`|GET|Get all ingredients|
|`/ingredients`|POST|Create a new ingredient|
|`/ingredients/<int:ingredient_id>`|GET|Get a specific ingredient by ID|
|`/ingredients/<int:ingredient_id>`|PUT|Update a specific ingredient by ID|
|`/ingredients/<int:ingredient_id>`|DELETE|Delete a specific ingredient by ID|

Testing
To run tests, ensure you have pytest installed and execute the following command:
- pytest


Git Commit Guidelines

```bash```
Use conventional commits:

- feat: add user authentication
- fix: resolve the database connection issue
- docs: update API documentation
- test: add user registration tests


