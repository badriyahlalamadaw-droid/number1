# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: MealPlanner
def generate_summary():
    if not recipes:
        print("Нет данных для сводки.")
        return
    
    total_recipes = len(recipes)
    unique_ingredients = set()
    
    for recipe in recipes:
        for ingredient, amount in recipe.get('ingredients', {}).items():
            unique_ingredients.add(ingredient)
            
    print(f"Сводка по {total_recipes} рецептам:")
    print(f"Уникальных продуктов в меню: {len(unique_ingredients)}")
    
    if shopping_list:
        total_items = sum(len(items) for items in shopping_list.values())
        print(f"Позиций в списке покупок: {total_items}")
        
    meal_plan = {}
    for day, meals in menu.items():
        for meal_type, recipe_name in meals.items():
            if recipe_name not in meal_plan:
                meal_plan[recipe_name] = 0
            meal_plan[recipe_name] += 1
            
    print(f"Распределение по дням недели:")
    for day, meals in menu.items():
        print(f"{day}: {', '.join(meals.values())}")
