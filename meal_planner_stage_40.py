# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: MealPlanner
def main():
    import argparse
    parser = argparse.ArgumentParser(description="MealPlanner CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    # меню
    p_menu = sub.add_parser("menu", help="показать/создать меню")
    p_menu.add_argument("--create", help="создать меню на неделю")
    p_menu.add_argument("--show", action="store_true", help="показать меню")

    # рецепты
    p_recipes = sub.add_parser("recipes", help="работа с рецептами")
    p_recipes.add_argument("--list", action="store_true", help="список рецептов")
    p_recipes.add_argument("--add", help="добавить рецепт")

    # продукты
    p_products = sub.add_parser("products", help="работа с продуктами")
    p_products.add_argument("--list", action="store_true", help="список продуктов")
    p_products.add_argument("--add", help="добавить продукт")

    # покупки
    p_shop = sub.add_parser("shop", help="список покупок")
    p_shop.add_argument("--show", action="store_true", help="показать список")
    p_shop.add_argument("--clear", action="store_true", help="очистить список")

    args = parser.parse_args()

    if args.command == "menu":
        if args.create:
            create_weekly_menu()
        elif args.show:
            show_menu()
        else:
            print("Укажите --create или --show")

    elif args.command == "recipes":
        if args.list:
            list_recipes()
        elif args.add:
            add_recipe(args.add)
        else:
            print("Укажите --list или --add")

    elif args.command == "products":
        if args.list:
            list_products()
        elif args.add:
            add_product(args.add)
        else:
            print("Укажите --list или --add")

    elif args.command == "shop":
        if args.show:
            show_shop_list()
        elif args.clear:
            clear_shop_list()
        else:
            print("Укажите --show или --clear")
