# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: MealPlanner
import json, os

def migrate_data():
    """Перед миграцией: сохранить текущую структуру.
    После: записать новый JSON с меткой версии и обновлёнными рецептами.
    """
    file_path = os.path.join(os.path.dirname(__file__), 'meal_data.json')
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {'version': 1, 'recipes': [], 'menu': [], 'shopping_list': []}
    if data.get('version', 1) < 2:
        data['version'] = 2
        for r in data.get('recipes', []):
            r.setdefault('ingredients', [])
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("Миграция завершена: версия обновлена до 2.")
    return data
