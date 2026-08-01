# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: MealPlanner
def repair_data():
    """Проверка целостности данных и ремонт простых проблем."""
    problems = []
    
    # Проверка: рецепты должны иметь ингредиенты
    if recipes and any(len(r.get('ingredients', [])) == 0 for r in recipes):
        problems.append("Некоторые рецепты без ингредиентов")
    
    # Проверка: ингредиенты в рецептах должны существовать в списке продуктов
    all_ingredients = set()
    if products:
        for p in products:
            for k, v in p.items():
                if isinstance(v, str):
                    all_ingredients.add(v)
    
    broken_recipes = []
    if recipes:
        for i, recipe in enumerate(recipes):
            missing = [ing for ing in recipe.get('ingredients', []) if ing not in all_ingredients]
            if missing:
                broken_recipes.append((i, missing))
        
        # Ремонт: удаление отсутствующих ингредиентов из рецептов
        for idx, _ in broken_recipes:
            recipes[idx]['ingredients'] = [ing for ing in recipes[idx].get('ingredients', []) if ing in all_ingredients]
    
    # Проверка: ингредиенты в списке покупок должны существовать в продуктах
    shopping_list_products = set()
    if products and shopping_list:
        for p in products:
            for k, v in p.items():
                if isinstance(v, str):
                    shopping_list_products.add(v)
        
        broken_shopping = [item for item in shopping_list if item not in shopping_list_products]
        if broken_shopping:
            problems.append(f"{len(broken_shopping)} позиций в списке покупок не найдено среди продуктов")
    
    # Вывод результатов проверки
    print("=== Проверка целостности данных ===")
    if problems:
        for p in problems:
            print(f"  ⚠️ {p}")
    else:
        print("  ✅ Все данные в порядке!")
