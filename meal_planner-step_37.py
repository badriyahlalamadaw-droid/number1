# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: MealPlanner
import unittest


class TestMealPlanner(unittest.TestCase):
    def test_add_ingredient(self):
        meal = Meal()
        meal.add_ingredient("Яблоки", 3)
        self.assertEqual(meal.ingredients, {"Яблоки": 3})

    def test_add_recipe(self):
        recipe = Recipe(name="Салат", duration=20)
        meal = Meal()
        meal.add_recipe(recipe)
        self.assertIn(recipe, meal.recipes.values())

    def test_list_of_shopping(self):
        planner = Planner()
        planner.add_ingredient("Молоко", 1)
        planner.add_ingredient("Хлеб", 2)
        items = planner.list_of_shopping()
        self.assertEqual(items, ["Молоко: 1 шт.", "Хлеб: 2 шт."])

    def test_plan_week(self):
        planner = Planner()
        recipe1 = Recipe(name="Омлет", duration=15)
        recipe2 = Recipe(name="Суп", duration=40)
        meal1 = Meal()
        meal1.add_recipe(recipe1)
        meal2 = Meal()
        meal2.add_recipe(recipe2)
        planner.plan_week([meal1, meal2])
        self.assertEqual(planner.week_plan, [meal1, meal2])


if __name__ == "__main__":
    unittest.main()
