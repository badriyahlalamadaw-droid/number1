# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: MealPlanner
def calculate_monthly_statistics(meals, recipes):
    from datetime import date, timedelta
    
    current_year = date.today().year
    start_date = date(current_year, 1, 1)
    end_date = date(today.year, today.month + 1, 0) if today.month < 12 else date(today.year + 1, 1, 1)
    
    monthly_stats = {}
    for d in range((end_date - start_date).days):
        stat_date = start_date + timedelta(days=d)
        month_key = f"{stat_date.year}-{stat_date.month:02d}"
        
        if month_key not in monthly_stats:
            monthly_stats[month_key] = {
                "total_meals": 0,
                "unique_recipes": set(),
                "ingredients_used": {}
            }
            
        meal_data = meals.get(stat_date)
        if meal_data and 'recipe_id' in meal_data:
            recipe_id = meal_data['recipe_id']
            monthly_stats[month_key]['total_meals'] += 1
            monthly_stats[month_key]['unique_recipes'].add(recipe_id)
            
            if recipe_id in recipes:
                for ingredient, amount in recipes[recipe_id].get('ingredients', {}).items():
                    current_amount = monthly_stats[month_key]['ingredients_used'].get(ingredient, 0)
                    monthly_stats[month_key]['ingredients_used'][ingredient] = current_amount + amount
                    
    return monthly_stats
