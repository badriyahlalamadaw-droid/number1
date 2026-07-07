# === Stage 20: Добавь восстановление записей из архива ===
# Project: MealPlanner
def load_archive(self):
        archive_path = "meal_planner_archive.txt"
        if not os.path.exists(archive_path):
            return
        with open(archive_path, 'r', encoding='utf-8') as f:
            lines = [l.strip() for l in f.readlines() if l.strip()]
        for line in lines:
            parts = line.split('|||')
            if len(parts) != 4:
                continue
            rec_id, meal_type, day_idx, recipe_name = map(int, parts[:3])
            recipe_name_str = parts[3]
            existing = None
            for r in self.recipes:
                if r.id == rec_id and r.name == recipe_name_str:
                    existing = r
                    break
            if existing is None:
                continue
            if len(existing.ingredients) != 0 or meal_type not in ('breakfast', 'lunch', 'dinner') or day_idx > 6:
                continue
            idx = next((i for i, d in enumerate(self.days['meal_types']) if d == meal_type and i >= day_idx), None)
            if idx is None:
                continue
            self.days['meals'][idx] = existing.name
