from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/Recipe'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class RefType(db.Model):
    __tablename__ = 'Ref_Types'
    type_code = db.Column(db.String(10), primary_key=True)
    type_description = db.Column(db.String(100))

class Menu(db.Model):
    __tablename__ = 'Menus'
    menu_id = db.Column(db.Integer, primary_key=True)
    menu_name = db.Column(db.String(100))
    menu_description = db.Column(db.String(255))
    menu_type_code = db.Column(db.String(10), db.ForeignKey('Ref_Types.type_code'))
    menu_type = db.relationship('RefType', backref=db.backref('menus', lazy=True))

class Recipe(db.Model):
    __tablename__ = 'Recipes'
    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(100))
    recipe_description = db.Column(db.String(255))

class RecipeStep(db.Model):
    __tablename__ = 'Recipe_Steps'
    recipe_id = db.Column(db.Integer, db.ForeignKey('Recipes.recipe_id'), primary_key=True)
    step_number = db.Column(db.Integer, primary_key=True)
    instructions = db.Column(db.Text)
    recipe = db.relationship('Recipe', backref=db.backref('steps', lazy=True))

class Ingredient(db.Model):
    __tablename__ = 'Ingredients'
    ingredient_id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String(100))
    ingredient_type_code = db.Column(db.String(10), db.ForeignKey('Ref_Types.type_code'))
    ingredient_type = db.relationship('RefType', backref=db.backref('ingredients', lazy=True))

class RecipeStepIngredient(db.Model):
    __tablename__ = 'Recipe_Step_Ingredients'
    recipe_id = db.Column(db.Integer, db.ForeignKey('Recipe_Steps.recipe_id'), primary_key=True)
    step_number = db.Column(db.Integer, db.ForeignKey('Recipe_Steps.step_number'), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('Ingredients.ingredient_id'), primary_key=True)
    amount_required = db.Column(db.String(50))
    recipe_step = db.relationship('RecipeStep', backref=db.backref('step_ingredients', lazy=True))
    ingredient = db.relationship('Ingredient', backref=db.backref('step_ingredients', lazy=True))


@app.errorhandler(SQLAlchemyError)
def handle_db_error(error):
    return jsonify({"error": "Database Error", "message": str(error)}), 500

# CRUD Operations:

# 1. Create a Menu
@app.route('/menus', methods=['POST'])
def create_menu():
    try:
        data = request.get_json()
        menu_name = data.get('menu_name')
        menu_description = data.get('menu_description')
        menu_type_code = data.get('menu_type_code')

        if not menu_name or not menu_description or not menu_type_code:
            return jsonify({"error": "Bad Request", "message": "Missing required fields"}), 400

        menu = Menu(menu_name=menu_name, menu_description=menu_description, menu_type_code=menu_type_code)
        db.session.add(menu)
        db.session.commit()

        return jsonify({"id": menu.menu_id, "name": menu.menu_name, "description": menu.menu_description}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": "Database Error", "message": str(e)}), 500

# 2. Read a Menu
@app.route('/menus/<int:menu_id>', methods=['GET'])
def get_menu(menu_id):
    menu = Menu.query.get(menu_id)
    if not menu:
        return jsonify({"error": "Not Found", "message": "Menu not found"}), 404
    return jsonify({
        "id": menu.menu_id,
        "name": menu.menu_name,
        "description": menu.menu_description,
        "type_code": menu.menu_type_code
    }), 200

# 3. Update a Menu
@app.route('/menus/<int:menu_id>', methods=['PUT'])
def update_menu(menu_id):
    menu = Menu.query.get(menu_id)
    if not menu:
        return jsonify({"error": "Not Found", "message": "Menu not found"}), 404
    
    data = request.get_json()
    menu_name = data.get('menu_name', menu.menu_name)
    menu_description = data.get('menu_description', menu.menu_description)
    menu_type_code = data.get('menu_type_code', menu.menu_type_code)

    menu.menu_name = menu_name
    menu.menu_description = menu_description
    menu.menu_type_code = menu_type_code

    db.session.commit()

    return jsonify({
        "id": menu.menu_id,
        "name": menu.menu_name,
        "description": menu.menu_description,
        "type_code": menu.menu_type_code
    }), 200

# 4. Delete a Menu
@app.route('/menus/<int:menu_id>', methods=['DELETE'])
def delete_menu(menu_id):
    menu = Menu.query.get(menu_id)
    if not menu:
        return jsonify({"error": "Not Found", "message": "Menu not found"}), 404

    db.session.delete(menu)
    db.session.commit()

    return jsonify({"message": "Menu deleted"}), 204

if __name__ == '__main__':
    app.run(debug=True)
