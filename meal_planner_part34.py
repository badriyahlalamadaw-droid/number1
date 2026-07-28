# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: MealPlanner
# --- Etap 34: Шаблоны для быстрого создания записей ---
TEMPLATES = [
    {"name": "Обычный приём пищи", "type": "meal", "fields": ["название", "количество_персон"]},
    {"name": "Продукт", "type": "ingredient", "fields": ["название", "вес_грамм"]},
    {"name": "Рецепт", "type": "recipe", "fields": ["название", "ингредиенты", "шаги"]},
    {"name": "Список покупок", "type": "shopping_list", "fields": ["продукты", "количество_персон"]},
]

TEMPLATE_DATA = {
    "meal": {"default_name": "Приём пищи", "default_persons": 1},
    "ingredient": {"default_weight": 50},
    "recipe": {"default_steps": []},
    "shopping_list": {"default_persons": 3},
}

def use_template(template_type, **overrides):
    """Создаёт пустую запись по шаблону и заполняет её. Возвращает (тип, данные)."""
    if template_type not in TEMPLATES:
        raise ValueError(f"Неизвестный шаблон: {template_type}. Доступные: {[t['name'] for t in TEMPLATES]}")
    
    data = {}
    if "meal" == template_type:
        data["название"] = overrides.get("название", TEMPLATE_DATA["meal"]["default_name"])
        data["количество_персон"] = int(overrides.get("количество_персон", TEMPLATE_DATA["meal"]["default_persons"]))
    elif "ingredient" == template_type:
        data["название"] = overrides.get("название", "Продукт")
        data["вес_грамм"] = int(overrides.get("вес_грамм", TEMPLATE_DATA["ingredient"]["default_weight"]))
    elif "recipe" == template_type:
        data["название"] = overrides.get("название", "Рецепт")
        data["ингредиенты"] = []
        data["шаги"] = []
    elif "shopping_list" == template_type:
        data["продукты"] = []
        data["количество_персон"] = int(overrides.get("количество_персон", TEMPLATE_DATA["shopping_list"]["default_persons"]))
    
    return (template_type, data)
