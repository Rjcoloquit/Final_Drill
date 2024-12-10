from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from http import HTTPStatus

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "recipe"

mysql = MySQL(app)

def validate_menu_data(data, is_update=False):
    """Validates required fields for creating and updating menus"""
    required_fields = ['menu_name', 'menu_description', 'menu_type_code']
    
    if not data:
        return {"error": "Bad Request", "message": "Missing data"}, HTTPStatus.BAD_REQUEST
    
    if not is_update:
        if not all(field in data for field in required_fields):
            return {"error": "Bad Request", "message": "Missing required fields"}, HTTPStatus.BAD_REQUEST
    else:
        if not any(field in data for field in required_fields):
            return {"error": "Bad Request", "message": "No valid fields provided for update"}, HTTPStatus.BAD_REQUEST
    
    return None

@app.route('/')
def welcome():
    """Welcome message"""
    return jsonify({"message": "Welcome to the Recipe API!"}), HTTPStatus.OK


#MENUS
@app.route('/menus', methods=['GET'])
def get_menus():
    """Get all menus"""
    try:
        with mysql.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Menus")
            menus = cursor.fetchall()

        if not menus:
            return jsonify({"error": "Not Found", "message": "No menus found"}), HTTPStatus.NOT_FOUND

        menu_list = [{"menu_id": menu[0], "menu_name": menu[1], "menu_description": menu[2], "menu_type_code": menu[3]} for menu in menus]
        return jsonify(menu_list), HTTPStatus.OK
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

@app.route('/menus/<int:menu_id>', methods=['GET'])
def get_menu(menu_id):
    """Get a specific menu by ID"""
    try:
        with mysql.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Menus WHERE menu_id = %s", (menu_id,))
            menu = cursor.fetchone()

        if not menu:
            return jsonify({"error": "Not Found", "message": "Menu not found"}), HTTPStatus.NOT_FOUND

        return jsonify({
            "menu_id": menu[0],
            "menu_name": menu[1],
            "menu_description": menu[2],
            "menu_type_code": menu[3]
        }), HTTPStatus.OK
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

@app.route('/menus', methods=['POST'])
def create_menu():
    """Create a new menu"""
    data = request.get_json()

    validation_response = validate_menu_data(data)
    if validation_response:
        return jsonify(validation_response[0]), validation_response[1]

    menu_name = data['menu_name']
    menu_description = data['menu_description']
    menu_type_code = data['menu_type_code']

    try:
        with mysql.connection.cursor() as cursor:
            cursor.execute("INSERT INTO Menus (menu_name, menu_description, menu_type_code) VALUES (%s, %s, %s)", 
                           (menu_name, menu_description, menu_type_code))
            mysql.connection.commit()

        return jsonify({"message": "Menu created successfully"}), HTTPStatus.CREATED
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

@app.route('/menus/<int:menu_id>', methods=['PUT'])
def update_menu(menu_id):
    """Update an existing menu by ID"""
    try:
        with mysql.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Menus WHERE menu_id = %s", (menu_id,))
            menu = cursor.fetchone()

        if not menu:
            return jsonify({"error": "Not Found", "message": "Menu not found"}), HTTPStatus.NOT_FOUND

        data = request.get_json()

        validation_response = validate_menu_data(data, is_update=True)
        if validation_response:
            return jsonify(validation_response[0]), validation_response[1]

        menu_name = data.get('menu_name', menu[1])
        menu_description = data.get('menu_description', menu[2])
        menu_type_code = data.get('menu_type_code', menu[3])

        with mysql.connection.cursor() as cursor:
            cursor.execute("UPDATE Menus SET menu_name = %s, menu_description = %s, menu_type_code = %s WHERE menu_id = %s", 
                           (menu_name, menu_description, menu_type_code, menu_id))
            mysql.connection.commit()

        return jsonify({"message": "Menu updated successfully"}), HTTPStatus.OK
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

@app.route('/menus/<int:menu_id>', methods=['DELETE'])
def delete_menu(menu_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Menus WHERE menu_id = %s", (menu_id,))
    menu = cursor.fetchone()

    if menu is None:
        return jsonify({"error": "Not Found", "message": "Menu not found"}), HTTPStatus.NOT_FOUND  

    cursor.execute("DELETE FROM Menus WHERE menu_id = %s", (menu_id,))
    mysql.connection.commit()

    return '', HTTPStatus.NO_CONTENT 

#RECIPES
@app.route('/recipes', methods=['GET'])
def get_recipes():
    """Get all recipes"""
    try:
        with mysql.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Recipes")
            recipes = cursor.fetchall()

        recipe_list = [{"recipe_id": recipe[0], "recipe_name": recipe[1], "recipe_description": recipe[2]} for recipe in recipes]
        return jsonify(recipe_list), HTTPStatus.OK
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR


@app.route('/recipes', methods=['POST'])
def create_recipe():
    """Create a new recipe"""
    data = request.get_json()

    if 'recipe_name' not in data or 'recipe_description' not in data:
        return jsonify({"error": "Bad Request", "message": "Missing required fields"}), HTTPStatus.BAD_REQUEST

    recipe_name = data['recipe_name']
    recipe_description = data['recipe_description']

    try:
        with mysql.connection.cursor() as cursor:
            cursor.execute("INSERT INTO Recipes (recipe_name, recipe_description) VALUES (%s, %s)", 
                           (recipe_name, recipe_description))
            mysql.connection.commit()

        return jsonify({"message": "Recipe created successfully"}), HTTPStatus.CREATED
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR


@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    """Get a specific recipe by ID"""
    try:
        with mysql.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Recipes WHERE recipe_id = %s", (recipe_id,))
            recipe = cursor.fetchone()

        if not recipe:
            return jsonify({"error": "Not Found", "message": "Recipe not found"}), HTTPStatus.NOT_FOUND

        return jsonify({
            "recipe_id": recipe[0],
            "recipe_name": recipe[1],
            "recipe_description": recipe[2]
        }), HTTPStatus.OK
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR


@app.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    """Update an existing recipe by ID"""
    try:
        with mysql.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Recipes WHERE recipe_id = %s", (recipe_id,))
            recipe = cursor.fetchone()

        if not recipe:
            return jsonify({"error": "Not Found", "message": "Recipe not found"}), HTTPStatus.NOT_FOUND

        data = request.get_json()

        recipe_name = data.get('recipe_name', recipe[1])
        recipe_description = data.get('recipe_description', recipe[2])

        with mysql.connection.cursor() as cursor:
            cursor.execute("UPDATE Recipes SET recipe_name = %s, recipe_description = %s WHERE recipe_id = %s", 
                           (recipe_name, recipe_description, recipe_id))
            mysql.connection.commit()

        return jsonify({"message": "Recipe updated successfully"}), HTTPStatus.OK
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR


@app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    try:
        with mysql.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Recipes WHERE recipe_id = %s", (recipe_id,))
            recipe = cursor.fetchone()

            if not recipe:
                return jsonify({"error": "Not Found", "message": "Recipe not found"}), HTTPStatus.NOT_FOUND

            cursor.execute("DELETE FROM Recipes WHERE recipe_id = %s", (recipe_id,))
            mysql.connection.commit()

        return '', HTTPStatus.NO_CONTENT 
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR



@app.errorhandler(500)
def handle_internal_error(error):
    """Handle Internal Server Errors"""
    return jsonify({"error": "Internal Server Error", "message": str(error)}), HTTPStatus.INTERNAL_SERVER_ERROR

if __name__ == '__main__':
    app.run(debug=True)
