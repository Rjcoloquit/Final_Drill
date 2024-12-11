from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from http import HTTPStatus
import logging



logging.basicConfig(level=logging.DEBUG)
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


# MENUS
@app.route('/menus', methods=['GET'])
def get_menus():
    app.logger.debug("Fetching menus from the database...")
    try:
        with mysql.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Menus")
            menus = cursor.fetchall()

        if not menus:
            app.logger.debug("No menus found.")
            return jsonify({"error": "Not Found", "message": "No menus found"}), HTTPStatus.NOT_FOUND
        
        return jsonify(menus), HTTPStatus.OK
    except Exception as e:
        app.logger.error(f"Error occurred: {str(e)}")
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
    data = request.get_json()
    menu_name = data.get('menu_name')
    menu_description = data.get('menu_description')
    menu_type_code = data.get('menu_type_code')

    if not menu_name or not menu_description or not menu_type_code:
        return jsonify({"error": "Bad Request", "message": "Menu name, description, and type code are required"}), 400

    try:
        with mysql.connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO Menus (menu_name, menu_description, menu_type_code)
                VALUES (%s, %s, %s)
            """, (menu_name, menu_description, menu_type_code))
            mysql.connection.commit()

        return jsonify({"message": "Menu created successfully"}), 201
    except Exception as e:
        app.logger.error(f"Error occurred: {str(e)}")
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500


@app.route('/menus/<int:menu_id>', methods=['PUT'])
def update_menu(menu_id):
    """Update a specific menu by ID"""
    try:
        data = request.get_json()
        menu_name = data.get('menu_name')
        menu_description = data.get('menu_description')
        menu_type_code = data.get('menu_type_code')

        if not menu_name and not menu_description and not menu_type_code:
            return jsonify({"error": "Bad Request", "message": "Menu name, description, or type code must be provided"}), HTTPStatus.BAD_REQUEST

        update_fields = []
        update_values = []

        if menu_name:
            update_fields.append("menu_name = %s")
            update_values.append(menu_name)

        if menu_description:
            update_fields.append("menu_description = %s")
            update_values.append(menu_description)

        if menu_type_code:
            update_fields.append("menu_type_code = %s")
            update_values.append(menu_type_code)

        update_values.append(menu_id)

        query = f"UPDATE Menus SET {', '.join(update_fields)} WHERE menu_id = %s"

        with mysql.connection.cursor() as cursor:
            cursor.execute(query, tuple(update_values))
            mysql.connection.commit()

            if cursor.rowcount == 0:
                return jsonify({"error": "Not Found", "message": "Menu not found"}), HTTPStatus.NOT_FOUND

        return jsonify({"message": "Menu updated successfully"}), HTTPStatus.OK

    except Exception as e:
        app.logger.error(f"Error occurred: {str(e)}")
        return jsonify({"error": "Internal Server Error", "message": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

@app.route('/menus/<int:id>', methods=['DELETE'])
def delete_menu(id):
    try:
        with mysql.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Menus WHERE menu_id = %s", (id,))
            menu = cursor.fetchone()

            if cursor.rowcount == 0:
                return jsonify({"error": "Not Found", "message": "Menu not found"}), HTTPStatus.NOT_FOUND

            cursor.execute("DELETE FROM Menus WHERE menu_id = %s", (id,))
            mysql.connection.commit()

        return jsonify({"message": "Menu deleted successfully"}), HTTPStatus.OK
    except Exception as e:
        app.logger.error(f"Error occurred: {str(e)}")
        return jsonify({"error": "Internal Server Error", "message": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

# RECIPES
@app.route('/recipes', methods=['GET'])
def get_recipes():
    try:
        with mysql.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Recipes")
            recipes = cursor.fetchall()
        
        if not recipes: 
            return jsonify({"error": "Not Found", "message": "No recipes found"}), HTTPStatus.NOT_FOUND
        
        return jsonify(recipes), HTTPStatus.OK
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR


@app.route('/recipes', methods=['POST'])
def create_recipe():
    data = request.get_json()
    recipe_name = data.get('recipe_name')
    recipe_description = data.get('recipe_description')

    if not recipe_name or not recipe_description:
        return jsonify({"error": "Bad Request", "message": "Recipe name and description are required"}), 400

    try:
        with mysql.connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO Recipes (recipe_name, recipe_description)
                VALUES (%s, %s)
            """, (recipe_name, recipe_description))
            mysql.connection.commit()

        return jsonify({"message": "Recipe created successfully"}), 201
    except Exception as e:
        app.logger.error(f"Error occurred: {str(e)}")
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500


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
    """Update a specific recipe by ID"""
    try:
        data = request.get_json()
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        if not recipe_name and not recipe_description:
            return jsonify({"error": "Bad Request", "message": "Recipe name or description must be provided"}), HTTPStatus.BAD_REQUEST

        update_fields = []
        update_values = []

        if recipe_name:
            update_fields.append("recipe_name = %s")
            update_values.append(recipe_name)

        if recipe_description:
            update_fields.append("recipe_description = %s")
            update_values.append(recipe_description)

        update_values.append(recipe_id)

        query = f"UPDATE Recipes SET {', '.join(update_fields)} WHERE recipe_id = %s"

        with mysql.connection.cursor() as cursor:
            cursor.execute(query, tuple(update_values))
            mysql.connection.commit()

            if cursor.rowcount == 0:
                return jsonify({"error": "Not Found", "message": "Recipe not found"}), HTTPStatus.NOT_FOUND

        return jsonify({"message": "Recipe updated successfully"}), HTTPStatus.OK

    except Exception as e:
        app.logger.error(f"Error occurred: {str(e)}")
        return jsonify({"error": "Internal Server Error", "message": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR


@app.route('/recipes/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    try:
        with mysql.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Recipes WHERE recipe_id = %s", (id,))
            recipe = cursor.fetchone()

            if cursor.rowcount == 0:
                return jsonify({"error": "Not Found", "message": "Recipe not found"}), HTTPStatus.NOT_FOUND

            cursor.execute("DELETE FROM Recipes WHERE recipe_id = %s", (id,))
            mysql.connection.commit()

        return jsonify({"message": "Recipe deleted successfully"}), HTTPStatus.OK
    except Exception as e:
        app.logger.error(f"Error occurred: {str(e)}")
        return jsonify({"error": "Internal Server Error", "message": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR



@app.errorhandler(500)
def handle_internal_error(error):
    """Handle Internal Server Errors"""
    return jsonify({"error": "Internal Server Error", "message": str(error)}), HTTPStatus.INTERNAL_SERVER_ERROR


if __name__ == '__main__':
    app.run(debug=True)
