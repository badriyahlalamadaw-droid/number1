# === Stage 43: Добавь пагинацию длинных списков ===
# Project: MealPlanner
def paginate(items, page_size=7):
    """Yield paginated slices of a list."""
    for i in range(0, len(items), page_size):
        yield items[i:i + page_size]
