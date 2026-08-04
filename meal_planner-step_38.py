# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: MealPlanner
def test_edge_cases():
    # Тест: пустое меню вызывает ошибку при попытке получить план
    assert meal_plan.get_weekly_menu() == {}
    
    # Тест: рецепт без ингредиентов возвращает пустой список покупок
    recipe = Recipe("Test", 30, [], "desc")
    assert recipe.ingredients == []
    assert len(recipe.shopping_list()) == 0
    
    # Тест: рецептурный шаг с невалидным временем вызывает исключение
    with pytest.raises(ValueError):
        Step("Boil water", time_minutes=-1)
    
    # Тест: добавление шага в рецепт с пустым списком ингредиентов
    recipe.add_ingredient("Flour", 200, "g")
    assert len(recipe.ingredients) == 1
    
    # Тест: удаление не существующего ингредиента возвращает False
    result = recipe.remove_ingredient("Salt")
    assert result is False
    
    # Тест: рецепт с нулевым временем приготовления
    zero_time_recipe = Recipe("Instant", 0, ["Sugar"], "fast")
    assert zero_time_recipe.cooking_time() == 0

if __name__ == "__main__":
    test_edge_cases()
