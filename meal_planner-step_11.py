# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: MealPlanner
import json, os

def save_data(data):
    with open('meal_planner.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_data():
    if not os.path.exists('meal_planner.json'):
        return {'menu': [], 'products': [], 'recipes': []}
    try:
        with open('meal_planner.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {'menu': [], 'products': [], 'recipes': []}

def init_storage():
    save_data({'menu': [], 'products': [], 'recipes': []})
