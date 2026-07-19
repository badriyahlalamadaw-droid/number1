# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: MealPlanner
def project_metrics():
    total_recipes = len(recipes) if recipes else 0
    total_ingredients = len(ingredients) if ingredients else 0
    total_days = len(meals_of_week) if meals_of_week else 7
    weekly_meal_count = sum(len(day) for day in (meals_of_week or [[]] * 7))
    
    has_all_ingredients = all(
        set(i.lower()) <= set((meal[0].get('ingredients', [])))
        for day in meals_of_week
        for meal in day
    ) if total_days > 0 and any(meals_of_week) else False

    metrics = {
        'total_recipes': total_recipes,
        'total_ingredients': total_ingredients,
        'planned_days': total_days,
        'weekly_meals': weekly_meal_count,
        'all_ingredients_covered': has_all_ingredients,
    }
    
    for key, value in metrics.items():
        print(f"{key}: {value}")

project_metrics()
