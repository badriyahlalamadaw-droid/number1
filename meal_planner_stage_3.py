# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: MealPlanner
class MealPlanner:
    def __init__(self):
        self.meals = {}
        self.products = []
        self.recipes = {}
        self.shopping_list = []

    def add_meal(self, day, meal_type, recipe_name):
        if day not in self.meals:
            self.meals[day] = {}
        self.meals[day][meal_type] = recipe_name

    def add_product(self, name, quantity, unit="шт"):
        self.products.append({"name": name, "quantity": quantity, "unit": unit})

    def add_recipe(self, name, ingredients):
        self.recipes[name] = {"ingredients": ingredients}

    def update_shopping_list(self):
        needed = set()
        for day, meals in self.meals.items():
            for meal_type, recipe_name in meals.items():
                if recipe_name in self.recipes:
                    for ing in self.recipes[recipe_name]["ingredients"]:
                        needed.add(ing)
        return list(needed)
