# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: MealPlanner
class MealPlannerData:
    def __init__(self):
        self.meals = {}
        self.ingredients = {}
        self.shopping_list = []

    def validate_recipe(self, name, ingredients, servings):
        if not isinstance(name, str) or not name.strip():
            return False, "Название рецепта должно быть непустой строкой."
        if not isinstance(ingredients, dict):
            return False, "Ингредиенты должны быть заданы в виде словаря."
        for ing_name, amount in ingredients.items():
            if not isinstance(ing_name, str) or not ing_name.strip():
                return False, f"Название ингредиента '{ing_name}' должно быть непустой строкой."
            if not isinstance(amount, (int, float)) or amount <= 0:
                return False, f"Количество ингредиента '{ing_name}' должно быть положительным числом."
        if not isinstance(servings, int) or servings <= 0:
            return False, "Порций должно быть целым положительным числом."
        return True, None

    def validate_ingredient(self, name, amount):
        if not isinstance(name, str) or not name.strip():
            return False, "Название ингредиента должно быть непустой строкой."
        if not isinstance(amount, (int, float)) or amount <= 0:
            return False, "Количество ингредиента должно быть положительным числом."
        return True, None

    def add_recipe(self, name, ingredients, servings):
        is_valid, error = self.validate_recipe(name, ingredients, servings)
        if not is_valid:
            print(f"Ошибка валидации рецепта '{name}': {error}")
            return False
        self.meals[name] = {'ingredients': ingredients, 'servings': servings}
        return True

    def add_ingredient(self, name, amount):
        is_valid, error = self.validate_ingredient(name, amount)
        if not is_valid:
            print(f"Ошибка валидации ингредиента '{name}': {error}")
            return False
        self.ingredients[name] = amount
        return True

    def generate_shopping_list(self):
        needed = {}
        for meal_name, data in self.meals.items():
            servings = data['servings']
            for ing, qty in data['ingredients'].items():
                if ing not in needed:
                    needed[ing] = 0.0
                needed[ing] += qty * (1.0 / servings)
        self.shopping_list = [name for name in needed.keys()]
