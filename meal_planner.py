# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: MealPlanner
import json
from datetime import datetime, timedelta

# --- Демонстрационные данные (Mock Data) ---
MEALS = {
    "Monday": ["Овсянка с ягодами", "Салат Цезарь", "Курица с овощами"],
    "Tuesday": ["Творожная запеканка", "Суп-пюре из брокколи", "Гречка с котлетой"],
    "Wednesday": ["Яичница с томатами", "Паста Карбонара", "Щи"],
    "Thursday": ["Рыба на пару", "Салат из свежих овощей", "Борщ"],
    "Friday": ["Куриное филе в духовке", "Гарнир из риса", "Фруктовый салат"]
}

SHOPPING_LIST = [
    {"item": "Молоко", "quantity": 1, "unit": "л"},
    {"item": "Яйца", "quantity": 10, "unit": "шт"},
    {"item": "Куриное филе", "quantity": 500, "unit": "г"},
    {"item": "Рис", "quantity": 1, "unit": "кг"}
]

# --- Точка входа и логика ---

def get_week_schedule():
    """Генерирует расписание на текущую неделю."""
    today = datetime.now()
    start_day = (today.weekday() + 1) % 7 # Понедельник = 0
    schedule = {}
    
    for i in range(7):
        day_name = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][i]
        date = today + timedelta(days=i - start_day)
        schedule[day_name] = {
            "date": date.strftime("%d.%m"),
            "meals": MEALS.get(day_name, ["Суп", "Хлеб", "Чай"])
        }
    return schedule

def print_menu():
    """Выводит меню на неделю."""
    print("\n=== Меню на неделю ===")
    for day, data in get_week_schedule().items():
        print(f"{day}: {data['date']}")
        for meal in data["meals"]:
            print(f"  - {meal}")

def generate_shopping_list():
    """Генерирует список покупок (упрощенно)."""
    print("\n=== Список покупок ===")
    for item in SHOPPING_LIST:
        print(f"{item['quantity']} {item['unit']} {item['item']}")

if __name__ == "__main__":
    print("Запуск MealPlanner...")
    print_menu()
    generate_shopping_list()
