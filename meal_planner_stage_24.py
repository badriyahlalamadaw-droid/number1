# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: MealPlanner
def print_recipe_card(recipe):
    """Компактная карточка рецепта: название, ингредиенты, шаги."""
    title = recipe.get("title", "Без названия")
    prep = recipe.get("prep_time", "")
    cook = recipe.get("cook_time", "")
    
    ingredients = recipe.get("ingredients", [])
    steps = recipe.get("steps", [])
    
    print(f"\n{'═'*40}")
    print(f"  📖 {title}")
    
    if prep or cook:
        times = []
        if prep:
            times.append(f"⏱️ Подготовить: {prep}")
        if cook:
            times.append(f"🔥 Готовить: {cook}")
        print("  " + " | ".join(times))
    
    if ingredients:
        print("  🛒 Ингредиенты:")
        for i, ing in enumerate(ingredients, 1):
            print(f"     {i}. {ing}")
    
    if steps:
        print("  👨‍🍳 Приготовление:")
        for step_num, step in enumerate(steps, 1):
            print(f"     Шаг {step_num}: {step}")
