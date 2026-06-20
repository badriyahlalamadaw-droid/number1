# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: MealPlanner
def export_to_json():
    import json
    state = {
        "menu": menu,
        "products": products,
        "recipes": recipes,
        "shopping_list": shopping_list,
        "week_days": week_days
    }
    return json.dumps(state, indent=2, ensure_ascii=False)
