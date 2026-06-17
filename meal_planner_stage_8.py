# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: MealPlanner
def show_menu():
    print("\n=== MealPlanner CLI ===")
    print("1. Показать меню на неделю")
    print("2. Добавить рецепт")
    print("3. Просмотреть продукты")
    print("4. Удалить продукт из списка покупок")
    print("5. Выход")
    try:
        choice = input("Выберите действие (1-5): ").strip()
        if choice == "1":
            for day, meal in MEAL_PLAN.items():
                print(f"{day}: {meal}")
        elif choice == "2":
            name = input("Название рецепта: ")
            ingredients = input("Продукты (через запятую): ").split(",")
            recipe = {"name": name, "ingredients": [ing.strip() for ing in ingredients]}
            RECIPES.append(recipe)
            print(f"Рецепт '{name}' добавлен.")
        elif choice == "3":
            if SHOPPING_LIST:
                print("Список покупок:")
                for item in SHOPPING_LIST:
                    print("- " + item)
            else:
                print("Список покупок пуст.")
        elif choice == "4":
            item = input("Название продукта для удаления: ")
            if item in SHOPPING_LIST:
                SHOPPING_LIST.remove(item)
                print(f"Продукт '{item}' удалён.")
            else:
                print(f"Продукт '{item}' не найден в списке.")
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите от 1 до 5.")
    except KeyboardInterrupt:
        print("\nПрограмма завершена пользователем.")
