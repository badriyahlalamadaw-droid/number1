# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: MealPlanner
def self_check():
    print("=" * 60)
    print("MealPlanner — Самопроверка приложения")
    print("=" * 60)
    
    # Проверка наличия ключевых сущностей
    entities = {
        "Рецепты": recipes,
        "Продукты": products,
        "Меню на неделю": weekly_menu,
        "Список покупок": shopping_list,
    }
    
    for name, obj in entities.items():
        if obj is None:
            print(f"[ОШИБКА] {name} не определены")
        elif isinstance(obj, dict) and len(obj) == 0:
            print(f"[ВНИМАНИЕ] {name} — пустой")
        else:
            print(f"[OK] {name} — {len(obj)} элементов")
    
    # Проверка структуры рецептов
    if recipes:
        sample = list(recipes.values())[0]
        required_keys = ["name", "ingredients", "instructions"]
        missing = [k for k in required_keys if k not in sample]
        if missing:
            print(f"[ОШИБКА] Рецепт '{sample.get('name', 'unknown')}' — не хватает: {missing}")
        else:
            print(f"[OK] Структура рецептов — корректна")
    
    # Проверка структуры продуктов
    if products:
        sample = list(products.values())[0]
        required_keys = ["name", "quantity"]
        missing = [k for k in required_keys if k not in sample]
        if missing:
            print(f"[ОШИБКА] Продукт '{sample.get('name', 'unknown')}' — не хватает: {missing}")
        else:
            print(f"[OK] Структура продуктов — корректна")
    
    # Проверка меню
    if weekly_menu:
        days = list(weekly_menu.keys())
        print(f"[OK] Меню на неделю — {days}")
    
    # Проверка списка покупок
    if shopping_list:
        print(f"[OK] Список покупок — {len(shopping_list)} позиций")
    
    # Проверка функций интерфейса
    ui_functions = ["display_menu", "display_recipes", "display_products", "display_shopping_list"]
    for func_name in ui_functions:
        if func_name not in globals():
            print(f"[ОШИБКА] Функция {func_name} не определена")
        else:
            print(f"[OK] Функция {func_name} — доступна")
    
    print("=" * 60)
    print("Самопроверка завершена")
    print("=" * 60)

self_check()
