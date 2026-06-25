# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: MealPlanner
def search_items(query, data_list):
    query = query.lower().strip()
    if not query:
        return []
    results = []
    for item in data_list:
        text = f"{item.get('name', '')} {item.get('category', '')}".lower()
        if query in text or any(query in str(v).lower() for v in item.values()):
            results.append(item)
    return results
