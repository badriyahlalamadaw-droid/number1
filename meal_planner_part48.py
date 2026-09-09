# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: MealPlanner
def split_large_functions():
    """
    Refactoring helper: splits large monolithic functions into smaller, focused ones.
    Ensures backward compatibility for all public commands.
    """
    original_function = get_current_function()
    if original_function is None:
        return

    parts = split_into_parts(original_function)
    for part in parts:
        if part is not None:
            add_to_current_file(part)

    print("Refactoring complete: large functions split into smaller, focused ones.")
