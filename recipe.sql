-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: recipe
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ingredients`
--

DROP TABLE IF EXISTS `ingredients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingredients` (
  `ingredient_id` int NOT NULL,
  `ingredient_name` varchar(100) DEFAULT NULL,
  `ingredient_type_code` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`ingredient_id`),
  KEY `ingredient_type_code` (`ingredient_type_code`),
  CONSTRAINT `ingredients_ibfk_1` FOREIGN KEY (`ingredient_type_code`) REFERENCES `ref_types` (`type_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredients`
--

LOCK TABLES `ingredients` WRITE;
/*!40000 ALTER TABLE `ingredients` DISABLE KEYS */;
INSERT INTO `ingredients` VALUES (1,'Zucchini','IT001'),(2,'Bell Pepper','IT001'),(3,'Mushroom','IT001'),(4,'Pasta','IT004'),(5,'Cream','IT003'),(6,'Salmon','IT002'),(7,'Tomato','IT001'),(8,'Basil','IT005'),(9,'Chocolate','IT002'),(10,'Flour','IT004'),(11,'Garlic','IT001'),(12,'Olive Oil','IT002'),(13,'Lemon','IT001'),(14,'Cheese','IT003'),(15,'Onion','IT001'),(16,'Salt','IT005'),(17,'Pepper','IT005'),(18,'Butter','IT003'),(19,'Egg','IT003'),(20,'Crushed Tomatoes','IT001'),(21,'Mint','IT006'),(22,'Potato','IT001'),(23,'Chicken Breast','IT002'),(24,'Caesar Dressing','IT003'),(25,'Croutons','IT004'),(26,'Parmesan Cheese','IT003'),(27,'Vegetable Broth','IT002'),(28,'Carrot','IT001'),(29,'Celery','IT001'),(30,'Lettuce','IT001');
/*!40000 ALTER TABLE `ingredients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menus`
--

DROP TABLE IF EXISTS `menus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menus` (
  `menu_id` int NOT NULL AUTO_INCREMENT,
  `menu_name` varchar(100) DEFAULT NULL,
  `menu_description` varchar(255) DEFAULT NULL,
  `menu_type_code` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`menu_id`),
  KEY `menu_type_code` (`menu_type_code`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menus`
--

LOCK TABLES `menus` WRITE;
/*!40000 ALTER TABLE `menus` DISABLE KEYS */;
INSERT INTO `menus` VALUES (2,'Seafood Special','An assortment of seafood dishes','MT002'),(3,'Sweet Treats','Desserts for every occasion','MT003'),(4,'Beverage Bonanza','Refreshing drinks for all seasons','MT004'),(5,'Spaghetti','A delicious Italian pasta dish','Main Course'),(8,'Pasta','A delicious Italian dish','MT002'),(9,'Lemonade','A refreshing citrus drink','BVG001'),(10,'French Fries','Crispy fried potato sticks','SNK001'),(11,'Chicken Alfredo','Creamy chicken pasta','MC002'),(12,'Vegan Salad','A fresh and healthy salad with no animal products','VG001'),(14,'Coffee','Fresh brewed coffee','Beverage'),(15,'Coffee','Fresh brewed coffee','Beverage'),(17,'Spaghetti','A delicious Italian pasta dish','Main Course'),(19,'Lunch Specials','A selection of delicious lunch options','lunch'),(20,'Lunch Specials','A selection of delicious lunch options','lunch'),(21,'Lunch Specials','A selection of delicious lunch options','lunch'),(22,'Lunch Specials','A selection of delicious lunch options','lunch'),(23,'Lunch Specials','A selection of delicious lunch options','lunch'),(24,'Lunch Specials','A selection of delicious lunch options','lunch'),(25,'Lunch Specials','A selection of delicious lunch options','lunch'),(26,'Curry Corner','Rich and flavorful curries','MT026'),(27,'Asian Favorites','Popular Asian-inspired dishes','MT027'),(28,'Pizza Paradise','A variety of delicious pizzas','MT028'),(29,'Wraps & Rolls','Handheld meals wrapped to perfection','MT029'),(30,'Classic Sandwiches','Timeless sandwich recipes','MT030'),(31,'Sushi Selection','An assortment of fresh sushi rolls and nigiri','MT031'),(32,'Classic Cocktails','Signature cocktails with a twist','MT032'),(33,'Taco Treats','Delicious tacos with various fillings','MT033'),(34,'Salad Sensations','Creative salads with fresh ingredients','MT034'),(35,'Gourmet Pizzas','Handcrafted pizzas with gourmet toppings','MT035'),(36,'BBQ Platters','Smoky grilled platters with meats and sides','MT036'),(37,'Fried Favorites','Crispy fried dishes with a variety of sides','MT037'),(38,'Mediterranean Flavors','Tastes from the Mediterranean region','MT038'),(39,'Fresh Smoothies','Healthy and refreshing fruit smoothies','MT039'),(40,'Comforting Soups','A variety of soups for all tastes','MT040'),(41,'Vegan Desserts','Sweet treats made without animal products','MT041'),(42,'Classic Roasts','Slow-roasted meats served with savory sides','MT042'),(43,'Asian Noodles','A variety of noodle dishes from across Asia','MT043'),(44,'Seafood Feast','A selection of seafood dishes','MT044'),(45,'Tasty Tapas','Small Spanish-style plates to share','MT045'),(46,'Healthy Snacks','Wholesome snacks for any time of day','MT046'),(47,'Italian Classics','Traditional Italian dishes made with love','MT047'),(48,'Exotic Fruits','Fresh fruit dishes from around the world','MT048'),(49,'Vegan Comfort Foods','Plant-based comfort foods for everyone','MT049'),(50,'Classic Breakfasts','Traditional breakfast options for a great start','MT050');
/*!40000 ALTER TABLE `menus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipe_step_ingredients`
--

DROP TABLE IF EXISTS `recipe_step_ingredients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recipe_step_ingredients` (
  `recipe_id` int NOT NULL,
  `step_number` int NOT NULL,
  `ingredient_id` int NOT NULL,
  `amount_required` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`recipe_id`,`step_number`,`ingredient_id`),
  KEY `ingredient_id` (`ingredient_id`),
  CONSTRAINT `recipe_step_ingredients_ibfk_1` FOREIGN KEY (`recipe_id`, `step_number`) REFERENCES `recipe_steps` (`recipe_id`, `step_number`),
  CONSTRAINT `recipe_step_ingredients_ibfk_2` FOREIGN KEY (`ingredient_id`) REFERENCES `ingredients` (`ingredient_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipe_step_ingredients`
--

LOCK TABLES `recipe_step_ingredients` WRITE;
/*!40000 ALTER TABLE `recipe_step_ingredients` DISABLE KEYS */;
INSERT INTO `recipe_step_ingredients` VALUES (1,1,1,'2 Zucchini'),(1,1,2,'2 Bell Peppers'),(1,1,3,'1 cup Mushrooms'),(1,2,12,'2 tbsp Olive Oil'),(1,2,16,'1 tsp Salt'),(1,2,17,'1 tsp Pepper'),(2,1,4,'200g Pasta'),(2,2,5,'1/2 cup Cream'),(2,2,7,'2 Tomatoes'),(2,3,8,'2 tbsp Basil'),(3,1,9,'100g Chocolate'),(3,2,10,'1/2 cup Flour'),(3,2,18,'1/4 cup Butter'),(3,3,9,'50g Chocolate'),(4,1,6,'2 Salmon Fillets'),(4,1,13,'1 Lemon'),(4,2,12,'1 tbsp Olive Oil'),(5,1,15,'1 Onion'),(5,2,20,'1 can Crushed Tomatoes'),(5,3,5,'1/2 cup Cream'),(6,1,12,'2 tbsp Olive Oil'),(6,1,13,'1 Lemon'),(6,1,21,'1/4 cup Mint'),(7,1,22,'4 Potatoes'),(7,2,12,'2 tbsp Olive Oil'),(7,3,5,'1/2 cup Cream'),(8,1,23,'2 Chicken Breasts'),(8,2,24,'1/4 cup Caesar Dressing'),(8,2,25,'1/2 cup Croutons'),(8,3,26,'2 tbsp Parmesan Cheese'),(9,1,28,'2 Carrots'),(9,1,29,'2 Celery Sticks'),(9,2,27,'4 cups Vegetable Broth');
/*!40000 ALTER TABLE `recipe_step_ingredients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipe_steps`
--

DROP TABLE IF EXISTS `recipe_steps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recipe_steps` (
  `recipe_id` int NOT NULL,
  `step_number` int NOT NULL,
  `instructions` text,
  PRIMARY KEY (`recipe_id`,`step_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipe_steps`
--

LOCK TABLES `recipe_steps` WRITE;
/*!40000 ALTER TABLE `recipe_steps` DISABLE KEYS */;
INSERT INTO `recipe_steps` VALUES (1,1,'Preheat the grill to medium heat and prepare skewers'),(1,2,'Thread vegetables onto skewers and season with salt, pepper, and olive oil'),(1,3,'Grill the skewers for 5-7 minutes until vegetables are tender'),(2,1,'Boil pasta in salted water according to package instructions'),(2,2,'Sauté vegetables in olive oil until tender'),(2,3,'Combine pasta and sautéed vegetables with creamy sauce'),(3,1,'Preheat oven to 350°F (175°C)'),(3,2,'Prepare chocolate cake batter and pour into greased ramekins'),(3,3,'Bake for 12-15 minutes until the outside is firm but the inside is soft'),(4,1,'Season salmon with lemon juice, garlic, and herbs'),(4,2,'Bake the salmon at 400°F for 10-12 minutes until flaky'),(5,1,'Sauté onions and garlic in olive oil until fragrant'),(5,2,'Add crushed tomatoes and simmer for 20 minutes'),(5,3,'Blend the soup until smooth and serve hot'),(6,1,'Brew green tea and let it cool to room temperature'),(6,2,'Mix in lemon juice, mint leaves, and a touch of honey'),(6,3,'Serve over ice with additional mint for garnish'),(7,1,'Peel and chop potatoes into chunks'),(7,2,'Boil potatoes in salted water until tender'),(7,3,'Mash potatoes with roasted garlic, cream, and butter'),(8,1,'Grill chicken breasts and slice them thinly'),(8,2,'Toss Romaine lettuce with Caesar dressing'),(8,3,'Top with sliced chicken, croutons, and grated Parmesan'),(9,1,'Sauté onions, carrots, and celery in olive oil'),(9,2,'Add vegetable broth, tomatoes, and pasta to the pot'),(9,3,'Simmer until pasta is tender and vegetables are cooked');
/*!40000 ALTER TABLE `recipe_steps` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recipes`
--

DROP TABLE IF EXISTS `recipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recipes` (
  `recipe_id` int NOT NULL AUTO_INCREMENT,
  `recipe_name` varchar(100) DEFAULT NULL,
  `recipe_description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`recipe_id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes`
--

LOCK TABLES `recipes` WRITE;
/*!40000 ALTER TABLE `recipes` DISABLE KEYS */;
INSERT INTO `recipes` VALUES (2,'Pasta Primavera','A creamy pasta with fresh vegetables'),(3,'Chocolate Lava Cake','A rich and gooey chocolate dessert'),(5,'Tomato Basil Soup','A creamy and tangy tomato soup'),(6,'Iced Green Tea','A refreshing iced green tea with mint and lemon'),(7,'Garlic Mashed Potatoes','Creamy mashed potatoes with roasted garlic'),(8,'Chicken Caesar Salad','A classic Caesar salad with grilled chicken'),(9,'Pasta Carbonara Deluxe','An improved version of the classic Pasta Carbonara'),(35,'Vegetable Stir-Fry','A colorful mix of vegetables sautéed in a savory sauce'),(36,'Margherita Pizza','A classic pizza topped with fresh tomatoes, mozzarella, and basil'),(37,'Sushi Rolls','Fresh sushi rolls made with fish, veggies, and rice'),(38,'Chicken Tacos','Spicy marinated chicken wrapped in a soft taco shell'),(39,'Classic Caesar Salad','Crisp romaine lettuce with Caesar dressing, croutons, and parmesan'),(40,'BBQ Ribs','Tender ribs coated with smoky barbecue sauce'),(41,'Fried Chicken','Crispy fried chicken served with a side of coleslaw'),(42,'Lamb Kofta','Grilled lamb meatballs with Mediterranean spices'),(43,'Green Smoothie','A refreshing smoothie made with spinach, banana, and apple'),(44,'Tom Yum Soup','A spicy Thai soup with shrimp and lemongrass'),(45,'Vegan Chocolate Cake','A rich and decadent chocolate cake made without dairy or eggs'),(46,'Beef Wellington','A luxurious beef fillet wrapped in puff pastry'),(47,'Pho','A Vietnamese noodle soup with aromatic broth and fresh herbs'),(48,'Tiramisu','Classic Italian dessert made with coffee-soaked ladyfingers and mascarpone'),(49,'Falafel','Crispy chickpea balls served with tahini sauce'),(50,'Pad Thai','A Thai stir-fried noodle dish with tamarind, peanuts, and lime'),(51,'Vegetarian Lasagna','Layers of pasta, ricotta, and marinara sauce baked to perfection'),(52,'Churros','Fried dough pastries dusted with cinnamon sugar'),(53,'Chicken Parmesan','Breaded chicken topped with marinara sauce and melted cheese'),(54,'Stuffed Bell Peppers','Bell peppers stuffed with rice, ground meat, and vegetables'),(55,'Eggplant Parmesan','Breaded eggplant layered with marinara sauce and cheese'),(56,'Chicken Shawarma','Grilled marinated chicken served in pita with garlic sauce'),(57,'Mushroom Risotto','Creamy rice dish with mushrooms and parmesan'),(58,'Banh Mi','A Vietnamese sandwich with pickled vegetables, pork, and cilantro'),(59,'Cheese Fondue','Melted cheese served with bread and vegetables for dipping'),(60,'Chicken Biryani','Spiced rice and chicken cooked to perfection');
/*!40000 ALTER TABLE `recipes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ref_types`
--

DROP TABLE IF EXISTS `ref_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ref_types` (
  `type_code` varchar(10) NOT NULL,
  `type_description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`type_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ref_types`
--

LOCK TABLES `ref_types` WRITE;
/*!40000 ALTER TABLE `ref_types` DISABLE KEYS */;
INSERT INTO `ref_types` VALUES ('IT001','Vegetable'),('IT002','Protein'),('IT003','Dairy'),('IT004','Grain'),('IT005','Spice'),('IT006','Fruit'),('IT007','Nuts'),('MT001','Appetizer'),('MT002','Main Course'),('MT003','Dessert'),('MT004','Beverage'),('MT005','Side Dish'),('MT006','Soup');
/*!40000 ALTER TABLE `ref_types` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-11 22:08:06
