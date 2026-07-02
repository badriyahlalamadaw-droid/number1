# === Stage 17: Добавь группировку записей по категориям ===
# Project: MealPlanner
def group_by_category(items, categories):
    grouped = {cat: [] for cat in categories}
    for item in items:
        category = item.get('category', 'other')
        if category not in grouped:
            grouped[category] = []
        grouped[category].append(item)
    return grouped

def generate_shopping_list(recipe_plan, ingredients_db):
    needed_ingredients = {}
    for day, meals in recipe_plan.items():
        for meal_name, recipes in meals.items():
            for recipe in recipes:
                if 'ingredients' not in recipe or not recipe['ingredients']:
                    continue
                for ing in recipe['ingredients']:
                    name = ing.get('name', '')
                    needed_ingredients[name] = needed_ingredients.get(name, 0) + ing.get('quantity', 1)
    grouped_list = group_by_category(list(needed_ingredients.items()), ['Овощи', 'Мясо', 'Бакалея', 'Другое'])
    return {cat: items for cat, items in grouped_list.items() if items}
