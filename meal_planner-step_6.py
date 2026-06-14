# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: MealPlanner
class FilteredList(list):
    def __init__(self, items):
        super().__init__()
        self.extend(items)
    
    def filter(self, status=None, category=None, tags=None):
        result = []
        for item in self:
            if status and item.get('status') != status:
                continue
            if category and item.get('category') != category:
                continue
            if tags:
                item_tags = set(item.get('tags', []))
                if not any(tag in item_tags for tag in tags):
                    continue
            result.append(dict(item))
        return FilteredList(result)

def get_filtered_items(items, status=None, category=None, tags=None):
    filtered = items.filter(status=status, category=category, tags=tags)
    return [dict(i) for i in filtered]
