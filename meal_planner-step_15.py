# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: MealPlanner
def generate_weekly_statistics(meals, recipes):
    from datetime import date, timedelta
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    stats = {d: {'calories': 0, 'meals_count': 0} for d in range(week_start, week_start + 7)}
    
    def get_recipe_stats(meal):
        r_key = meal.get('recipe_id') or ''
        if not r_key: return None
        recipe = recipes.get(r_key)
        if not recipe: return None
        
        ingredients_needed = []
        for ing in recipe['ingredients']:
            needed_qty = float(ing['qty'] * (meal.get('servings', 1)))
            existing = next((i for i in ingredients_needed if i['name'] == ing['name']), None)
            if existing:
                existing['needed'] += needed_qty
            else:
                ingredients_needed.append({'name': ing['name'], 'qty': float(ing['qty'])})
        return {'recipe_name': recipe['name'], 'ingredients': ingredients_needed}

    for day_offset in range(7):
        current_date = week_start + timedelta(days=day_offset)
        meal_plan = meals.get(current_date.strftime('%Y-%m-%d'), [])
        
        if not meal_plan: continue
        
        total_calories = 0
        unique_ingredients = {}

        for meal in meal_plan:
            recipe_stats = get_recipe_stats(meal)
            if recipe_stats is None: continue
            
            ingredients = recipe_stats['ingredients']
            
            for ing_data in ingredients:
                name = ing_data['name']
                needed_qty = float(ing_data['qty'])
                
                if name not in unique_ingredients:
                    unique_ingredients[name] = {'needed': 0, 'recipe_names': set()}
                
                unique_ingredients[name]['needed'] += needed_qty
                recipe_name = recipe_stats['recipe_name']
                if recipe_name not in unique_ingredients[name]['recipe_names']:
                    unique_ingredients[name]['recipe_names'].add(recipe_name)

            total_calories += meal.get('calories', 0)
        
        stats[current_date] = {
            'total_calories': int(total_calories),
            'unique_meals_count': len(meal_plan),
            'shopping_list': list(unique_ingredients.items())
        }
    
    return stats
