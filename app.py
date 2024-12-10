from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from http import HTTPStatus


app = Flask(__name__)


app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "recipe"

mysql = MySQL(app)

@app.route('/menus', methods=['GET'])
def get_menus():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Menus")
    menus = cursor.fetchall()

    menu_list = [{"menu_id": menu[0], "menu_name": menu[1], "menu_description": menu[2], "menu_type_code": menu[3]} for menu in menus]
    cursor.close()

    return jsonify(menu_list), HTTPStatus.OK


@app.route('/menus', methods=['POST'])
def create_menu():
    data = request.get_json()

    if not data or not all(key in data for key in ['menu_name', 'menu_description', 'menu_type_code']):
        return jsonify({"error": "Bad Request", "message": "Missing required fields"}), HTTPStatus.BAD_REQUEST

    menu_name = data['menu_name']
    menu_description = data['menu_description']
    menu_type_code = data['menu_type_code']

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO Menus (menu_name, menu_description, menu_type_code) VALUES (%s, %s, %s)", 
                   (menu_name, menu_description, menu_type_code))
    mysql.connection.commit()
    cursor.close()

    return jsonify({"message": "Menu created successfully"}), HTTPStatus.CREATED


@app.route('/menus/<int:menu_id>', methods=['GET'])
def get_menu(menu_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Menus WHERE menu_id = %s", (menu_id,))
    menu = cursor.fetchone()
    cursor.close()

    if not menu:
        return jsonify({"error": "Not Found", "message": "Menu not found"}), HTTPStatus.NOT_FOUND

    return jsonify({
        "menu_id": menu[0],
        "menu_name": menu[1],
        "menu_description": menu[2],
        "menu_type_code": menu[3]
    }), HTTPStatus.OK

@app.route('/menus/<int:menu_id>', methods=['PUT'])
def update_menu(menu_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Menus WHERE menu_id = %s", (menu_id,))
    menu = cursor.fetchone()

    if not menu:
        return jsonify({"error": "Not Found", "message": "Menu not found"}), HTTPStatus.NOT_FOUND

    data = request.get_json()

    menu_name = data.get('menu_name', menu[1])
    menu_description = data.get('menu_description', menu[2])
    menu_type_code = data.get('menu_type_code', menu[3])

    cursor.execute("UPDATE Menus SET menu_name = %s, menu_description = %s, menu_type_code = %s WHERE menu_id = %s", 
                   (menu_name, menu_description, menu_type_code, menu_id))
    mysql.connection.commit()
    cursor.close()

    return jsonify({"message": "Menu updated successfully"}), HTTPStatus.OK


@app.route('/menus/<int:menu_id>', methods=['DELETE'])
def delete_menu(menu_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Menus WHERE menu_id = %s", (menu_id,))
    menu = cursor.fetchone()

    if not menu:
        return jsonify({"error": "Not Found", "message": "Menu not found"}), HTTPStatus.NOT_FOUND

    cursor.execute("DELETE FROM Menus WHERE menu_id = %s", (menu_id,))
    mysql.connection.commit()
    cursor.close()

    return jsonify({"message": "Menu deleted successfully"}), HTTPStatus.NO_CONTENT

if __name__ == '__main__':
    app.run(debug=True)
