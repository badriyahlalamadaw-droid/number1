# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: MealPlanner
def reset_demo_data():
    """Сбрасывает все данные в демо-состояние и очищает UI."""
    global meals, products, recipes, shopping_list, day
    meals = [
        {"meal_type": "Breakfast", "dishes": ["Овсянка с ягодами", "Тост с авокадо"]},
        {"meal_type": "Lunch", "dishes": ["Салат Цезарь", "Куриный суп"]}
    ] * 7
    products = [
        {"name": "Куринное филе", "qty": 500, "unit": "г"},
        {"name": "Яйца", "qty": 12, "unit": "шт"},
        {"name": "Молоко", "qty": 1, "unit": "л"},
    ]
    recipes = [
        {"name": "Овсянка с ягодами", "ingredients": [{"item": "Овсяные хлопья", "amount": 80}, {"item": "Ягоды", "amount": 50}]},
        {"name": "Тост с авокадо", "ingredients": [{"item": "Хлеб", "amount": 2}, {"item": "Авокадо", "amount": 1}]},
    ]
    shopping_list = []
    day = 1

def clear_state():
    """Полностью очищает все данные и интерфейс."""
    global meals, products, recipes, shopping_list, day, current_edit_index
    meals = []
    products = []
    recipes = []
    shopping_list = []
    day = 0
    current_edit_index = None
