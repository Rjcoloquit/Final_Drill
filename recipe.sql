-- Create the database
CREATE DATABASE Recipe;

-- Use the database
USE Recipe;

ALTER TABLE Menus MODIFY menu_id INT AUTO_INCREMENT;

-- Table: Ref_Types (Combining Menu Types and Ingredient Types)
CREATE TABLE Ref_Types (
    type_code VARCHAR(10) PRIMARY KEY,
    type_description VARCHAR(100)
);

-- Table: Menus
CREATE TABLE Menus (
    menu_id INT PRIMARY KEY,
    menu_name VARCHAR(100),
    menu_description VARCHAR(255),
    menu_type_code VARCHAR(10),
    FOREIGN KEY (menu_type_code) REFERENCES Ref_Types(type_code)
);

-- Table: Recipes
CREATE TABLE Recipes (
    recipe_id INT PRIMARY KEY,
    recipe_name VARCHAR(100),
    recipe_description VARCHAR(255)
);

-- Table: Recipe_Steps
CREATE TABLE Recipe_Steps (
    recipe_id INT,
    step_number INT,
    instructions TEXT,
    PRIMARY KEY (recipe_id, step_number),
    FOREIGN KEY (recipe_id) REFERENCES Recipes(recipe_id)
);

-- Table: Ingredients
CREATE TABLE Ingredients (
    ingredient_id INT PRIMARY KEY,
    ingredient_name VARCHAR(100),
    ingredient_type_code VARCHAR(10),
    FOREIGN KEY (ingredient_type_code) REFERENCES Ref_Types(type_code)
);

-- Table: Recipe_Step_Ingredients
CREATE TABLE Recipe_Step_Ingredients (
    recipe_id INT,
    step_number INT,
    ingredient_id INT,
    amount_required VARCHAR(50),
    PRIMARY KEY (recipe_id, step_number, ingredient_id),
    FOREIGN KEY (recipe_id, step_number) REFERENCES Recipe_Steps(recipe_id, step_number),
    FOREIGN KEY (ingredient_id) REFERENCES Ingredients(ingredient_id)
);

-- ------------------------------------------------------------------- --
INSERT INTO Ref_Types (type_code, type_description) VALUES
('MT004', 'Beverage'),
('MT005', 'Side Dish'),
('MT006', 'Soup'),
('IT006', 'Fruit'),
('IT007', 'Nuts');

INSERT INTO Menus (menu_id, menu_name, menu_description, menu_type_code) VALUES
(4, 'Beverage Bonanza', 'Refreshing drinks for all seasons', 'MT004'),
(5, 'Healthy Sides', 'A variety of nutritious side dishes', 'MT005'),
(6, 'Hearty Soups', 'A selection of comforting soups', 'MT006');

INSERT INTO Recipes (recipe_id, recipe_name, recipe_description) VALUES
(6, 'Iced Green Tea', 'A refreshing iced green tea with mint and lemon'),
(7, 'Garlic Mashed Potatoes', 'Creamy mashed potatoes with roasted garlic'),
(8, 'Chicken Caesar Salad', 'A classic Caesar salad with grilled chicken'),
(9, 'Minestrone Soup', 'A hearty Italian soup with vegetables and pasta');

INSERT INTO Ingredients (ingredient_id, ingredient_name, ingredient_type_code) VALUES
(21, 'Mint', 'IT006'),
(22, 'Potato', 'IT001'),
(23, 'Chicken Breast', 'IT002'),
(24, 'Caesar Dressing', 'IT003'),
(25, 'Croutons', 'IT004'),
(26, 'Parmesan Cheese', 'IT003'),
(27, 'Vegetable Broth', 'IT002'),
(28, 'Carrot', 'IT001'),
(29, 'Celery', 'IT001'),
(30, 'Lettuce', 'IT001');

INSERT INTO Recipe_Step_Ingredients (recipe_id, step_number, ingredient_id, amount_required) VALUES
(6, 1, 12, '2 tbsp Olive Oil'),
(6, 1, 21, '1/4 cup Mint'),
(6, 1, 13, '1 Lemon'),
(7, 1, 22, '4 Potatoes'),
(7, 2, 12, '2 tbsp Olive Oil'),
(7, 3, 5, '1/2 cup Cream'),
(8, 1, 23, '2 Chicken Breasts'),
(8, 2, 24, '1/4 cup Caesar Dressing'),
(8, 2, 25, '1/2 cup Croutons'),
(8, 3, 26, '2 tbsp Parmesan Cheese'),
(9, 1, 28, '2 Carrots'),
(9, 1, 29, '2 Celery Sticks'),
(9, 2, 27, '4 cups Vegetable Broth');


INSERT INTO Recipe_Steps (recipe_id, step_number, instructions) VALUES
(6, 1, 'Brew green tea and let it cool to room temperature'),
(6, 2, 'Mix in lemon juice, mint leaves, and a touch of honey'),
(6, 3, 'Serve over ice with additional mint for garnish'),
(7, 1, 'Peel and chop potatoes into chunks'),
(7, 2, 'Boil potatoes in salted water until tender'),
(7, 3, 'Mash potatoes with roasted garlic, cream, and butter'),
(8, 1, 'Grill chicken breasts and slice them thinly'),
(8, 2, 'Toss Romaine lettuce with Caesar dressing'),
(8, 3, 'Top with sliced chicken, croutons, and grated Parmesan'),
(9, 1, 'Sauté onions, carrots, and celery in olive oil'),
(9, 2, 'Add vegetable broth, tomatoes, and pasta to the pot'),
(9, 3, 'Simmer until pasta is tender and vegetables are cooked');


INSERT INTO Ref_Types (type_code, type_description) VALUES
('MT001', 'Appetizer'),
('MT002', 'Main Course'),
('MT003', 'Dessert'),
('IT001', 'Vegetable'),
('IT002', 'Protein'),
('IT003', 'Dairy'),
('IT004', 'Grain'),
('IT005', 'Spice');


INSERT INTO Menus (menu_id, menu_name, menu_description, menu_type_code) VALUES
(1, 'Vegetarian Feast', 'A variety of vegetarian appetizers and main courses', 'MT001'),
(2, 'Seafood Special', 'An assortment of seafood dishes', 'MT002'),
(3, 'Sweet Treats', 'Desserts for every occasion', 'MT003');

INSERT INTO Recipes (recipe_id, recipe_name, recipe_description) VALUES
(1, 'Grilled Veggie Skewers', 'Delicious skewers with a mix of grilled vegetables'),
(2, 'Pasta Primavera', 'A creamy pasta with fresh vegetables'),
(3, 'Chocolate Lava Cake', 'A rich and gooey chocolate dessert'),
(4, 'Lemon Herb Salmon', 'Tender salmon with a zesty lemon herb glaze'),
(5, 'Tomato Basil Soup', 'A creamy and tangy tomato soup');

INSERT INTO Recipe_Steps (recipe_id, step_number, instructions) VALUES
(1, 1, 'Preheat the grill to medium heat and prepare skewers'),
(1, 2, 'Thread vegetables onto skewers and season with salt, pepper, and olive oil'),
(1, 3, 'Grill the skewers for 5-7 minutes until vegetables are tender'),
(2, 1, 'Boil pasta in salted water according to package instructions'),
(2, 2, 'Sauté vegetables in olive oil until tender'),
(2, 3, 'Combine pasta and sautéed vegetables with creamy sauce'),
(3, 1, 'Preheat oven to 350°F (175°C)'),
(3, 2, 'Prepare chocolate cake batter and pour into greased ramekins'),
(3, 3, 'Bake for 12-15 minutes until the outside is firm but the inside is soft'),
(4, 1, 'Season salmon with lemon juice, garlic, and herbs'),
(4, 2, 'Bake the salmon at 400°F for 10-12 minutes until flaky'),
(5, 1, 'Sauté onions and garlic in olive oil until fragrant'),
(5, 2, 'Add crushed tomatoes and simmer for 20 minutes'),
(5, 3, 'Blend the soup until smooth and serve hot');

INSERT INTO Ingredients (ingredient_id, ingredient_name, ingredient_type_code) VALUES
(1, 'Zucchini', 'IT001'),
(2, 'Bell Pepper', 'IT001'),
(3, 'Mushroom', 'IT001'),
(4, 'Pasta', 'IT004'),
(5, 'Cream', 'IT003'),
(6, 'Salmon', 'IT002'),
(7, 'Tomato', 'IT001'),
(8, 'Basil', 'IT005'),
(9, 'Chocolate', 'IT002'),
(10, 'Flour', 'IT004'),
(11, 'Garlic', 'IT001'),
(12, 'Olive Oil', 'IT002'),
(13, 'Lemon', 'IT001'),
(14, 'Cheese', 'IT003'),
(15, 'Onion', 'IT001'),
(16, 'Salt', 'IT005'),
(17, 'Pepper', 'IT005'),
(18, 'Butter', 'IT003'),
(19, 'Egg', 'IT003'),
(20, 'Crushed Tomatoes', 'IT001');

INSERT INTO Recipe_Step_Ingredients (recipe_id, step_number, ingredient_id, amount_required) VALUES
(1, 1, 1, '2 Zucchini'),
(1, 1, 2, '2 Bell Peppers'),
(1, 1, 3, '1 cup Mushrooms'),
(1, 2, 12, '2 tbsp Olive Oil'),
(1, 2, 16, '1 tsp Salt'),
(1, 2, 17, '1 tsp Pepper'),
(2, 1, 4, '200g Pasta'),
(2, 2, 7, '2 Tomatoes'),
(2, 2, 5, '1/2 cup Cream'),
(2, 3, 8, '2 tbsp Basil'),recipes
(3, 1, 9, '100g Chocolate'),
(3, 2, 10, '1/2 cup Flour'),
(3, 2, 18, '1/4 cup Butter'),
(3, 3, 9, '50g Chocolate'),
(4, 1, 6, '2 Salmon Fillets'),
(4, 1, 13, '1 Lemon'),
(4, 2, 12, '1 tbsp Olive Oil'),
(5, 1, 15, '1 Onion'),
(5, 2, 20, '1 can Crushed Tomatoes'),
(5, 3, 5, '1/2 cup Cream');

