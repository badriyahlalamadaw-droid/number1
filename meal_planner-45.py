# === Stage 45: Добавь восстановление из резервной копии ===
# Project: MealPlanner
import json, os

BACKUP_PATH = "mealplanner_backup.json"

def save_backup():
    """Сохраняет текущее состояние проекта в резервную копию."""
    try:
        with open("mealplanner.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"menu": {}, "products": [], "recipes": [], "shopping_list": []}
    with open(BACKUP_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Резервная копия сохранена в", BACKUP_PATH)

def restore_backup():
    """Восстанавливает проект из резервной копии."""
    if not os.path.exists(BACKUP_PATH):
        print("Резервная копия не найдена!")
        return False
    try:
        with open(BACKUP_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        with open("mealplanner.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("Проект восстановлен из резервной копии.")
        return True
    except Exception as e:
        print("Ошибка восстановления:", e)
        return False

if __name__ == "__main__":
    save_backup()
    restore_backup()
