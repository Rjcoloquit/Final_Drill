from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from http import HTTPStatus


app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "recipe"

mysql = MySQL(app)


def validate_menu_data(data):
    required_fields = ['menu_name', 'menu_description', 'menu_type_code']
    if not data or not all(field in data for field in required_fields):
        return jsonify({"error": "Bad Request", "message": "Missing required fields"}), HTTPStatus.BAD_REQUEST
    
    return None


@app.route('/menus', methods=['GET'])
def get_menus():
    try:
        with mysql.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Menus")
            menus = cursor.fetchall()

        menu_list = [{"menu_id": menu[0], "menu_name": menu[1], "menu_description": menu[2], "menu_type_code": menu[3]} for menu in menus]
        return jsonify(menu_list), HTTPStatus.OK
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR


@app.route('/menus', methods=['POST'])
def create_menu():
    data = request.get_json()

    validation_response = validate_menu_data(data)
    if validation_response:
        return validation_response

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


@app.route('/menus/<int:menu_id>', methods=['GET'])
def get_menu(menu_id):
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


@app.route('/menus/<int:menu_id>', methods=['PUT'])
def update_menu(menu_id):
    try:
        with mysql.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Menus WHERE menu_id = %s", (menu_id,))
            menu = cursor.fetchone()

        if not menu:
            return jsonify({"error": "Not Found", "message": "Menu not found"}), HTTPStatus.NOT_FOUND

        data = request.get_json()

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
    try:
        with mysql.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Menus WHERE menu_id = %s", (menu_id,))
            menu = cursor.fetchone()

        if not menu:
            return jsonify({"error": "Not Found", "message": "Menu not found"}), HTTPStatus.NOT_FOUND

        with mysql.connection.cursor() as cursor:
            cursor.execute("DELETE FROM Menus WHERE menu_id = %s", (menu_id,))
            mysql.connection.commit()

        return jsonify({"message": "Menu deleted successfully"}), HTTPStatus.NO_CONTENT
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR


@app.errorhandler(Exception)
def handle_unexpected_error(error):
    return jsonify({"error": "Internal Server Error", "message": str(error)}), HTTPStatus.INTERNAL_SERVER_ERROR


if __name__ == '__main__':
    app.run(debug=True)
