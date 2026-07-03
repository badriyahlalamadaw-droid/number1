# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: MealPlanner
class TagManager:
    def __init__(self, tags_db):
        self.tags_db = tags_db
    
    def add_tag(self, tag_name):
        if not any(t.lower() == tag_name.lower() for t in self.tags_db):
            self.tags_db.append(tag_name)
    
    def remove_tag(self, tag_name):
        try:
            index = next(i for i, t in enumerate(self.tags_db) if t.lower() == tag_name.lower())
            del self.tags_db[index]
        except StopIteration:
            pass
    
    def get_tags_for_recipe(self, recipe_id):
        return [t for t in self.tags_db if any(t.lower() in r.get('tags', []) for r in self.recipes if r['id'] == recipe_id)]

# Инициализация менеджера тегов (пример использования)
tag_manager = TagManager(tags_db=[])
