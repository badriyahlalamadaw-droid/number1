# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: MealPlanner
import json, sys

def load_initial_data(json_string):
    data = json.loads(json_string)
    
    recipes = {}
    for r in data.get("recipes", []):
        name = r["name"]
        ingredients = {ing["name"]: ing["amount"] for ing in r["ingredients"]}
        steps = r.get("steps", [])
        prep_time = r.get("prepTime", 0)
        recipes[name] = {"ingredients": ingredients, "steps": steps, "prepTime": prep_time}
    
    meals = {}
    for m in data.get("meals", []):
        name = m["name"]
        day = m.get("day", "Monday")
        recipe_name = m.get("recipeName", "")
        if not recipe_name:
            continue
        if recipe_name in recipes:
            meals[name] = {"day": day, "recipe": recipe_name}
    
    shopping_list = {}
    for r_name, info in recipes.items():
        for name, amount in info["ingredients"].items():
            if name not in shopping_list or shopping_list[name]["amount"] < amount:
                shopping_list[name] = {"name": name, "amount": amount}
    
    return {
        "recipes": recipes,
        "meals": meals,
        "shoppingList": list(shopping_list.values())
    }

initial_json_string = '''
{
  "recipes": [
    {
      "name": "Омлет",
      "ingredients": [{"name": "Яйца", "amount": 4}, {"name": "Молоко", "amount": 50}],
      "steps": ["Взбить яйца с молоком", "Жарить на сковороде"],
      "prepTime": 10
    },
    {
      "name": "Паста Карбонара",
      "ingredients": [{"name": "Макароны", "amount": 200}, {"name": "Бекон", "amount": 100}],
      "steps": ["Сварить макароны", "Обжарить бекон"],
      "prepTime": 25
    }
  ],
  "meals": [
    {
      "name": "Завтрак Пн",
      "day": "Monday",
      "recipeName": "Омлет"
    },
    {
      "name": "Обед Вт",
      "day": "Tuesday",
      "recipeName": "Паста Карбонара"
    }
  ]
}
'''

initial_data = load_initial_data(initial_json_string)
